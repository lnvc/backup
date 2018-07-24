# Generated by Django 2.0.6 on 2018-07-16 15:50

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_school'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attend_School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currently_attending', models.BooleanField()),
                ('student_awards', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=250), blank=True, null=True, size=None)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.School')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Student')),
            ],
        ),
    ]
