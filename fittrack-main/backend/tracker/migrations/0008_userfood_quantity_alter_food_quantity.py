# Generated by Django 5.0.6 on 2024-06-23 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_alter_userexercise_date_alter_userfood_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfood',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='food',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
