# Generated by Django 4.2.5 on 2023-09-13 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0005_alter_articles_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]