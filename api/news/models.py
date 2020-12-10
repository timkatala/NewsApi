from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from api.tag.models import Tag

class Language(models.Model):

    LANGUAGE_CHOICES = [
        ('ru', 'Russian'),
        ('uz', 'Uzbek')
    ]
    language = models.CharField(max_length=2, primary_key=True)

    def __str__(self):
        return dict(self.LANGUAGE_CHOICES)[str(self.language)]

class News(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.DO_NOTHING)
    title = models.TextField(null=False, blank=False)
    description = models.TextField(_('Описание'), null=False, blank=False)
    date_joined = models.DateTimeField(_('Дата создания'), default=timezone.now)
    tag = models.ManyToManyField(Tag, verbose_name=_('Теги'), related_name='news'),

    def __str__(self):
    	return self.title	
