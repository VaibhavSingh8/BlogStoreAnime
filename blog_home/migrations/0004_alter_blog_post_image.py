# Generated by Django 4.0.6 on 2022-07-08 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_home', '0003_alter_blog_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='image',
            field=models.ImageField(upload_to='blog_uploads/'),
        ),
    ]
