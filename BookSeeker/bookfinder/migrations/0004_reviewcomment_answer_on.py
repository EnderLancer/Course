# Generated by Django 3.2.6 on 2021-08-24 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookfinder', '0003_alter_bookreview_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewcomment',
            name='answer_on',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bookfinder.reviewcomment'),
        ),
    ]
