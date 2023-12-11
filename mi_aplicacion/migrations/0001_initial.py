# Generated by Django 4.2 on 2023-12-11 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to='productos/')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
