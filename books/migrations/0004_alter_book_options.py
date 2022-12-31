from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20210906_1548'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('title',), 'permissions': [('special_status', 'Can read all books')], 'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
    ]
