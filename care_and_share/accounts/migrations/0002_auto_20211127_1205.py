# Generated by Django 3.2.9 on 2021-11-27 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=64, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=64, verbose_name='Imię'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password_1',
            field=models.CharField(max_length=64, verbose_name='Hasło'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password_2',
            field=models.CharField(max_length=64, verbose_name='Powtórz hasło'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='surname',
            field=models.CharField(max_length=64, verbose_name='Nazwisko'),
        ),
    ]
