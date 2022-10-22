# Generated by Django 4.1.2 on 2022-10-21 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_skills_jobpost_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='type',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part TIme')], default='Full Time', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='description',
            field=models.TextField(),
        ),
    ]
