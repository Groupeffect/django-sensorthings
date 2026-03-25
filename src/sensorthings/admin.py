from django.contrib import admin
from django.apps import apps
from django.core.exceptions import ImproperlyConfigured

app_models = apps.get_app_config("sensorthings").get_models()

def load_admin():
    for model in app_models:
        # Create a dynamic Admin class
        class DynamicAdmin(admin.ModelAdmin):
            verbose_name = "Sensor"
            list_display = [field.name for field in model._meta.fields]

        try:
            admin.site.register(model, DynamicAdmin)
        except admin.sites.AlreadyRegistered:
            pass

        except ImproperlyConfigured:
            pass

if not hasattr(settings, "SENSORTHINGS_DISABLE_MODELS") and not hasattr(
    settings, "SENSORTHINGS_DISABLE_ADMIN"
):
    load_admin()

elif (
    hasattr(settings, "SENSORTHINGS_DISABLE_MODELS")
    and hasattr(settings, "SENSORTHINGS_DISABLE_ADMIN")
    and settings.SENSORTHINGS_DISABLE_MODELS is False
    and settings.SENSORTHINGS_DISABLE_ADMIN is False
):
    load_admin()

elif (
    not hasattr(settings, "SENSORTHINGS_DISABLE_MODELS")
    and hasattr(settings, "SENSORTHINGS_DISABLE_ADMIN")
    and settings.SENSORTHINGS_DISABLE_ADMIN is False
):
    load_admin()

elif (
    hasattr(settings, "SENSORTHINGS_DISABLE_MODELS")
    and settings.SENSORTHINGS_DISABLE_MODELS is False
    and not hasattr(settings, "SENSORTHINGS_DISABLE_ADMIN")
):
    load_admin()

