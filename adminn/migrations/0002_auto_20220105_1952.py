# Generated by Django 3.2.6 on 2022-01-05 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto_msg',
            name='admin_block',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='auto_msg',
            name='admin_unblock',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='auto_msg',
            name='breakup',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='auto_msg',
            name='matching',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='auto_msg',
            name='user_block',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='auto_msg',
            name='user_delete',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='auto_msg',
            name='welcome',
            field=models.TextField(null=True),
        ),
    ]
