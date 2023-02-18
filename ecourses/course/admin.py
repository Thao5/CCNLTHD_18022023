from django.contrib import admin
from .models import *

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'created_date', 'active']
    search_fields = ['subject']
    list_filter = ['subject', 'created_date']

admin.site.register(Category)
admin.site.register(Courses, CourseAdmin)