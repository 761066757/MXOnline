# Generated by Django 2.2 on 2020-05-18 13:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=50, verbose_name='课程名')),
                ('desc', models.CharField(max_length=300, verbose_name='课程描述')),
                ('learn_times', models.IntegerField(default=0, verbose_name='学习时长(分钟数)')),
                ('degree', models.CharField(choices=[('cj', '初级'), ('zj', '中级'), ('gj', '高级')], max_length=2, verbose_name='难度')),
                ('students', models.IntegerField(default=0, verbose_name='学习人数')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏人数')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击数')),
                ('notice', models.CharField(default='', max_length=300, verbose_name='课程公告')),
                ('category', models.CharField(default='后端开发', max_length=20, verbose_name='课程类别')),
                ('tag', models.CharField(default='', max_length=10, verbose_name='课程标签')),
                ('youneed_know', models.CharField(default='', max_length=300, verbose_name='课程须知')),
                ('teacher_tell', models.CharField(default='', max_length=300, verbose_name='老师告诉你')),
                ('is_classics', models.BooleanField(default=False, verbose_name='是否经典')),
                ('detail', models.CharField(max_length=500, verbose_name='课程详情')),
                ('is_banner', models.BooleanField(default=False, verbose_name='是否广告位')),
                ('image', models.ImageField(upload_to='courses/%Y/%m', verbose_name='封面图')),
                ('course_org', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organizations.CourseOrg', verbose_name='课程机构')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.Teacher', verbose_name='讲师')),
            ],
            options={
                'verbose_name': '课程信息',
                'verbose_name_plural': '课程信息',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=100, verbose_name='章节名')),
                ('learn_times', models.IntegerField(default=0, verbose_name='学习时长(分钟数)')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='课程')),
            ],
            options={
                'verbose_name': '课程章节',
                'verbose_name_plural': '课程章节',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=100, verbose_name='视频名')),
                ('learn_times', models.IntegerField(default=0, verbose_name='学习时长(分钟数)')),
                ('url', models.CharField(max_length=1000, verbose_name='访问地址')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Lesson', verbose_name='章节')),
            ],
            options={
                'verbose_name': '视频',
                'verbose_name_plural': '视频',
            },
        ),
        migrations.CreateModel(
            name='CourseTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('tag', models.CharField(max_length=100, verbose_name='标签')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='课程')),
            ],
            options={
                'verbose_name': '课程标签',
                'verbose_name_plural': '课程标签',
            },
        ),
        migrations.CreateModel(
            name='CourseResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('file', models.FileField(max_length=200, upload_to='course/resourse/%Y/%m', verbose_name='下载地址')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='课程')),
            ],
            options={
                'verbose_name': '课程资源',
                'verbose_name_plural': '课程资源',
            },
        ),
        migrations.CreateModel(
            name='BannerCourse',
            fields=[
            ],
            options={
                'verbose_name': '轮播课程',
                'verbose_name_plural': '轮播课程',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('courses.course',),
        ),
    ]
