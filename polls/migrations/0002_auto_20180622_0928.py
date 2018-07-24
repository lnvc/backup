# Generated by Django 2.0.6 on 2018-06-22 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='choice',
            options={'verbose_name': 'Choice', 'verbose_name_plural': 'Choices'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Question', 'verbose_name_plural': 'Questions'},
        ),
        migrations.AddField(
            model_name='question',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]