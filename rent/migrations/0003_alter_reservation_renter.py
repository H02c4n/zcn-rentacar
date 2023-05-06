# Generated by Django 4.1.5 on 2023-01-29 14:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rent', '0002_alter_reservation_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='renter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]