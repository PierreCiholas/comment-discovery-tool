# Generated by Django 2.0.1 on 2018-01-31 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordcloud', '0010_comment_source_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='source_id',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
