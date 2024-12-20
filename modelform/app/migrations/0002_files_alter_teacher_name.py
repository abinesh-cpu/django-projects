# Generated by Django 5.1.3 on 2024-12-20 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('description', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.TextField(),
        ),
    ]