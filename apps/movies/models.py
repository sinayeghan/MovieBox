from django.db import models


class Genre(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    slug = models.SlugField(
        max_length=100,
        unique=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(
        max_length=255,
    )

    slug = models.SlugField(
        max_length=255,
        unique=True,
    )

    biography = models.TextField(
        blank=True,
    )

    photo = models.ImageField(
        upload_to="people/photos/",
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(
        max_length=255,
    )

    slug = models.SlugField(
        max_length=255,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    poster = models.ImageField(
        upload_to="movies/posters/",
        blank=True,
    )

    release_year = models.PositiveSmallIntegerField()

    duration = models.PositiveSmallIntegerField(
        help_text="Duration in minutes",
    )

    country = models.CharField(
        max_length=100,
        blank=True,

    )

    language = models.CharField(
        max_length=100,
        blank=True,
    )

    genres = models.ManyToManyField(
        Genre,
        related_name="movies",
    )

    people = models.ManyToManyField(
        Person,
        through="MoviePerson",
        related_name="movies",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.title

class MovieImage(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="images",
    )
    image = models.ImageField(
        upload_to="movies/gallery/",
    )
    sort_order = models.PositiveIntegerField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["sort_order"]
        constraints = [
            models.UniqueConstraint(
                fields=["movie", "sort_order"],
                name="unique_movie_image_order",
            ),
        ]

    def __str__(self):
        return f"{self.movie.title} - Image {self.sort_order}"

class MoviePerson(models.Model):
    class Role(models.TextChoices):
        ACTOR = "ACTOR", "Actor"
        DIRECTOR = "DIRECTOR", "Director"

    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="movie_people",
    )

    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="movie_people",
    )

    role = models.CharField(
        max_length=20,
        choices=Role,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["movie", "person", "role"],
                name="unique_movie_person_role",
            ),
        ]

    def __str__(self):
        return f"{self.person} - {self.role}"