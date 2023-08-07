from django.contrib import admin
from .models import (
    User,
    Music,
    Artist
)
# Register your models here.

admin.site.register([User,Music,Artist])
