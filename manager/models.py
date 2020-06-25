from django.db import models


class Password(models.Model):
    software_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    website_link = models.TextField(max_length=500)
    seq_qu_1 = models.TextField(max_length=500)
    seq_ans_1 = models.TextField(max_length=250)
    seq_qu_2 = models.TextField(max_length=500)
    seq_ans_2 = models.TextField(max_length=250)
    notes = models.TextField(max_length=500)
    date_added = models.DateTimeField('date added')
    date_modified = models.DateTimeField('data last modified')

    def __str__(self):
        return self.software_name

    def was_modified(self):
        return self.date_added != self.date_modified
