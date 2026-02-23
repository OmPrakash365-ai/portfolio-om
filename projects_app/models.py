from django.db import models
from django.utils.text import slugify

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)   # 🔥 important
    description = models.TextField()
    tech_stack = models.CharField(max_length=200, blank=True)

    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    live_demo = models.URLField(blank=True, null=True)

    created_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            count = 1

            while Project.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"
                count += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title