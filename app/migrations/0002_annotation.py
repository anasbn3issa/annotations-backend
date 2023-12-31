# Generated by Django 4.2.7 on 2023-11-26 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.TextField()),
                ('start_position', models.IntegerField()),
                ('end_position', models.IntegerField()),
                ('annotated_text', models.CharField(max_length=255)),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.label')),
            ],
        ),
    ]
