from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import *

# Register your models here.
@admin.register(Companies)

class csa_star_registy(ImportExportModelAdmin):

    class Meta:
        model = Companies

admin.site.register(caiq_company_map)