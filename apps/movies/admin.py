from django.contrib import admin

from .models import Genre, Movie


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
        "slug": ("name",)
    }


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "release_year",
        "duration",
        "created_at",
    )

    search_fields = (
        "title",
    )

    list_filter = (
        "release_year",
        "genres",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }