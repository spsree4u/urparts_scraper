# Generated by Django 4.1.3 on 2022-11-23 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PartsDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=256)),
                ('category_name', models.CharField(max_length=256)),
                ('model_name', models.CharField(max_length=256)),
                ('part_name', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'parts_details',
            },
        ),
    ]
