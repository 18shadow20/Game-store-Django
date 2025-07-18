# Generated by Django 5.2.1 on 2025-06-21 18:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameStore', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/game_gallery/')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_gallery', to='GameStore.game')),
            ],
        ),
    ]
