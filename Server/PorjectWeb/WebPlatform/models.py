from django.db import models


class User(models.Model):

    username = models.CharField(max_length=20)  # 用户名
    password = models.CharField(max_length=20)  # 密码
    identity = models.IntegerField()    # 身份标识 管理员为0 学生为1 送水工为2

    def __str__(self):
        return self.username


class Oder(models.Model):
    oderNumber = models.IntegerField()  # 订单号
    student = models.CharField(max_length=20)   # 下订单的人
    waterman = models.CharField(max_length=20)  # 送水工
    date = models.CharField(max_length=50)  # 日期格式例如2018030115:04  就是指2018年3月1号15点04分
    interval = models.CharField(max_length=50)   # 要求几个小时内送达
    amount = models.IntegerField()  #订单水量
    address = models.CharField(max_length=500)  # 地址
    allocation = models.IntegerField()  # 是否已经分配送水员 0为未分配 1为已分配
    complete = models.IntegerField()    # 订单是否完成 0为未完成 1为已完成

    def __str__(self):
        return 'The Oder Message %d : %r %r %r %d %d %r %d %d' %(self.oderNumber, self.student, self.waterman, self.date,
                                                                 self.interval, self.amount, self.address,
                                                                 self.allocation, self.complete)


class Complain(models.Model):
    oderNumber = models.IntegerField()  # 订单号
    username = models.CharField(max_length=20)  # 用户名
    content = models.CharField(max_length=500)  # 投诉内容

    def __str__(self):
        return self.content
