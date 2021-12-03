# Generated by Django 3.2.9 on 2021-12-03 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='institution',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='donation',
            name='zip_code',
            field=models.TextField(max_length=6),
        ),
        migrations.AlterField(
            model_name='institution',
            name='type',
            field=models.IntegerField(choices=[(0, 'Fundacja'), (1, 'Organizacja pozarządowa'), (2, 'Zbiórka lokalna')], default=0),
        ),
    ]