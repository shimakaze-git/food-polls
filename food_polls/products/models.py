from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel


class Product(TimeStampedModel, SoftDeletableModel):
    name = models.CharField(
        verbose_name='商品名',
        blank=True,
        null=False,
        max_length=150,
        default='',
    )
    # vendor = 販売店
    # manufacturer = 製造者
    # ean_code = models.IntegerField() janコード

    image = models.ImageField(
        verbose_name='パッケージ写真',
        null=True,
        blank=True,
        upload_to='images/'
    )
