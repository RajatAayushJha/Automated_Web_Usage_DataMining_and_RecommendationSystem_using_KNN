from django.contrib import admin
from .models import Movie,Myrating
from import_export.admin import ImportExportModelAdmin

admin.site.register(Movie)
admin.site.register(Myrating)
class ViewAdmin(ImportExportModelAdmin):
	pass

# Register your models here.
