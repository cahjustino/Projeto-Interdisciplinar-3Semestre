# Generated by Django 4.1.12 on 2023-11-18 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='apoioModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=14)),
                ('rg', models.CharField(max_length=10)),
                ('orgao', models.CharField(max_length=50)),
                ('nome', models.CharField(max_length=255)),
                ('idade', models.IntegerField()),
                ('endereco', models.CharField(max_length=255)),
                ('numero', models.IntegerField()),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=2)),
                ('telefone', models.CharField(max_length=15)),
                ('celular', models.CharField(max_length=15)),
                ('renda', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pessoas', models.IntegerField()),
                ('sobre', models.TextField()),
                ('encontrou', models.CharField(max_length=20)),
                ('declaracao', models.BooleanField()),
                ('modificado_em', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
            ],
        ),
        migrations.CreateModel(
            name='cnpjModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('senha', models.CharField(max_length=128)),
                ('cnpj', models.CharField(max_length=14)),
                ('empresa', models.CharField(max_length=255)),
                ('responsavel', models.CharField(max_length=255)),
                ('cargo', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=255)),
                ('numero', models.IntegerField()),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=2)),
                ('telefone', models.CharField(max_length=15)),
                ('celular', models.CharField(max_length=15)),
                ('sobre', models.TextField()),
                ('encontrou', models.CharField(max_length=20)),
                ('declaracao', models.BooleanField()),
                ('modificado_em', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
            ],
        ),
        migrations.CreateModel(
            name='cpfModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('senha', models.CharField(max_length=128)),
                ('cpf', models.CharField(max_length=14)),
                ('rg', models.CharField(max_length=10)),
                ('orgao', models.CharField(max_length=50)),
                ('nome', models.CharField(max_length=255)),
                ('idade', models.IntegerField()),
                ('endereco', models.CharField(max_length=255)),
                ('numero', models.IntegerField()),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=2)),
                ('telefone', models.CharField(max_length=15)),
                ('celular', models.CharField(max_length=15)),
                ('sobre', models.TextField()),
                ('encontrou', models.CharField(max_length=20)),
                ('declaracao', models.BooleanField()),
                ('modificado_em', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
            ],
        ),
    ]
