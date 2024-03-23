from typing import Any
from django import forms
from inventory.models import Itens

class InventoryForm(forms.ModelForm):
  class Meta:
    model = Itens
    fields = '__all__'
    