from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


ALLOW_NUMBER_ONLY = RegexValidator(r'^[0-9]*$',
                                   'Only numeric characters are allowed.')


class User(AbstractUser):
    AbstractUser._meta.get_field('first_name').max_length = 60
    AbstractUser._meta.get_field('last_name').max_length = 60
    age = models.CharField(max_length=10)
    mobile_number = models.CharField(max_length=10,
                                    validators=[ALLOW_NUMBER_ONLY],
                                    unique=True,
                                    db_index=True,
                                    blank=True,
                                    )
    AbstractUser._meta.get_field('email').max_length = 60
    
    def __str__(self):
        return '%s' % self.username

    class Meta:
        verbose_name_plural = "User" 
        verbose_name = 'User'
        ordering = ('username',)


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
    	verbose_name='code'
        ordering = ('created',)