# Generated by Django 4.2.6 on 2023-10-06 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='followers',
        ),
        migrations.AddField(
            model_name='books',
            name='author',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='books.author'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='books',
            name='genre',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='books.genre'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='books',
            name='publisher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='books.publisher'),
            preserve_default=False,
        ),
    ]
