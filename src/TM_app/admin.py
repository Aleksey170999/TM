from django.contrib import admin
from .models import TimesModel

# Register your models here.
# admin.site.register(TimesModel)

@admin.register(TimesModel)
class TimesModelAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user_name = request.user
        super().save_model(request, obj, form, change)