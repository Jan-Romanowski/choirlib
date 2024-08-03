from django.contrib import admin
from .models import Composition, CompositionFile

class CompositionFileInline(admin.TabularInline):
    model = CompositionFile
    extra = 1

@admin.register(Composition)
class CompositionAdmin(admin.ModelAdmin):
    inlines = [CompositionFileInline]

admin.site.register(CompositionFile)