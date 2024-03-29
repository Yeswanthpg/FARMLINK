# Generated by Django 5.0.1 on 2024-02-11 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Farmer', '0004_alter_profile_profileimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='{% static img\\default.jpg %}', upload_to='post_images'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='{% static img\\default.jpg %}', upload_to='profile_images'),
        ),
    ]
