from django.contrib import admin
from django.apps import apps
from django.core.exceptions import ImproperlyConfigured

app_models = apps.get_app_config("sensorthings").get_models()

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
