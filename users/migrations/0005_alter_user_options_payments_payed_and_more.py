# Generated by Django 5.0.2 on 2024-02-26 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['id'], 'permissions': [('can_view_password', 'может просматривать пароль'), ('can_view_last_name', 'может просматривать фамилию')], 'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AddField(
            model_name='payments',
            name='payed',
            field=models.BooleanField(default=False, verbose_name='Оплачено'),
        ),
        migrations.AddField(
            model_name='payments',
            name='session_id',
            field=models.CharField(default='', max_length=255, verbose_name='ID сессии'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payments',
            name='url',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='Ссылка на оплату'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Сумма платежа'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('cash', 'наличные'), ('card', 'банковская карта'), ('bancontact', 'Bancontact'), ('eps', 'эквайринг'), ('giropay', 'giropay'), ('ideal', 'ideal'), ('p24', 'p24'), ('sepa_debit', 'sepa debit')], max_length=30, null=True, verbose_name='Способ оплаты'),
        ),
    ]