from django.db.models.signals import post_delete,post_save,pre_save
from django.dispatch import receiver
from inventory.models import Itens,InventoryControl


def inventory_count():
    itens_count = Itens.objects.all().count()

    InventoryControl.objects.create(
      itens_count=itens_count,
    )
    
   

@receiver(post_save,sender=Itens)
def itens_post_save(sender,instance,**kwargs):
  inventory_count()


@receiver(post_delete,sender=Itens)
def itens_post_delete(sender,instance,**kwargs):
  inventory_count()