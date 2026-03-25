from django.contrib import admin
from django.apps import apps
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings

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

# load admin if not disabled
if (not hasattr(settings, "SENSORTHINGS_DISABLE_MODELS") or settings.SENSORTHINGS_DISABLE_MODELS is False) and (not hasattr(settings, "SENSORTHINGS_DISABLE_ADMIN") or settings.SENSORTHINGS_DISABLE_ADMIN is False):
    load_admin()


