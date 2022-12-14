# Generated by Django 4.1.3 on 2022-11-25 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0002_remove_jobseek_callstatus_jobseek_call_tatus_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='definition',
        ),
        migrations.AddField(
            model_name='jobseek',
            name='call_tatus_defenition',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobseek',
            name='meet_status_defenition',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobseek',
            name='meetemp_status_defenition',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobseek',
            name='test_status_defenition',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='callstatus',
            name='status',
            field=models.CharField(choices=[(0, 'Состоялось'), (1, 'Перезвонить'), (2, 'Недозвон')], max_length=300),
        ),
        migrations.AlterField(
            model_name='denialstatus',
            name='status',
            field=models.CharField(choices=[(0, 'Активный'), (1, 'Отказ рекрутёра'), (2, 'Отказ соискателя'), (3, 'Отказ заказчика')], max_length=300),
        ),
        migrations.AlterField(
            model_name='meetempstatus',
            name='status',
            field=models.CharField(choices=[(0, 'Состоялось'), (1, 'Перезвонить'), (2, 'Недозвон')], max_length=300),
        ),
        migrations.AlterField(
            model_name='meetstatus',
            name='status',
            field=models.CharField(choices=[(0, 'Запланировано'), (1, 'Состоялось'), (2, 'Не состоялось')], max_length=300),
        ),
        migrations.AlterField(
            model_name='statusjob',
            name='status',
            field=models.CharField(choices=[(0, 'Открыта'), (1, 'Закрыта'), (2, 'Заморожена')], max_length=300),
        ),
        migrations.AlterField(
            model_name='teststatus',
            name='status',
            field=models.CharField(choices=[(0, 'В работе'), (1, 'Не выполнено'), (2, 'Отказ от выполнения'), (3, 'Выполнено')], max_length=300),
        ),
    ]
