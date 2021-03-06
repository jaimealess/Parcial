# Generated by Django 3.2.9 on 2021-11-03 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=100)),
                ('pedido', models.TextField()),
                ('total', models.TextField()),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedidos', to='pedidos.venta')),
            ],
        ),
    ]
