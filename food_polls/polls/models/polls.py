from django.db import models
from django.contrib.auth import get_user_model

from model_utils.models import TimeStampedModel, SoftDeletableModel

from products.models import Product
from polls.models import PreferenceChoice

User = get_user_model()


class Poll(TimeStampedModel, SoftDeletableModel):
    """ 投票モデル. """

    """フィールド."""
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='商品'
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=False,
        verbose_name="投票ユーザーyu-za-"
    )
    text = models.CharField(
        verbose_name='投票の感想.',
        blank=True,
        null=True,
        max_length=500,
        default=None
    )
    choices = models.ManyToManyField(
        PreferenceChoice,
        verbose_name='好みの選択肢'
    )
