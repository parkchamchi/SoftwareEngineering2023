# Generated by Django 4.2.1 on 2023-06-02 09:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lists', '0004_frontendoptions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frontendoptions',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='frontend_options', to=settings.AUTH_USER_MODEL),
        ),
    ]
