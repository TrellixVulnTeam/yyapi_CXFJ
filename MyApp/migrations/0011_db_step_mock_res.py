# Generated by Django 3.1.2 on 2020-11-30 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0010_auto_20201110_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='db_step',
            name='mock_res',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
