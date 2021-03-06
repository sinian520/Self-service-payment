# Generated by Django 2.2.1 on 2019-06-19 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jiage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jiage_leixing', models.IntegerField()),
                ('jiage_diyibz', models.CharField(max_length=20)),
                ('jiage_tidudaxiao', models.CharField(max_length=20)),
                ('jiage_xishu', models.CharField(max_length=20)),
                ('jiage_fengdingtd', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='xinwen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xinwen_id', models.IntegerField()),
                ('xinwen_biaoti', models.CharField(max_length=20)),
                ('xinwen_neirong', models.TextField(max_length=300)),
                ('xinwen_leixing', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='yonghu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('money', models.CharField(max_length=10)),
                ('tele', models.CharField(max_length=12)),
                ('live', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='yuangong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('money', models.CharField(max_length=20)),
                ('tele', models.CharField(max_length=12)),
                ('zhuangtai', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='yongliang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yongliang_type', models.IntegerField()),
                ('yongliang_jichumany', models.IntegerField()),
                ('yongliang_many', models.IntegerField()),
                ('yonghu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='axf.yonghu')),
            ],
        ),
        migrations.CreateModel(
            name='weixiudan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yonghu_leibie', models.CharField(max_length=20)),
                ('weixiu_stime', models.DateField()),
                ('yonghu_tel', models.CharField(max_length=12)),
                ('yonghu_home', models.CharField(max_length=50)),
                ('weixiu_news', models.CharField(max_length=100)),
                ('yonghu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='axf.yonghu')),
            ],
        ),
        migrations.CreateModel(
            name='weihu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weihu_id', models.IntegerField()),
                ('time', models.DateField()),
                ('money', models.CharField(max_length=20, null=True)),
                ('zhuangtai', models.BooleanField()),
                ('yonghu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='axf.yonghu')),
                ('yuangong_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='axf.yuangong')),
            ],
        ),
        migrations.CreateModel(
            name='feiyong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yonghu_id', models.IntegerField()),
                ('feiyong_danhaoid', models.IntegerField()),
                ('feiyong_kaishi', models.DateField()),
                ('feiyong_jieshu', models.DateField()),
                ('feiyong_qian', models.CharField(max_length=20)),
                ('feiyong_zhuangtai', models.BooleanField()),
                ('feiyong_leixing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='axf.jiage')),
                ('feiyong_yhid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='axf.yonghu')),
            ],
        ),
    ]
