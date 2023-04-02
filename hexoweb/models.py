from django.db import models
import uuid


class Cache(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(max_length=0x7FFFFFFF)
    content = models.TextField(max_length=0x7FFFFFFF, blank=True)


class SettingModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(max_length=0x7FFFFFFF)
    content = models.TextField(max_length=0x7FFFFFFF, blank=True)


class ImageModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(max_length=0x7FFFFFFF)
    url = models.TextField(max_length=0x7FFFFFFF)
    size = models.TextField(max_length=0x7FFFFFFF)
    date = models.TextField(max_length=0x7FFFFFFF)
    type = models.TextField(max_length=0x7FFFFFFF)


class FriendModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(max_length=0x7FFFFFFF, blank=False)
    url = models.TextField(max_length=0x7FFFFFFF, blank=False)
    imageUrl = models.TextField(max_length=0x7FFFFFFF)
    time = models.TextField(max_length=0x7FFFFFFF, blank=False)
    description = models.TextField(max_length=0x7FFFFFFF)
    status = models.BooleanField(default=True)


class NotificationModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    time = models.TextField(max_length=0x7FFFFFFF)
    label = models.TextField(max_length=0x7FFFFFFF, blank=True)
    content = models.TextField(max_length=0x7FFFFFFF, blank=True)


class CustomModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(max_length=0x7FFFFFFF)
    content = models.TextField(max_length=0x7FFFFFFF, blank=True)


class StatisticUV(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ip = models.GenericIPAddressField()


class StatisticPV(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField()
    number = models.IntegerField(default=0)


class TalkModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField(max_length=0x7FFFFFFF, blank=True)
    tags = models.TextField(max_length=0x7FFFFFFF, blank=True)
    time = models.TextField(max_length=0x7FFFFFFF)
    like = models.TextField(max_length=0x7FFFFFFF, blank=True, default="[]")
    values = models.TextField(max_length=0x7FFFFFFF, default="{}")


class EssayModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField(max_length=0x7FFFFFFF, blank=True)
    tags = models.TextField(max_length=0x7FFFFFFF, blank=True)
    time = models.TextField(max_length=0x7FFFFFFF)
    like = models.TextField(max_length=0x7FFFFFFF, blank=True, default="[]")
    values = models.TextField(max_length=0x7FFFFFFF, default="{}")

class VerificationCodeModel(models.Model):
    mail=models.CharField(primary_key=True, max_length=50, verbose_name='邮箱')
    name=models.CharField(unique=False, max_length=30, verbose_name='名称')
    key=models.CharField(unique=False, max_length=30, verbose_name='验证码')
    validtime=models.IntegerField(default=0)

class MailModel(models.Model):
    mail=models.CharField(primary_key=True, max_length=50, verbose_name='邮箱')
    name=models.CharField(unique=False, max_length=30, verbose_name='名称')

class PostLikeModel(models.Model):
    postName=models.CharField(primary_key=True, max_length=50, verbose_name='文章名称')
    like=models.IntegerField(default=0)

class SentMailModel(models.Model):
    id = models.AutoField(primary_key=True)
    sendermail=models.CharField(max_length=50, verbose_name='发送者邮箱')
    sendername=models.CharField(max_length=30, verbose_name='发送者名称')
    revmail=models.CharField(max_length=50, verbose_name='接收者邮箱')
    revname=models.CharField(max_length=30, verbose_name='接收者名称')
    sendtime=models.IntegerField(default=0, verbose_name='发送时间')