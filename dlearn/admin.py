from django.contrib import admin
from .models import LearnersPermit

class LearnersPermitAdmin(admin.ModelAdmin):
    readonly_fields = ['permit_id', 'db_id']

admin.site.register(LearnersPermit, LearnersPermitAdmin)
