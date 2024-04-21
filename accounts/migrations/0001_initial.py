import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='Пароль')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='Дата/время последней активности')),
                ('is_superuser', models.BooleanField(default=False, help_text='Означает, что у этого пользователя есть все разрешения без их явного назначения.', verbose_name='Статус суперпользователя')),
                ('username', models.CharField(error_messages={'unique': 'Пользователь с таким именем уже существует.'}, help_text='Доступно 150 символов и менее. Разрешены только буквы, цифры и @/./+/-/_.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='Имя пользователя')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='Фамилия')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='Имя')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='E-mail')),
                ('is_staff', models.BooleanField(default=False, help_text='Определяет, может ли пользователь войти на этот сайт администрирования.', verbose_name='Статус персонала')),
                ('is_active', models.BooleanField(default=True, help_text='Определяет, следует ли считать этого пользователя активным.', verbose_name='Активен')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='Группы, к которым принадлежит этот пользователь. Пользователь получит все права, предоставленные каждой из его групп.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='Группы')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Особые права для этого пользователя.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='Права пользователя')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
