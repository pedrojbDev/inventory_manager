from django.db import models

class Maquina(models.Model):
  id = models.AutoField(primary_key=True)
  nome = models.CharField(max_length=200, null=True)
  
  def __str__(self):
    return self.nome

class Setor(models.Model):
  id = models.AutoField(primary_key=True)
  nome = models.CharField(max_length=200,null=True)
  def __str__(self):
    return self.nome

class Marca(models.Model):
  id = models.AutoField(primary_key=True)
  nome = models.CharField(max_length=200, null=True)
  def __str__(self):
    return self.nome

class Monitor(models.Model):
  id = models.AutoField(primary_key=True)
  nome = models.CharField(max_length=200, null=True)
  def __str__(self):
    return self.nome

class Propietario(models.Model):
  id = models.AutoField(primary_key=True)
  nome = models.CharField(max_length=200, null=True)
  def __str__(self):
    return self.nome


class Itens(models.Model):
  id = models.AutoField(primary_key=True)
  nome = models.CharField(max_length=50)
  setor = models.ForeignKey(Setor,on_delete=models.PROTECT,related_name='itens_maquina',null=True)
  maquina = models.ForeignKey(Maquina,on_delete=models.PROTECT,related_name='itens_setor',null=True)
  propietario = models.ForeignKey(Propietario,on_delete=models.PROTECT,related_name='itens_propietario',null=True)
  marca = models.ForeignKey(Marca,on_delete=models.PROTECT,related_name='itens_marca',null=True)
  patrimonio = models.CharField(max_length=50,blank=True,unique=True)
  serie = models.CharField(max_length=50,blank=True,unique=True)
  monitor =models.ForeignKey(Monitor,on_delete=models.PROTECT,related_name='itens_monitor',null=True)
  arquivo = models.FileField(upload_to='inventory/',blank=True,null=True)
  

  def __str__(self):
    return self.nome





class Meta:
    ordering = ['-created_at']

class InventoryControl(models.Model):
  itens_count = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)