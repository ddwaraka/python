from django.contrib import admin

# Register your models here.
from .models import Task


def change_status(modeladmin, request, queryset):
    queryset.update(task_status='Complete')

change_status.short_description = "Mark selected tasks as complete"


class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'task_status', 'task_priority', 'target_date')
    list_filter = ('task_status', 'task_priority', 'target_date')
    search_fields = ['task_name', 'task_status', 'task_priority']
    # list_editable = ['task_status']
    actions = [change_status]


admin.site.register(Task, TaskAdmin)
