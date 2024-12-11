from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)


class Master(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(Person, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields=['title'], name='master_title_idx'),
            models.Index(fields=['code'], name='master_code_idx'),
        ]

    def __str__(self):
        return self.title


class Subsidiary(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(Person, on_delete=models.CASCADE)
    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name='subsidiaries')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    is_deleted = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields=['title'], name='subsidiary_title_idx'),
            models.Index(fields=['code'], name='subsidiary_code_idx'),
        ]

    def __str__(self):
        return self.title
