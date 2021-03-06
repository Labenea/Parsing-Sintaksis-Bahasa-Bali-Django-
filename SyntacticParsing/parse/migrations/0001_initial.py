# Generated by Django 3.1.4 on 2020-12-17 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rules', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rules', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Gt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rules', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='K',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rules', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rules', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='O',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rules', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='P',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rules', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rules', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rules', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rules', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='S',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rules', models.CharField(max_length=255)),
            ],
        ),
    ]
