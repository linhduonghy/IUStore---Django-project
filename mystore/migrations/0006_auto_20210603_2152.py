# Generated by Django 3.2.3 on 2021-06-03 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0005_rename_itemid_discount_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='commentid',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='itemid',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='productid',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='importproduct',
            old_name='import_fileid',
            new_name='import_file',
        ),
        migrations.RenameField(
            model_name='importproduct',
            old_name='productid',
            new_name='product',
        ),
    ]
