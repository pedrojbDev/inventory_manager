# Generated by Django 5.0.3 on 2024-03-16 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_itens_patrimonio_alter_itens_serie'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itens_count', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
