# Generated by Django 3.2.9 on 2021-11-12 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cast', '0001_initial'),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
                ('poster_image', models.ImageField(upload_to='movie_poster')),
                ('casts', models.ManyToManyField(related_name='movies', to='cast.Cast')),
                ('categories', models.ManyToManyField(related_name='movies', to='category.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]