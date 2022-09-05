# Generated by Django 4.1 on 2022-09-01 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("task", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="subtask",
            name="task",
        ),
        migrations.AddField(
            model_name="task",
            name="subtask",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="task.subtask",
            ),
        ),
    ]