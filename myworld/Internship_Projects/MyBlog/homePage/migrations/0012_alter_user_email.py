# Generated by Django 4.2.5 on 2023-09-20 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0011_alter_articles_body_alter_articles_conclusion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]