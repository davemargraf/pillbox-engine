# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-28 21:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'Enabled?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('spl_id', models.CharField(max_length=100, unique=True, verbose_name=b'Unii Code')),
                ('code_system', models.CharField(blank=True, max_length=200, null=True, verbose_name=b'Code System')),
                ('name', models.CharField(max_length=300, verbose_name=b'Name')),
                ('class_code', models.CharField(blank=True, max_length=100, null=True, verbose_name=b'Class Code')),
            ],
            options={
                'verbose_name': 'OSDF Ingredient',
            },
        ),
        migrations.CreateModel(
            name='Pill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'Enabled?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ssp', models.CharField(max_length=200, unique=True, verbose_name=b'Pillbox Unique ID')),
                ('dosage_form', models.CharField(max_length=20, verbose_name=b'Dosage Form')),
                ('ndc', models.CharField(blank=True, max_length=100, null=True, verbose_name=b'NDC9')),
                ('ndc9', models.CharField(blank=True, max_length=100, null=True, verbose_name=b'NDC9')),
                ('product_code', models.CharField(blank=True, max_length=60, null=True, verbose_name=b'Product Code')),
                ('produce_code', models.CharField(blank=True, max_length=60, null=True, verbose_name=b'Produce Code')),
                ('equal_product_code', models.CharField(blank=True, max_length=30, null=True, verbose_name=b'Equal Product Code')),
                ('approval_code', models.CharField(blank=True, max_length=100, null=True, verbose_name=b'approval_code')),
                ('medicine_name', models.CharField(max_length=300, verbose_name=b'Medicine Name')),
                ('part_num', models.IntegerField(default=0, verbose_name=b'Part Number')),
                ('part_medicine_name', models.CharField(blank=True, max_length=200, null=True, verbose_name=b'Part Medicine Name')),
                ('rxtty', models.TextField(blank=True, null=True, verbose_name=b'rxtty')),
                ('rxstring', models.TextField(blank=True, null=True, verbose_name=b'rxttystring')),
                ('rxcui', models.CharField(blank=True, max_length=100, null=True, verbose_name=b'rxcui')),
                ('dea_schedule_code', models.CharField(blank=True, max_length=100, null=True, verbose_name=b'DEA_SCHEDULE_CODE')),
                ('dea_schedule_name', models.CharField(blank=True, max_length=100, null=True, verbose_name=b'DEA_SCHEDULE_NAME')),
                ('marketing_act_code', models.CharField(blank=True, max_length=100, null=True, verbose_name=b'MARKETING_ACT_CODE')),
                ('splcolor', models.CharField(blank=True, max_length=100, null=True, verbose_name=b'SPL Color Code')),
                ('splcolor_text', models.CharField(blank=True, max_length=100, null=True, verbose_name=b'SPL Color Display Name')),
                ('splsize', models.CharField(blank=True, max_length=100, null=True, verbose_name=b'SPL Size')),
                ('splshape', models.CharField(blank=True, max_length=100, null=True, verbose_name=b'SPL Shape Code')),
                ('splshape_text', models.CharField(blank=True, max_length=100, null=True, verbose_name=b'SPL Shape Display Name')),
                ('splimprint', models.CharField(blank=True, max_length=100, null=True, verbose_name=b'SPL Imprint')),
                ('splimage', models.FileField(blank=True, null=True, upload_to=b'spl', verbose_name=b'SPL Image')),
                ('splscore', models.CharField(blank=True, max_length=100, null=True, verbose_name=b'SPL Score')),
                ('spl_strength', models.TextField(blank=True, null=True, verbose_name=b'SPL_STRENGTH')),
                ('spl_ingredients', models.TextField(blank=True, null=True, verbose_name=b'SPL_INGREDIENTS')),
                ('spl_inactive_ing', models.TextField(blank=True, null=True, verbose_name=b'SPL_INACTIVE_ING')),
            ],
            options={
                'verbose_name': 'SPL OSDF Pill',
                'verbose_name_plural': 'SPL OSDF Pills',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'Enabled?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('setid', models.CharField(max_length=200, unique=True, verbose_name=b'setid')),
                ('id_root', models.CharField(max_length=200, verbose_name=b'id root')),
                ('title', models.TextField(blank=True, null=True, verbose_name=b'Title')),
                ('effective_time', models.CharField(max_length=100, verbose_name=b'Effective Time')),
                ('version_number', models.IntegerField(verbose_name=b'Version Number')),
                ('code', models.CharField(max_length=250, verbose_name=b'Document Type (Code)')),
                ('filename', models.CharField(max_length=300, verbose_name=b'File Name')),
                ('source', models.CharField(max_length=250, verbose_name=b'Source')),
                ('author', models.CharField(blank=True, max_length=300, null=True, verbose_name=b'Author (Laberer)')),
                ('author_legal', models.CharField(blank=True, max_length=300, null=True, verbose_name=b'Legal Author')),
                ('is_osdf', models.BooleanField(default=False, verbose_name=b'Is In Oral Solid Dosage Form?')),
                ('discontinued', models.BooleanField(default=False, verbose_name=b'Is Discontinued from SPL?')),
            ],
            options={
                'verbose_name': 'SPL Product',
                'verbose_name_plural': 'SPL Products',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'Enabled?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'Title')),
                ('host', models.CharField(help_text=b'FTP host to download the files from', max_length=200, verbose_name=b'FTP Host')),
                ('path', models.CharField(help_text=b'Path where the files are located on the ftp server', max_length=200, verbose_name=b'PATH')),
                ('files', jsonfield.fields.JSONField(help_text=b'Enter in form python list', verbose_name=b'File Names')),
                ('last_downloaded', models.DateTimeField(blank=True, null=True, verbose_name=b'Last Downloaded and Unzipped')),
                ('zip_size', models.FloatField(blank=True, null=True, verbose_name=b'Total zip folder size (bytes)')),
                ('unzip_size', models.FloatField(blank=True, null=True, verbose_name=b'Total unzip folder size (bytes)')),
                ('xml_count', models.IntegerField(blank=True, null=True, verbose_name=b'Total xml files')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name=b'Task Name')),
                ('task_id', models.CharField(blank=True, max_length=250, null=True, unique=True, verbose_name=b'Task ID')),
                ('time_started', models.DateTimeField(auto_now_add=True)),
                ('time_ended', models.DateTimeField(blank=True, null=True, verbose_name=b'Time Ended')),
                ('duration', models.FloatField(default=0, verbose_name=b'Duration')),
                ('status', models.CharField(blank=True, max_length=200, null=True, verbose_name=b'Status')),
                ('meta', jsonfield.fields.JSONField(default={}, verbose_name=b'Meta')),
                ('pid', models.CharField(blank=True, max_length=100, null=True, verbose_name=b'PID')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'Task is active (running)?')),
                ('download_type', models.CharField(blank=True, max_length=200, null=True, verbose_name=b'Download source name')),
                ('traceback', models.TextField(blank=True, null=True, verbose_name=b'Traceback')),
            ],
        ),
        migrations.AddField(
            model_name='pill',
            name='setid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spl.Product'),
        ),
    ]