# Generated by Django 3.2.4 on 2021-09-16 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votesmodel',
            name='categorys',
            field=models.ManyToManyField(related_name='category', to='votes.category'),
        ),
    ]