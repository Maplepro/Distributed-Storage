# Generated by Django 2.1.7 on 2019-03-10 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_auto_20190310_0909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermetadata',
            name='username',
        ),
        migrations.AddField(
            model_name='usermetadata',
            name='email',
            field=models.EmailField(default='user@email.com', max_length=100, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
