from django.contrib import admin
from .models import Pais, ValorRepresentativo


class ValorInline(admin.TabularInline):
    model = ValorRepresentativo
    extra = 1


@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display  = ('bandera_emoji', 'nombre', 'codigo_iso', 'continente', 'capital', 'poblacion_formato')
    list_filter   = ('continente',)
    search_fields = ('nombre', 'capital', 'idioma')
    inlines       = [ValorInline]

    def poblacion_formato(self, obj):
        return obj.poblacion_formato
    poblacion_formato.short_description = 'Población'


@admin.register(ValorRepresentativo)
class ValorAdmin(admin.ModelAdmin):
    list_display  = ('pais', 'categoria', 'titulo')
    list_filter   = ('categoria',)
    search_fields = ('titulo', 'pais__nombre')
