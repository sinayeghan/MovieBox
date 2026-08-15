from django.contrib import admin

from .models import Genre, Movie, MoviePerson, Person


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
        "created_at",
    )

    search_fields = (
        "name",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }


class MoviePersonInline(admin.TabularInline):
    model = MoviePerson
    extra = 1


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "release_year",
        "duration",
        "country",
        "language",
        "created_at",
    )

    search_fields = (
        "title",
    )

    list_filter = (
        "release_year",
        "country",
        "language",
        "genres",
    )

    prepopulated_fields = {
        "slug": ("title",),
    }

    inlines = (
        MoviePersonInline,
    )


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "created_at",
    )

    search_fields = (
        "name",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }


@admin.register(MoviePerson)
class MoviePersonAdmin(admin.ModelAdmin):
    list_display = (
        "movie",
        "person",
        "role",
    )

    list_filter = (
        "role",
    )

    search_fields = (
        "movie__title",
        "person__name",
    )

    autocomplete_fields = (
        "movie",
        "person",
    )