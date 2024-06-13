from django.contrib import admin
from django.apps import apps

# Retrieve the app configuration
app = apps.get_app_config('api')

# Iterate over all models and register them
for model in app.get_models():
    admin.site.register(model)
