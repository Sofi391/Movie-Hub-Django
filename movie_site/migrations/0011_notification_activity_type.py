from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_site', '0010_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='type',
            field=models.CharField(
                choices=[
                    ('System', 'System'),
                    ('Admin', 'Admin'),
                    ('Reminder', 'Reminder'),
                    ('Quiz', 'Quiz'),
                    ('Badge', 'Badge'),
                    ('Activity', 'Activity'),
                ],
                max_length=100,
            ),
        ),
    ]
