from django.contrib import admin
from .models import Pages
class PagesAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    list_display = ('title', 'order')
    list_editable = ('order',)

admin.site.register(Pages, PagesAdmin)