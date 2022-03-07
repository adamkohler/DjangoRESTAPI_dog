# Generated by Django 4.0.2 on 2022-03-06 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0004_remove_breed_a friendly value between 1-5_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breed',
            name='size',
            field=models.CharField(choices=[('tiny', 'Tiny'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], default='small', max_length=6),
        ),
    ]
