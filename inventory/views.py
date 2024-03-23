from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from inventory.models import Itens, InventoryControl,Setor,Maquina,Monitor
from inventory.forms import InventoryForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



class InventoryListView(ListView):
    model = Itens
    template_name = 'inventory.html'
    context_object_name = 'inventory'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        quantidade_de_itens = Itens.objects.all().count()
        
        context['quantidade_de_itens'] = quantidade_de_itens

        quantidade_notebooks = Itens.objects.filter(maquina__nome='Notebook').count()
      
        context['quantidade_notebooks'] = quantidade_notebooks

        quantidade_pc = Itens.objects.filter(maquina__nome='PC').count()
      
        context['quantidade_pc'] = quantidade_pc

        quantidade_moni = Itens.objects.filter(monitor__nome='Sim').count()
      
        context['quantidade_moni'] = quantidade_moni


        return context
    


    def get_queryset(self):

        itens = super().get_queryset().order_by('setor')
        search = self.request.GET.get('search')
        if search:
          itens = itens.filter(nome__icontains=search)
        return itens
    
    

    

@method_decorator(login_required(login_url='login'), name='dispatch')
class NewIten(CreateView):
  form_class = InventoryForm
  model = Itens
  template_name = 'new_iten.html'
  def get_success_url(self):
        #ESSA LINHA ABAIXO SERVE DIRECIONAR PARA URL DETAIL_VIEW POR ISSO A FUNÇÃO REVERSE_LAZY
        return reverse_lazy('inventory')

class ItensDetailView(DetailView):
  model = Itens
  template_name = 'inventory_detail.html'

class ItensUpdateView(UpdateView):
    model = Itens
    template_name = 'inventory_update.html'
    form_class = InventoryForm
    

    def get_success_url(self):
          #ESSA LINHA ABAIXO SERVE DIRECIONAR PARA URL DETAIL_VIEW POR ISSO A FUNÇÃO REVERSE_LAZY
          return reverse_lazy('itens_detail', kwargs={'pk':self.object.pk})

class ItensDeleteView(DeleteView):
  model = Itens
  template_name = 'inventory_delete.html'
  success_url = '/inventory/'



