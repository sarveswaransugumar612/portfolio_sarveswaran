# Generated by Django 4.2.9 on 2024-02-21 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='resume_clas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_title', models.CharField(max_length=100)),
                ('resume_file', models.FileField(upload_to='resumefile/')),
            ],
        ),
    ]
