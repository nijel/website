# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-01 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("payments", "0006_auto_20181101_0900")]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="tax",
            field=models.CharField(
                blank=True,
                help_text="Please fill in your tax registration if it should appear on the invoice.",
                max_length=200,
                verbose_name="Tax registration",
            ),
        )
    ]
