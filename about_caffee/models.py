from django.db import models

# Create your models here.
# blog/models.py

from django.db import models
from django.utils.text import slugify

class BlogCategory(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="عنوان دسته‌بندی")
    slug = models.SlugField(unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True, verbose_name="تصویر دسته بندی")
    class Meta:
        verbose_name = "دسته‌بندی بلاگ"
        verbose_name_plural = "دسته‌بندی‌های بلاگ"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class BlogPost(models.Model):
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name='posts', verbose_name="دسته‌بندی")
    title = models.CharField(max_length=200, verbose_name="عنوان مطلب")
    slug = models.SlugField(unique=True, blank=True, null=True)
    short_description = models.TextField(verbose_name="توضیح کوتاه", blank=True)
    content = models.TextField(verbose_name="محتوای مطلب")
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True, verbose_name="تصویر مطلب")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "مطلب بلاگ"
        verbose_name_plural = "مطالب بلاگ"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
