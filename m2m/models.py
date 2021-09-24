from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):

    favorites = models.ManyToManyField("self", blank=True, symmetrical=False)

    phone = models.CharField(max_length=50)
    is_autor = models.BooleanField(default=False)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.username


class Post(models.Model):

    autors = models.ManyToManyField("m2m.User", related_name="my_posts")
    likes = models.ManyToManyField("m2m.User", related_name="liked_posts",
                                   through='Like', through_fields=('post', 'user'))

    title = models.CharField(max_length=200)
    text = models.TextField()

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        return self.title


class Like(models.Model):

    user = models.ForeignKey("m2m.User", on_delete=models.CASCADE)
    post = models.ForeignKey("m2m.Post", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "like"
        verbose_name_plural = "likes"

    def __str__(self):
        return self.id
