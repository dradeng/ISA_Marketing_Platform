# Generated by Django 2.1 on 2019-03-07 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField(default='', max_length=100)),
                ('duration', models.IntegerField(default=0)),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('url', models.URLField(blank=True, null=True)),
                ('site_title', models.CharField(default='Google', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Authenticator',
            fields=[
                ('authenticator', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MarketUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.TextField(max_length=500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='marketplace.MarketUser')),
            ],
        ),
        migrations.AddField(
            model_name='buyer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='marketplace.MarketUser'),
        ),
        migrations.AddField(
            model_name='authenticator',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.MarketUser'),
        ),
        migrations.AddField(
            model_name='ad',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='marketplace.MarketUser'),
        ),
    ]