# Generated by Django 5.0.3 on 2024-03-16 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_itens_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itens',
            name='patrimonio',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='itens',
            name='serie',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
