
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0002_alter_balancete_data_alter_despesa_foto_boleto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balancete',
            name='data',
            field=models.DateTimeField(verbose_name='Data de registro'),
        ),
    ]
