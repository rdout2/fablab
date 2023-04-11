# Generated by Django 4.2 on 2023-04-06 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=255, null=True, verbose_name='Slug')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
        ),
        migrations.CreateModel(
            name='Galery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
        ),
        migrations.CreateModel(
            name='MachineCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Nom')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=255, null=True, verbose_name='Slug')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Nom')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=255, null=True, verbose_name='Slug')),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=255, null=True, verbose_name='Slug')),
                ('image', models.ImageField(upload_to='media')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FABLAB.trainingcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('image', models.ImageField(upload_to='media')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=255, null=True, verbose_name='Slug')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FABLAB.machinecategory')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=255, null=True, verbose_name='Slug')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FABLAB.blogcategory')),
            ],
        ),
    ]
