from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20240118_1523'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('title',), 'permissions': [('special_status', '???')], 'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
    ]
