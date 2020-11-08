# Generated by Django 3.0.8 on 2020-11-08 02:40
import random

from django.db import migrations

from aitojunction.models import Place

l = [
    "1594877656_b.jpg",
    "1594877838_b.jpg",
    "DSCN1367-1024x768.jpg",
    "IMG_9582 2.jpg",
    "IMG_9584.jpg",
    "IMG_9651.jpg",
    "IMG_9706.jpg",
    "IMG_9716.jpg",
    "_EatPlayWorks_1st_TheRestaurant_Oxomoco.jpg",
    "_EatPlayWorks_1st_TheRestaurant_terrace.jpg",
    "_EatPlayWorks_2rd_TheRestaurant_Gracia.jpg",
    "_EatPlayWorks_3rd_Lounge.jpg",
    "_EatPlayWorks_3rd_LoungeOffice.jpg",
    "_EatPlayWorks_5th_OfficeRoom.jpg",
    "c-members_1.jpg",
    "eatplayworks-3.jpg",
    "eatplayworks20200630-020.jpg",
    "img_03fbc3ece79ceccf76ade27bb2766bc6364536.jpg",
    "ダウンロード.jpeg"
]

def forwards_func(apps, schema_editor):
    prefix = 'https://s3.ap-northeast-2.amazonaws.com/static.seoulsounds.net/EPW/'
    for place in Place.objects.all():
        place.image_url = prefix + random.choice(l)
        print(place.image_url)
        place.save(update_fields=["image_url"])


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('aitojunction', '0010_auto_20201108_0238'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func)
    ]
