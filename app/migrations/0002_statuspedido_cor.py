# Generated by Django 3.1.7 on 2022-04-25 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='statuspedido',
            name='cor',
            field=models.CharField(blank=True, choices=[('default', 'Padrao'), ('info', 'Azul Claro'), ('primary', 'Azul Escuro'), ('success', 'Verde'), ('danger', 'Vermelho'), ('warning', 'Amarelo')], max_length=255, null=True),
        ),
    ]