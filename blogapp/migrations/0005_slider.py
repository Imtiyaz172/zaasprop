# Generated by Django 2.0.3 on 2019-09-13 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_auto_20190913_1222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='slider/')),
                ('Status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Slider',
                'verbose_name_plural': 'Slider',
            },
        ),
    ]
