# Generated by Django 3.2.4 on 2021-06-14 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BranchModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_ru', models.CharField(max_length=255)),
                ('region_kz', models.CharField(max_length=255)),
                ('city_ru', models.CharField(max_length=255)),
                ('city_kz', models.CharField(max_length=255)),
                ('area_ru', models.CharField(max_length=255)),
                ('area_kz', models.CharField(max_length=255)),
                ('address_ru', models.CharField(max_length=255)),
                ('address_kz', models.CharField(max_length=255)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('newbranch', models.BooleanField()),
                ('alias', models.CharField(max_length=100)),
                ('londonfix3', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=30)),
                ('Whatsapp', models.CharField(max_length=30)),
                ('Vyhodnye', models.CharField(max_length=255)),
                ('RezhimRabotyLeto', models.CharField(max_length=255)),
                ('RezhimRabotyZima', models.CharField(max_length=255)),
                ('Uslugi', models.CharField(max_length=255)),
                ('VIP', models.BooleanField()),
                ('BranchNumber', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'branch',
            },
        ),
    ]
