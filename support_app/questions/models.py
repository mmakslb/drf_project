from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
import datetime
import random
import string
from django.contrib.auth import get_user_model


User = get_user_model()


class Question(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='question_sender')
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=500)
    slug = models.SlugField(blank=True)
    status = models.CharField(default='actual', max_length=6, choices=[('actual', 'actual'),
                                                                       ('solved', 'solved'), ('frozen', 'frozen')])
    timestamp = models.DateTimeField(auto_now_add=datetime.datetime.now())

    class Meta:
        ordering = ['timestamp']
        verbose_name_plural = "Question"

    def __str__(self):
        return self.title


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_sender')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='messages')
    text = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ('timestamp',)


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


@receiver(pre_save, sender=Question)
def slugify_name(instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(rand_slug() + "-" + instance.title)


