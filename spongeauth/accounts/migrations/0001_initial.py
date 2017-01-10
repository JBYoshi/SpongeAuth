# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-10 00:05
from __future__ import unicode_literals

import accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('email_verified', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('mc_username', models.CharField(blank=True, max_length=255, null=True, verbose_name='Minecraft Username')),
                ('irc_nick', models.CharField(blank=True, max_length=255, null=True, verbose_name='IRC Nick')),
                ('gh_username', models.CharField(blank=True, max_length=255, null=True, verbose_name='GitHub Username')),
                ('joined_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('twofa_enabled', models.BooleanField(default=False, verbose_name='2FA Enabled')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('image_file', models.ImageField(blank=True, null=True, upload_to=accounts.models._avatar_upload_path)),
                ('remote_url', models.URLField(blank=True, null=True)),
                ('source', models.CharField(choices=[('upload', 'Uploaded avatar'), ('url', 'Avatar at URL')], default='upload', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExternalAuthenticator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(choices=[('google', 'Google')], default='google', max_length=20)),
                ('external_id', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='current_avatar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='accounts.Avatar'),
        ),
    ]
