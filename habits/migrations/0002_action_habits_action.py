# Generated by Django 4.2.7 on 2023-11-30 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Разминка', max_length=200, unique=True, verbose_name='действие')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание привычки')),
            ],
            options={
                'verbose_name': 'Действие',
                'verbose_name_plural': 'Действия',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='habits',
            name='action',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='habits.action', verbose_name='действие'),
        ),
    ]