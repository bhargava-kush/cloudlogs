from django.db import models

# Create your models here.
class Logs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.PositiveIntegerField()
    content = models.TextField()
    source = models.CharField(max_length=100)

    @classmethod
    def from_file(cls, line):
        log = cls.create(title=title, description=description, status=status, content=content, source=source)
        return log

    def __str__(self):
        return self.title

    class Meta:
        db_table = "logs"

