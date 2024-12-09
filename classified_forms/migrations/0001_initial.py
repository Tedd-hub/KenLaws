# Generated by Django 5.0.7 on 2024-11-09 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=20)),
                ('home_address', models.TextField()),
                ('id_card_front', models.FileField(upload_to='id_cards/')),
                ('id_card_back', models.FileField(upload_to='id_cards/')),
                ('ssn_number', models.CharField(max_length=11)),
                ('maximum_salary_monthly', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
