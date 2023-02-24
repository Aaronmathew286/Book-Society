# Generated by Django 4.1.5 on 2023-02-22 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pic')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pic')),
                ('desc', models.TextField()),
                ('qty', models.IntegerField()),
                ('discount', models.IntegerField(default=0)),
                ('price', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('pro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='home.category')),
            ],
        ),
        migrations.DeleteModel(
            name='MainProducts',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
