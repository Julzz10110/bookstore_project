from django.db import migrations, models
from django.utils.translation import ugettext_lazy as _


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name':'Category',
                'verbose_name_plural':'Categories',
                'ordering': ('name',),
            },
        ),
    ]
