# Generated by Django 4.0.6 on 2023-06-15 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twenty_four_seven', '0005_alter_item_header_alter_item_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='linked_items',
            field=models.ManyToManyField(blank=True, related_name='attached_items', to='twenty_four_seven.item'),
        ),
    ]
