# Generated by Django 2.0.3 on 2019-09-13 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='company_footer_link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('facebook', models.TextField(max_length=254)),
                ('tweeter', models.TextField(max_length=254)),
                ('google_plas', models.TextField(max_length=254)),
                ('youtube', models.TextField(max_length=254)),
            ],
            options={
                'verbose_name': 'company_footer_link',
                'verbose_name_plural': 'company_footer_link',
            },
        ),
    ]
