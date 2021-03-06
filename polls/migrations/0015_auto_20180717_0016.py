# Generated by Django 2.0.6 on 2018-07-16 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_parent_parent_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_current_member', models.BooleanField()),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=1000)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='student_team',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Team'),
        ),
    ]
