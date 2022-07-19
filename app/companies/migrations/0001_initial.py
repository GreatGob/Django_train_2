# Generated by Django 4.0 on 2022-07-18 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date_published')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date_published')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='companies.company')),
            ],
        ),
        migrations.CreateModel(
            name='More',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('pub_date', models.DateTimeField(verbose_name='date_published')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='more', to='companies.employee')),
            ],
        ),
    ]
