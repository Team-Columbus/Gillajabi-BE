# Generated by Django 4.2.1 on 2023-08-02 13:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_subscribe_sub_end_alter_subscribe_sub_start"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, null=True, verbose_name="이메일"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(
                blank=True, default="", max_length=30, null=True, verbose_name="이름"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(
                blank=True, max_length=30, null=True, verbose_name="비밀번호"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_id",
            field=models.CharField(
                blank=True, max_length=30, null=True, unique=True, verbose_name="아이디"
            ),
        ),
    ]
