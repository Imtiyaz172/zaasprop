# Generated by Django 2.0.3 on 2019-09-20 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0018_remove_properte_image2'),
    ]

    operations = [
        migrations.AddField(
            model_name='properte',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='property/'),
        ),
    ]