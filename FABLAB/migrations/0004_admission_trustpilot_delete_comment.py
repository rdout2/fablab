# Generated by Django 4.2 on 2023-04-08 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FABLAB', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Nom')),
                ('last_name', models.CharField(max_length=255, verbose_name='Prenom')),
                ('phone', models.CharField(max_length=255, verbose_name='Numero')),
                ('email', models.EmailField(max_length=255)),
                ('cv', models.ImageField(upload_to='media')),
                ('Motivation', models.TextField()),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('Training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FABLAB.training')),
            ],
        ),
        migrations.CreateModel(
            name='Trustpilot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Nom')),
                ('email', models.EmailField(max_length=255)),
                ('comment', models.TextField()),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
