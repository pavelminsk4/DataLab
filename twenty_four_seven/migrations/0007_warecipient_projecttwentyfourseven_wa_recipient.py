# Generated by Django 4.0.6 on 2023-06-20 13:10

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('twenty_four_seven', '0006_item_linked_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='WARecipient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='projecttwentyfourseven',
            name='wa_recipient',
            field=models.ManyToManyField(blank=True, to='twenty_four_seven.warecipient'),
        ),
    ]