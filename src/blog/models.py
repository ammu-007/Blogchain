from django import forms
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models import Q

User = settings.AUTH_USER_MODEL


class BlogPostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(published_date__lte=now)

    def search(self, query):
        lookup = (
            Q(title__icontains=query)
            | Q(content__icontains=query)
            | Q(user__first_name__icontains=query)
            | Q(user__first_name__icontains=query)
            | Q(user__username__icontains=query)
        )
        return self.filter(lookup)


class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, self._db)

    def published(self):
        return self.get_queryset().published()

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        else:
            return self.get_queryset().published().search(query)


# Create your models here.
class BlogPost(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="image/", blank=True, null=True)
    published_date = models.DateTimeField(
        auto_now=False, auto_now_add=False, null=True, blank=True
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = BlogPostManager()

    class Meta:
        ordering = ["-published_date", "-updated", "-timestamp"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/blog/{ self.slug }"  # /blog/<slug>

    def get_delete_url(self):
        print("Watch this", f"{ self.get_absolute_url }/delete")
        return f"/blog/{ self.slug }/delete"

    def get_edit_url(self):
        return f"/blog/{ self.slug }/edit"
