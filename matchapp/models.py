from django.db import models


class SiteUser(models.Model):
    rank = models.PositiveIntegerField(verbose_name="Rank")

    level = models.PositiveIntegerField(verbose_name="Level")

    real_name = models.CharField(verbose_name="Realname", max_length=20)

    main_user_name = models.CharField(verbose_name="Mainusername", max_length=20)

    def __str__(self):
        return self.main_user_name + "/" + self.real_name

# class ReqruitmentObj(models.Model):

# class ActionObj(models.Model):

# class Rank(models.Model):

# class Platform(models.Model):

# class UserSec(models.Model):
