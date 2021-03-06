# Generated by Django 3.1.1 on 2020-09-18 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuestResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Имя пользователя')),
                ('body', models.CharField(max_length=512, verbose_name='Тело отзыва')),
                ('img', models.ImageField(upload_to='responses', verbose_name='Иллюстрация отзыва')),
                ('active', models.BooleanField(db_index=True, default=True, verbose_name='Активен ли объект')),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
            ],
        ),
    ]
