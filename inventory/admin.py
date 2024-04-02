from django.contrib import admin
from inventory.models import Itens,Maquina,Marca,Monitor,Setor

class ItensAdmin(admin.ModelAdmin):
  list_display= ('nome','setor','maquina','marca','patrimonio','serie','monitor','arquivo')
  search_fields=('nome','setor','patrimonio')


class SetorAdmin(admin.ModelAdmin):
  list_display= ('nome',)
  search_fields=('nome',)

class MaquinaAdmin(admin.ModelAdmin):
  list_display= ('nome',)
  search_fields=('nome',)

class MarcaAdmin(admin.ModelAdmin):
  list_display= ('nome',)
  search_fields=('nome',)

class MonitorAdmin(admin.ModelAdmin):
  list_display= ('nome',)
  search_fields=('nome',)

admin.site.register(Itens,ItensAdmin)
admin.site.register(Setor,SetorAdmin)
admin.site.register(Maquina,MaquinaAdmin)
admin.site.register(Marca,MarcaAdmin)
admin.site.register(Monitor,MonitorAdmin)

