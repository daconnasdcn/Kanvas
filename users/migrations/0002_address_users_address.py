# Generated by Django 4.0.4 on 2022-05-26 16:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('zip_code', models.CharField(max_length=255, unique=True)),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Users', to='users.address'),
        ),
    ]
