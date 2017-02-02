from django.contrib import admin

from .models import Task

class TaskAdmin(admin.ModelAdmin):
    exclude = ('created_by','created_on','amended_by','amended_on')
    # form = TaskAdminForm
    # fields = ('dt',)

# 
# class TaskAdminForm(forms.ModelForm):
#     class Meta:
#         model = Task
#
#
admin.site.register(Task,TaskAdmin)
