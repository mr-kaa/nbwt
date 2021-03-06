# Generated by Django 3.1.3 on 2020-11-08 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filesystem', '0003_auto_20201108_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='identical_file',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='clones', to='filesystem.file', verbose_name='Previously created identical file'),
        ),
    ]
