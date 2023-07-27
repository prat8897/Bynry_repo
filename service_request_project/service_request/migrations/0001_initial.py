# Generated by Django 4.2.3 on 2023-07-25 16:53

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
            name='ServiceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Type 1', 'Type 1'), ('Type 2', 'Type 2')], max_length=50)),
                ('details', models.TextField()),
                ('attached_files', models.FileField(blank=True, null=True, upload_to='service_request_attachments/')),
                ('submitted_datetime', models.DateTimeField(auto_now_add=True)),
                ('resolved_datetime', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('done', 'Done')], default='pending', max_length=10)),
                ('user', models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RequestTracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('service_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service_request.servicerequest')),
            ],
        ),
    ]
