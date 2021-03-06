# Generated by Django 3.2.2 on 2021-05-17 20:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('supershop_app', '0002_auto_20210516_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_count',
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cart_code', models.UUIDField(default=uuid.uuid4)),
                ('added_products', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='supershop_app.product')),
            ],
        ),
    ]
