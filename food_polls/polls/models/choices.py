from enum import Enum

from django.db import models
from django.contrib.auth import get_user_model

from model_utils.models import TimeStampedModel, SoftDeletableModel

User = get_user_model()


class PreferenceStatus(Enum):
    """
    PreferenceStatus.

    好みの状態.
    """

    ATE = 1  # 食べた
    NOT_ATE = 2  # 食べていない

    @classmethod
    def choices(cls):
        """choices."""
        return [(m.value, m.name) for m in cls]


class ChoiceStatus(Enum):
    """
    ChoiceStatus.
    """

    ATE_THREE = 6  # 人にすすめたい
    ATE_TWO = 5  # また買いたい
    ATE_ONE = 4  # 普通、一回食べて満足.
    ATE_ZERO = 3  # 自分の味覚には合わない.

    NOT_ATE_TWO = 2  # 食べてみたい
    NOT_ATE_ONE = 1  # 売っていない
    NOT_ATE_ZERO = 0  # 自分の味覚に合わなそうなので食べない

    @classmethod
    def choices(cls):
        """choices."""
        return [(m.value, m.name) for m in cls]


class PreferenceChoice(TimeStampedModel, SoftDeletableModel):
    """ 好みに対する選択. """

    # 食べた or 食べていない flag
    preference = models.PositiveSmallIntegerField(
        verbose_name="食べた or 食べていないflag",
        choices=PreferenceStatus.choices(),
        blank=False,
        null=False,
        default=PreferenceStatus.ATE.value,
    )

    # 食べてみたい ~ 人に勧めたい など
    choice_status = models.IntegerField(
        verbose_name="感想の選択肢",
        choices=ChoiceStatus.choices(),
        blank=True,
        null=True
    )

    def get_all_choices(self):
        """
        preferenceの状態によって選択できるchoice_statusを返す.
        """

        choices = {}

        choices[PreferenceStatus.ATE.value] = [
            {ChoiceStatus.ATE_THREE.value: '人にすすめたい'},
            {ChoiceStatus.ATE_TWO.value: 'また買いたい'},
            {ChoiceStatus.ATE_ONE.value: '普通、一回食べて満足'},
            {ChoiceStatus.ATE_ZERO.value: '自分の味覚には合わない'}
        ]

        choices[PreferenceStatus.NOT_ATE.value] = [
            {ChoiceStatus.NOT_ATE_TWO.value: '食べてみたい'},
            {ChoiceStatus.NOT_ATE_ONE.value: '売っていない'},
            {ChoiceStatus.NOT_ATE_ZERO.value: '自分の味覚に合わなそうなので食べない'}
        ]

        return choices

    def get_select_choices(self):
        """
        preferenceの状態によって選択できるchoice_statusを返す.
        """

        if self.preference == PreferenceStatus.ATE.value:
            return [
                (ChoiceStatus.ATE_THREE.value, '人にすすめたい'),
                (ChoiceStatus.ATE_TWO.value, 'また買いたい'),
                (ChoiceStatus.ATE_ONE.value, '普通、一回食べて満足.'),
                (ChoiceStatus.ATE_ZERO.value, '自分の味覚には合わない.')
            ]
        else:
            return [
                (ChoiceStatus.NOT_ATE_TWO.value, '食べてみたい'),
                (ChoiceStatus.NOT_ATE_ONE.value, '売っていない'),
                (ChoiceStatus.NOT_ATE_ZERO.value, '自分の味覚に合わなそうなので食べない.')
            ]
