
from django.test import TestCase
from WebPlatform import models


# Django的单元测试基于unittest库
class StudentTestCase(TestCase):
    # 测试函数执行前执行
    def setUp(self):
        print("======in setUp")
        username = 15331100
        password = 15331100
        identity = 1
        models.User.objects.create(username=username, password=password, identity=identity)
        oderNumber = 12302143
        student = 15331100
        waterman = 15331133
        date = 20170789
        interval = 5
        amount = 2
        address = "慎思园6号514"
        allocation = 0
        complete = 0
        models.Oder.objects.create(oderNumber=oderNumber, student=student, waterman=waterman, date=date,
                                   interval=interval,
                                   amount=amount, address=address, allocation=allocation, complete=complete)

        content = "超时未送达"
        models.Complain.objects.create(username=username, oderNumber=oderNumber, content=content)

    # 需要测试的内容
    def test_check_exit(self):
        username = 15331100
        password = 15331100
        oderNumber = 12302143
        student = 15331100
        waterman = 15331133
        date = 20170789
        interval = 5
        amount = 2
        address = "慎思园6号514"
        allocation = 0
        complete = 0
        content = "超时未送达"
        user = models.User.objects.get(username=username)
        oder = models.Oder.objects.get(oderNumber=oderNumber)
        complain = models.Complain.objects.get(oderNumber=oderNumber)
        self.assertEqual(user.username, str(username))
        self.assertEqual(user.password, str(password))
        self.assertEqual(user.identity, 1)
        self.assertEqual(oder.oderNumber, oderNumber)
        self.assertEqual(oder.student, str(student))
        self.assertEqual(oder.waterman, str(waterman))
        self.assertEqual(oder.date, str(date))
        self.assertEqual(oder.interval, str(interval))
        self.assertEqual(oder.amount, amount)
        self.assertEqual(oder.address, address)
        self.assertEqual(oder.allocation, allocation)
        self.assertEqual(oder.complete, complete)
        self.assertEqual(complain.content, content)
    # 测试函数执行后执行
    def tearDown(self):
        print("======in tearDown")


