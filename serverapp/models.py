import uuid

from django.db import models


# Create your models here.

# Tables
class Users(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    password = models.CharField(max_length=512)  # todo czy to nie będzie za krótkie na hashe

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f'{self.email} {self.username}'


class Achievements(models.Model):
    achievement_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256)
    description = models.TextField()

    class Meta:
        verbose_name = "Achievement"
        verbose_name_plural = "Achievements"
    def __str__(self):
        return f'{self.name}'


class Mountains(models.Model):
    mountain_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mountain_name = models.CharField(max_length=256)
    description = models.TextField()
    image_path = models.CharField(max_length=256)
    image_source = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Mountain"
        verbose_name_plural = "Mountains"

    def __str__(self):
        return f'{self.mountain_name}'


class Comments(models.Model):
    comment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
    mountain_id = models.ForeignKey('Mountains', on_delete=models.CASCADE)
    root_comment_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f'{self.content[:10]}'


# Relations
class Users_Achievements(models.Model):
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
    achievement_id = models.ForeignKey('Achievements', on_delete=models.CASCADE)


class Users_Mountains(models.Model):
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
    mountain_id = models.ForeignKey('Mountains', on_delete=models.CASCADE)
