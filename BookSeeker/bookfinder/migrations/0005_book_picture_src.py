# Generated by Django 3.2.6 on 2021-08-26 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookfinder', '0004_reviewcomment_answer_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='picture_src',
            field=models.URLField(null=True),
        ),
    ]
