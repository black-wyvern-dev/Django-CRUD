# Generated by Django 2.2.20 on 2021-05-10 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.TextField(blank=True)),
                ('category', models.IntegerField(default=0)),
                ('location', models.TextField(blank=True)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
