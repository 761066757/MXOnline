# Generated by Django 2.2 on 2020-05-18 13:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('image', models.ImageField(max_length=200, upload_to='banner/%Y/%m', verbose_name='轮播图')),
                ('url', models.URLField(verbose_name='访问地址')),
                ('index', models.IntegerField(default=0, verbose_name='顺序')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
            },
        ),
        migrations.CreateModel(
            name='UserAsk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('mobile', models.CharField(max_length=11, verbose_name='手机')),
                ('course_name', models.CharField(max_length=50, verbose_name='课程名')),
            ],
            options={
                'verbose_name': '用户咨询',
                'verbose_name_plural': '用户咨询',
            },
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('message', models.CharField(max_length=200, verbose_name='消息内容')),
                ('has_read', models.BooleanField(default=False, verbose_name='是否已读')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户消息',
                'verbose_name_plural': '用户消息',
            },
        ),
        migrations.CreateModel(
            name='UserFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('fav_id', models.IntegerField(verbose_name='数据id')),
                ('fav_type', models.IntegerField(choices=[(1, '课程'), (2, '课程机构'), (3, '讲师')], default=1, verbose_name='收藏类型')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户收藏',
                'verbose_name_plural': '用户收藏',
            },
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='课程')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户课程',
                'verbose_name_plural': '用户课程',
            },
        ),
        migrations.CreateModel(
            name='CourseComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('comments', models.CharField(max_length=200, verbose_name='评论内容')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='课程')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '课程评论',
                'verbose_name_plural': '课程评论',
            },
        ),
    ]
