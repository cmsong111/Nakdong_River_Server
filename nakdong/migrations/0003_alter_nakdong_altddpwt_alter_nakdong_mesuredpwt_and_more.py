# Generated by Django 4.1.1 on 2022-09-10 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nakdong', '0002_alter_comment_id_alter_nakdong_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nakdong',
            name='altdDpwt',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='nakdong',
            name='mesureDpwt',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='nakdong',
            name='saln',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='nakdong',
            name='wtep',
            field=models.FloatField(),
        ),
    ]
