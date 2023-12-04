# Generated by Django 4.1.13 on 2023-12-02 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='eksisozluk_entries',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titleId', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250)),
                ('author_profile_link', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=250)),
                ('entryId', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('entry_date', models.DateTimeField()),
                ('entry_date_from_scape', models.DateTimeField()),
            ],
        ),
    ]
