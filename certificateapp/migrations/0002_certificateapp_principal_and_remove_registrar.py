from django.db import migrations, models


COLLEGE_NAME = "Model Polytechnic College Karunagappally"


class Migration(migrations.Migration):
    dependencies = [
        ("certificateapp", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="certificateapp",
            old_name="dean_name",
            new_name="principal_name",
        ),
        migrations.RemoveField(
            model_name="certificateapp",
            name="registrar_name",
        ),
        migrations.AlterField(
            model_name="certificateapp",
            name="college_name",
            field=models.CharField(
                default=COLLEGE_NAME,
                max_length=150,
            ),
        ),
    ]
