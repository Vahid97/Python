# Generated by Django 3.2.4 on 2021-07-10 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attorneys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, verbose_name='Name')),
                ('title', models.CharField(max_length=127, verbose_name='Title')),
                ('image', models.ImageField(max_length=127, upload_to='attorneys', verbose_name='Image')),
                ('slug', models.SlugField(max_length=150, verbose_name='Slug')),
                ('short_description', models.CharField(max_length=127, verbose_name='Short descritioon')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Attorney',
                'verbose_name_plural': 'Attorneys',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127, verbose_name='Title')),
                ('image', models.CharField(max_length=127, verbose_name='Image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=127, verbose_name='Title')),
                ('email', models.EmailField(max_length=127, verbose_name='E-mail')),
                ('subject', models.CharField(max_length=127, verbose_name='Subject')),
                ('message', models.TextField(help_text='Send your messages', verbose_name='Message')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='Practice_areas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127, verbose_name='Title')),
                ('image', models.ImageField(max_length=127, upload_to='practice_area_images', verbose_name='Image')),
                ('slug', models.SlugField(max_length=150, verbose_name='Slug')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Practice_area',
                'verbose_name_plural': 'Practice_areas',
            },
        ),
        migrations.CreateModel(
            name='Case_study',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127, verbose_name='Title')),
                ('image', models.ImageField(upload_to='case_study_images', verbose_name='Image')),
                ('slug', models.SlugField(max_length=150, verbose_name='Slug')),
                ('description', models.TextField(verbose_name='Description')),
                ('order', models.PositiveIntegerField(default=1, verbose_name='Order')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_studies', to='pages.category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Case_study',
                'verbose_name_plural': 'Case_studies',
            },
        ),
    ]