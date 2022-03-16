# Generated by Django 4.0.2 on 2022-03-15 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_project_task_remove_channelmembers_channel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sandwich',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sauce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SauceQuantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra_sauce', models.BooleanField(default=False)),
                ('sandwich', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.sandwich')),
                ('sauce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.sauce')),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='assignee',
        ),
        migrations.RemoveField(
            model_name='task',
            name='project',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.AddField(
            model_name='sandwich',
            name='sauces',
            field=models.ManyToManyField(through='api.SauceQuantity', to='api.Sauce'),
        ),
    ]