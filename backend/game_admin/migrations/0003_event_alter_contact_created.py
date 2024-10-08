# Generated by Django 5.1.1 on 2024-09-25 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_admin', '0002_alter_category_options_alter_game_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
                ('description', models.TextField()),
                ('location', models.CharField(blank=True, max_length=155, null=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('is_happend', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
