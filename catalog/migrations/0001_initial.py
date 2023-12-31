# Generated by Django 4.2.4 on 2023-08-31 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('description', models.TextField(max_length=300, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, max_length=300, null=True, verbose_name='Описание')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение')),
                ('category', models.TextField(max_length=100, verbose_name='Катогория')),
                ('price', models.IntegerField(max_length=100, verbose_name='Цена за покупку')),
                ('creation_date', models.DateField(blank=True, max_length=500, null=True, verbose_name='Дата создания')),
                ('last_changes', models.DateField(blank=True, max_length=500, null=True, verbose_name='Дата последнего изменения')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
            },
        ),
    ]
