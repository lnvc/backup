# Generated by Django 2.0.6 on 2018-07-16 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_question_maker'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_maker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='polls.Question_Maker'),
        ),
    ]