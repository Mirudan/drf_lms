# Generated by Django 5.0.2 on 2024-02-18 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_payments'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('can_view_password', 'может просматривать пароль'), ('can_view_last_name', 'может просматривать фамилию')], 'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
