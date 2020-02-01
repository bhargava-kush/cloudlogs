from django.shortcuts import render

from .models import Logs
from .serializers import LogSerializer
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from django_filters import rest_framework as filters
from .utils import check_status_len


# Create your views here.

class LogFilter(filters.FilterSet):
    title = filters.CharFilter(field_name="title", lookup_expr="icontains")
    description = filters.CharFilter(field_name="description", lookup_expr="icontains")
    status = filters.NumberFilter(field_name='status')
    content = filters.CharFilter(field_name='content', lookup_expr="icontains")
    source = filters.CharFilter(field_name="source", lookup_expr="icontains")

    class Meta:
        model = Logs
        fields = ['title', 'description', 'status', 'content', 'source']


class LogsViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    To create/list/retrieve logs
    """
    serializer_class = LogSerializer
    queryset = Logs.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = LogFilter


    def create(self, request):
        """
        To create logs
        :return:
        """
        data = self.request.data
        if not check_status_len(data['status']):
            return Response({"error":"Invalid status"}, status=400)

        if 'file' in request.data:
            data_file = file.readline()
            log = Logs()
            log.from_file(data_file)
            log.save()
            return Response(status=201)

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=400)

        return Response(serializer.data, status=201)

