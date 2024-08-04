# Generated by Django 5.0.6 on 2024-06-22 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_userexercise_calories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='category',
            field=models.CharField(choices=[('arms', 'Arms'), ('chest', 'Chest'), ('shoulders', 'Shoulders'), ('back', 'Back'), ('abs', 'Abs'), ('legs', 'Legs'), ('hips', 'Hips'), ('glutes', 'Glutes'), ('lower back', 'Lower Back')], max_length=50),
        ),
    ]
