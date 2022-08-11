# Generated by Django 4.0.6 on 2022-08-11 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedbackstudent',
            name='student',
        ),
        migrations.RemoveField(
            model_name='leavereportstaff',
            name='staff',
        ),
        migrations.RemoveField(
            model_name='leavereportstudent',
            name='student',
        ),
        migrations.RemoveField(
            model_name='notificationstaff',
            name='staff',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='session',
        ),
        migrations.RemoveField(
            model_name='student',
            name='session',
        ),
        migrations.DeleteModel(
            name='FeedbackStaff',
        ),
        migrations.DeleteModel(
            name='FeedbackStudent',
        ),
        migrations.DeleteModel(
            name='LeaveReportStaff',
        ),
        migrations.DeleteModel(
            name='LeaveReportStudent',
        ),
        migrations.DeleteModel(
            name='NotificationStaff',
        ),
        migrations.DeleteModel(
            name='Session',
        ),
    ]
