# Generated by Django 3.2.6 on 2021-08-26 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookfinder', '0005_book_picture_src'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.AddField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(null=True, related_name='books', to='bookfinder.Genre'),
        ),
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='books', to='bookfinder.Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]