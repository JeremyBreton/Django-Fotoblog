# Generated by Django 5.1.1 on 2024-09-17 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_remove_blog_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="content",
            field=models.CharField(max_length=5000, verbose_name="contenu"),
        ),
        migrations.AlterField(
            model_name="blog",
            name="title",
            field=models.CharField(max_length=128, verbose_name="titre"),
        ),
        migrations.AlterField(
            model_name="photo",
            name="caption",
            field=models.CharField(blank=True, max_length=128, verbose_name="légende"),
        ),
        migrations.AlterField(
            model_name="photo",
            name="image",
            field=models.ImageField(upload_to="", verbose_name="image"),
        ),
    ]
