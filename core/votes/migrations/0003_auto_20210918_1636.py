# Generated by Django 3.2.4 on 2021-09-18 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0002_alter_votesmodel_categorys'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='votesmodel',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='votesmodel',
            name='isclosed',
            field=models.BooleanField(default=False),
        ),
    ]
