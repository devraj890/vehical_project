from django.contrib import admin
from django.contrib.auth.decorators import user_passes_test
from .models import myuser
def is_manager(user):
    return user.is_authenticated and user.is_manager
admin.site.register(myuser)

# Restrict access to a view only to managers
@user_passes_test(is_manager)
def manager_only_view(request):
    pass
    # Handle logic for manager-only view
