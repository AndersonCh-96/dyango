# Generated by Django 4.1.4 on 2022-12-30 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0004_remove_employee_gener'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='types',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='erp.type'),
            preserve_default=False,
        ),
    ]
