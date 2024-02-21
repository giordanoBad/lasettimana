from django.contrib import admin
from .models import Gruppo, MembroGruppo
from django.db.models import Count  # Importa Count da django.db.models

class MembroGruppoInline(admin.TabularInline):
    model = MembroGruppo
    extra = 0

class GruppoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cognome', 'numero_telefono', 'data_arrivo', 'data_partenza', 'total_members']
    inlines = [MembroGruppoInline]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(total_members=Count('membrogruppo'))  # Usiamo Count direttamente
        return queryset

    def total_members(self, obj):
        return obj.total_members

    total_members.admin_order_field = 'total_members'
    total_members.short_description = 'Total Members'

admin.site.register(Gruppo, GruppoAdmin)
admin.site.register(MembroGruppo)