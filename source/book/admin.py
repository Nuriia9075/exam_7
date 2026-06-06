from django.contrib import admin

# Register your models here.
from .models import BookGuest
class GuestBookAdmin(admin.ModelAdmin):
    list_display = ('author', 'email', 'status')
    list_filter = ('status', 'created_at')
    search_fields = ['author']
    fields = ['author', 'email','status', 'content']

admin.site.register(BookGuest, GuestBookAdmin)
