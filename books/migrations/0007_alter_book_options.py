# Generated by Django 5.0.1 on 2024-02-26 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_merge_0003_auto_20240118_1523_0005_alter_book_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('title',), 'permissions': [('special_status', '???')], 'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
    ]
