# Generated by Django 4.0.6 on 2023-06-27 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twenty_four_seven', '0007_warecipient_projecttwentyfourseven_wa_recipient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projecttwentyfourseven',
            name='author_filter',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='projecttwentyfourseven',
            name='country_filter',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='projecttwentyfourseven',
            name='language_filter',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='projecttwentyfourseven',
            name='sentiment_filter',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='projecttwentyfourseven',
            name='source_filter',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
