# Generated by Django 4.1.1 on 2023-02-05 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='api.user', verbose_name='получатель'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='api.user', verbose_name='отправитель'),
        ),
        migrations.AlterField(
            model_name='user',
            name='chat_id',
            field=models.IntegerField(verbose_name='ID чата'),
        ),
    ]
