# Generated by Django 2.0.6 on 2018-07-16 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_question_question_maker'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image_equation',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/'),
        ),
        migrations.AddField(
            model_name='question',
            name='image_question',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/'),
        ),
        migrations.AddField(
            model_name='question',
            name='image_solution',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/'),
        ),
    ]