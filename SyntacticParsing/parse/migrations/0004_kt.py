# Generated by Django 3.1.4 on 2020-12-20 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parse', '0003_pr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rules', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Kt',
                'verbose_name_plural': 'Kt',
            },
        ),
    ]
