from django.contrib import admin

# Register your models here.
from .models import BookGuest
class GuestBookAdmin(admin.ModelAdmin):
    list_display = ('author', 'email', 'status')
    list_filter = ('status', 'created_at')
    search_fields = ['author']
    fields = ['author', 'email','status', 'content','created_at', 'updated_at']

admin.site.register(BookGuest, GuestBookAdmin)
