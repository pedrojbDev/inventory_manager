# Generated by Django 5.0.3 on 2024-03-14 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_setor_remove_maquina_name_remove_marca_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itens',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
