
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    content = RichTextUploadingField()
    featured_image = models.ImageField(upload_to='posts/', blank=True, null=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def can_publish(self, user):
        """
        HARD RULE:
        Only Editors or Superusers can publish
        """
        return (
            user.is_superuser or
            user.groups.filter(name='Editor').exists()
        )

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'Comment by {self.name}'


class AuthorApplication(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # message = models.TextField(blank=True)
    message = RichTextUploadingField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({'Approved' if self.approved else 'Pending'})"



























# from django.db import models
# from django.contrib.auth.models import User
# from django.utils.text import slugify
# from ckeditor_uploader.fields import RichTextUploadingField

# def can_publish(self, user):
#     return user.groups.filter(name='Editors').exists() or user.is_superuser


# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     slug = models.SlugField(unique=True)

#     def __str__(self):
#         return self.name


# class Post(models.Model):
#     STATUS_CHOICES = (
#         ('draft', 'Draft'),
#         ('published', 'Published'),
#     )

#     title = models.CharField(max_length=200)
#     slug = models.SlugField(unique=True, blank=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
#     # content = models.TextField()
#     content = RichTextUploadingField()
#     featured_image = models.ImageField(upload_to='posts/', blank=True, null=True)
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ['-created_at']

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.title)
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return self.title
    





# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     content = models.TextField()
#     approved = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['created_at']

#     def __str__(self):
#         return f'Comment by {self.name}'

