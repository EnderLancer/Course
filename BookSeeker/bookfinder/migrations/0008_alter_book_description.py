# Generated by Django 3.2.6 on 2021-08-26 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookfinder', '0007_alter_book_publication_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
