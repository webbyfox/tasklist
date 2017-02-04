from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

def get_user():
    # current_user = auth.username
    return User.get_username()

status_list =  (
    ('N', 'UNDONE'),
    ('Y', 'DONE'),
)

class MetaColumn(models.Model):
    created_by = models.CharField(max_length=64)
    created_on = models.DateTimeField('creation date', auto_now_add=True)
    amended_by = models.CharField(max_length=64)
    amended_on = models.DateTimeField('revision date', auto_now=True)

    class Meta:
        abstract = True


class Task(MetaColumn):


    title = models.CharField(max_length = 250)
    description = models.TextField()
    done = models.CharField(max_length=1, default='N', choices = status_list)

    class Meta:
        ordering = ('created_on',)

    def __init__(self, *args, **kwargs):
        kwargs['created_by'] = 'admin'
        kwargs['amended_by'] = 'admin'
        super(Task, self).__init__(*args, **kwargs)


    def __unicode__(self):
         #Tell it to return as a unicode string (The title of the task item) rather than just Object.
        return self.title
