# Generated by Django 3.0.4 on 2021-02-11 03:37

import application.storage_backends
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_merge_20210129_0403'),
    ]

    operations = [
        migrations.RenameField(
            model_name='simulationhistory',
            old_name='output_dvh_path',
            new_name='output_dvh_csv_path',
        ),
        migrations.AddField(
            model_name='simulationhistory',
            name='output_dvh_fig_path',
            field=models.FileField(default=django.utils.timezone.now, storage=application.storage_backends.PublicMediaStorage(), upload_to=''),
            preserve_default=False,
        ),
    ]