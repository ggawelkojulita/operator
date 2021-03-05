# Generated by Django 3.1.4 on 2021-03-03 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomepageSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('html_text', models.TextField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='images/logos')),
                ('show_button', models.BooleanField(default=False)),
                ('button_text', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]