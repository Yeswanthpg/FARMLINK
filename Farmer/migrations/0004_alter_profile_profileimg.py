# Generated by Django 5.0.1 on 2024-02-11 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Farmer', '0003_followers_likepost_rename_content_post_caption_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='\\static\\img\\default.jpg', upload_to='profile_images'),
        ),
    ]