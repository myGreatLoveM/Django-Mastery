# Generated by Django 5.1.3 on 2024-11-19 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("appointments", "0003_practicearea_pa_name_unq"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="practicearea",
            table="appointments__practice_areas",
        ),
    ]
