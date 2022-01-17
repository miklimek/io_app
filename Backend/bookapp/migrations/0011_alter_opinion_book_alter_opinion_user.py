# Generated by Django 4.0 on 2022-01-04 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('bookapp', '0010_remove_genre_slug_remove_genre_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opinion',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bookapp.book'),
        ),
        migrations.AlterField(
            model_name='opinion',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
