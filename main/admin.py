from django.contrib import admin
from .models import Student, Faculty, FacSpec
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'faculty', 'specialization', 'created_ad', 'updated_ad', 'is_visited', 'pincode')
    list_display_links = ('id', 'specialization')
    search_fields = ('specialization',)
    list_editable = ('is_visited',)
    list_filter = ('is_visited', 'faculty')


class FacultyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

class FacSpecAdmin(admin.ModelAdmin):
    list_display = ('id', 'faculty', 'name')
    list_display_links = ('id', 'faculty', 'name')
    search_fields = ('faculty', 'name')


admin.site.register(Faculty, FacultyAdmin)

admin.site.register(Student, StudentAdmin)

admin.site.register(FacSpec, FacSpecAdmin)