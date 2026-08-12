from django.db import models


class Genre(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    slug = models.SlugField(
        max_length=100,
        unique=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(
        max_length=255
    )

    slug = models.SlugField(
        max_length=255,
        unique=True
    )

    description = models.TextField(blank=True)

    poster = models.ImageField(
    upload_to="movies/posters/",
    blank=True
)

    release_year = models.PositiveSmallIntegerField()

    duration = models.PositiveSmallIntegerField(
        help_text="Duration in minutes"
    )

    genres = models.ManyToManyField(
        Genre,
        related_name="movies"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title