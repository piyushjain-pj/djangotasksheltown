# Generated by Django 3.1.2 on 2020-10-31 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='UserRegistered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('dob', models.DateField()),
                ('phone_number', models.CharField(max_length=13)),
                ('address_1', models.CharField(max_length=200)),
                ('address_2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=50)),
                ('is_sheltown_verified', models.CharField(max_length=50)),
                ('user_image', models.ImageField(upload_to='images/')),
                ('user_Type', models.CharField(choices=[('us', 'USER'), ('po', 'Property Owner')], max_length=2)),
                ('identity_proof', models.ImageField(upload_to='images/')),
            ],
            options={
                'db_table': 'Registered_Users',
            },
        ),
        migrations.CreateModel(
            name='PropertyOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whatsapp_number', models.CharField(max_length=50)),
                ('Property_owner_designation', models.CharField(choices=[('ow', 'Owner'), ('ma', 'Manager')], max_length=2)),
                ('cancelled_cheque', models.ImageField(upload_to='images/')),
                ('bank_account_number', models.CharField(max_length=50)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stafflogin.userregistered', verbose_name='phone_number')),
            ],
        ),
    ]
