# Generated by ShopOnline 4.2.5 on 2023-09-28 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_productmodel_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='descriptions',
            field=models.TextField(blank=True, null=True),
        ),
    ]