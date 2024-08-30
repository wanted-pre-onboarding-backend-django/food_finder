from django.contrib import admin
from restaurant.models import Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    """Admin for Restaurant model"""

    list_display = (
        "name",
        "category",
        "status",
        # "sigun",
        "road_addr",
        "rating",
    )
    list_filter = (
        "category",
        "status",
        # "sigun",
    )
    search_fields = ("name", "road_addr", "lot_addr")

    fieldsets = (
        (None, {"fields": ("name", "category", "status", "sigun")}),
        ("Location Information", {"fields": ("road_addr", "lot_addr", "lat", "lon")}),
        ("Additional Information", {"fields": ("rating",)}),
    )

    ordering = ("name",)