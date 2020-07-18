# Generated by Django 3.0.8 on 2020-07-13 22:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('critical', 'critical.'), ('debug', 'debug'), ('error', 'error'), ('warning', 'warning'), ('information', 'info')], max_length=20)),
                ('log', models.TextField(max_length=500)),
                ('date', models.DateField(auto_now_add=True)),
                ('archive', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
