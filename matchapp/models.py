from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Platform(models.Model):
    platform = models.IntegerField(verbose_name="Platform", choices=[(0, 'Origin(PC)'),
                                                                     (1, 'Steam(PC)'),
                                                                     (2, 'PlayStation'),
                                                                     (3, 'Xbox'),
                                                                     (4, 'Switch')])


class RankNumber(models.Model):
    rankNumber = models.IntegerField(verbose_name="Rank", choices=[(1, 'Ⅰ'),
                                                                   (2, 'Ⅱ'),
                                                                   (3, 'Ⅲ'),
                                                                   (4, 'Ⅳ')])


class InRank(models.Model):
    rank = models.IntegerField(verbose_name="Rank", choices=[(0, 'Predator'),
                                                             (1, 'Master'),
                                                             (2, 'Diamond'),
                                                             (3, 'Platinum'),
                                                             (4, 'Gold'),
                                                             (5, 'Silver'),
                                                             (6, 'Bronze')])

    rankNumber = models.ForeignKey(RankNumber, on_delete=models.CASCADE)


class SiteUser(models.Model):
    inRank = models.ForeignKey(InRank, on_delete=models.CASCADE)

    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)

    level = models.Field(verbose_name="Level", validators=[MinValueValidator(1), MaxValueValidator(500)])

    realName = models.CharField(verbose_name="Realname", max_length=20)

    mainUserName = models.CharField(verbose_name="Mainusername", max_length=20)

    def __str__(self):
        return self.mainUserName + "/" + self.realName


class ReqruitmentObj(models.Model):
    inRank = models.ForeignKey(InRank, on_delete=models.CASCADE)

    siteUser = models.ForeignKey(SiteUser, on_delete=models.CASCADE)

    neceNumber = models.IntegerField(verbose_name="NeceNumber", choices=[(1, '1人'), (2, '2人')])

    neceRank = models.PositiveIntegerField(verbose_name="NeceRank")

    rankOrCasual = models.CharField(verbose_name="RankOrCasual", max_length=50, choices=[('rank', 'ランク'), ('casual', 'カジュアル')])

    def __str__(self):
        return self.siteUser.mainUserName


class ActionObj(models.Model):
    reqruitmentObj = models.ForeignKey(ReqruitmentObj, on_delete=models.CASCADE)

    message = models.TextField(verbose_name="Message", max_length=150)

    accountId = models.CharField(verbose_name="AccountId", max_length=20)

    def __str__(self):
        return self.accountId

