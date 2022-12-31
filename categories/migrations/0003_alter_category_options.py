from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_auto_20210906_1548'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]
