from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
import random
import json
from WebPlatform import models
import re

Notice = ""

# 控制器


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
        return cls._instance


class UserController(Singleton):
    def login_function(self, username, password):
        print(username, password)
        try:
            temp = models.User.objects.get(username=username, password=password)
            resp = {'right': 'True', 'msg': 'login successfully', 'session': 'NULL'}
            return resp
        except models.User.DoesNotExist:
            resp = {'right': 'False', 'msg': 'login failed', 'session': 'NULL'}
            return resp

    def register_function(self, username, password, identity):
        try:
            temp = models.User.objects.get(username=username)
            resp = {'right': 'False', 'msg': 'sign up failed'}
            return resp
        except models.User.DoesNotExist:
            models.User.objects.create(username=username, password=password, identity=identity)
            resp = {'right': 'True', 'msg': 'sign up successfully'}
            return resp

    def new_oder_function(self, student, date, interval, amount, address):
        oderNumber = random.randint(0, 1000000)
        waterman = "null"
        allocation = 0
        complete = 0
        isOK = 0
        while isOK == 0:
            try:
                temp = models.Oder.objects.get(oderNumber=oderNumber)
                oderNumber = random.randint(0, 1000000)
            except models.Oder.DoesNotExist:
                isOK = 1

        models.Oder.objects.create(oderNumber=oderNumber, student=student, waterman=waterman, date=date, interval=interval,
                            amount=amount, address=address, allocation=allocation, complete=complete)

        oderr = models.Oder.objects.get(oderNumber=oderNumber)
        oderjson = {
            'orderNumber': oderr.oderNumber,
            'student': oderr.student,
            'waterman': oderr.waterman,
            'date': oderr.date,
            'interval': oderr.interval,
            'amount': oderr.amount,
            'address': oderr.address,
            'allocation': oderr.allocation,
            'complete': oderr.complete
        }
        resp = {'right': 'True', 'order': oderjson, 'msg': 'order  successfully'}
        return resp

    def get_all_list_by_manager_function(self):
        list = []
        for temp in models.Oder.objects.all():
            temp_list = {
                'orderNumber': temp.oderNumber,
                'student': temp.student,
                'waterman': temp.waterman,
                'date': temp.date,
                'interval': temp.interval,
                'amount': temp.amount,
                'address': temp.address,
                'allocation': temp.allocation,
                'complete': temp.complete
            }
            list.append(temp_list)

        resp = {'right': 'True', 'order': list, 'msg': 'get successfully'}
        return resp

    def handle_list_by_manager_function(self, waterman, oderNumber):
        try:
            obj = models.Oder.objects.get(oderNumber=oderNumber)
            obj.waterman = waterman
            obj.allocation = 1
            obj.save()
            obj = models.Oder.objects.get(oderNumber=oderNumber)
            temp_list = {
                'orderNumber': obj.oderNumber,
                'student': obj.student,
                'waterman': obj.waterman,
                'date': obj.date,
                'interval': obj.interval,
                'amount': obj.amount,
                'address': obj.address,
                'allocation': obj.allocation,
                'complete': obj.complete
            }
            resp = {'right': 'True', 'order': temp_list, 'msg': 'handled successfully'}
            return resp
        except models.Oder.DoesNotExist:
            temp_list = {}
            resp = {'right': 'True', 'order': temp_list, 'msg': 'handled failed'}
            return resp

    def confirm_oder_function(self, oderNumber):
        try:
            obj = models.Oder.objects.get(oderNumber=oderNumber)
            obj.complete = 1
            obj.save()
            obj = models.Oder.objects.get(oderNumber=oderNumber)
            temp_list = {
                'orderNumber': obj.oderNumber,
                'student': obj.student,
                'waterman': obj.waterman,
                'date': obj.date,
                'interval': obj.interval,
                'amount': obj.amount,
                'address': obj.address,
                'allocation': obj.allocation,
                'complete': obj.complete
            }
            resp = {'right': 'True', 'order': temp_list, 'msg': 'confirm successfully'}
            return resp
        except models.Oder.DoesNotExist:
            temp_list = {}
            resp = {'right': 'True', 'order': temp_list, 'msg': 'confirm successfully'}
            return resp

    def get_list_by_student_function(self, username):
        list = []
        for temp in models.Oder.objects.filter(student=username):
            temp_list = {
                'orderNumber': temp.oderNumber,
                'student': temp.student,
                'waterman': temp.waterman,
                'date': temp.date,
                'interval': temp.interval,
                'amount': temp.amount,
                'address': temp.address,
                'allocation': temp.allocation,
                'complete': temp.complete
            }
            list.append(temp_list)
        resp = {'right': 'True', 'order': list, 'msg': 'get successfully'}
        return resp

    def get_list_by_waterman_function(self, username):
        list = []
        for temp in models.Oder.objects.filter(waterman=username):
            temp_list = {
                'orderNumber': temp.oderNumber,
                'student': temp.student,
                'waterman': temp.waterman,
                'date': temp.date,
                'interval': temp.interval,
                'amount': temp.amount,
                'address': temp.address,
                'allocation': temp.allocation,
                'complete': temp.complete
            }
            list.append(temp_list)
        resp = {'right': 'True', 'order': list, 'msg': 'get successfully'}
        return resp

    def check_complain_function(self):
        list = []
        for temp in models.Complain.objects.all():
            temp_list = {
                'username': temp.username,
                'orderNumber': temp.oderNumber,
                'content': temp.content
            }
            list.append(temp_list)
        resp = {'right': 'True', 'complain': list, 'msg': 'check successfully'}
        return resp

    def do_complain_function(self, username, orderNumber, content):
        models.Complain.objects.create(username=username, oderNumber=orderNumber, content=content)
        list = {
            'username': username,
            'orderNumber': orderNumber,
            'content': content
        }
        resp = {'right': 'True', 'complain': list, 'msg': 'do complain successfully'}
        return resp

    def cancel_order_function(self, orderNumber):
        models.Oder.objects.filter(oderNumber=orderNumber).delete()
        resp = {'right': 'True', 'msg': 'Delete successfully'}
        return resp

    def get_waterman_function(self):
        list = []
        for temp in models.User.objects.filter(identity=2):
            temp_list = {
                'username': temp.username,
            }
            list.append(temp_list)
        resp = {'right': 'True', 'waterman': list, 'msg': 'waterman successfully'}
        return resp

class OderController(Singleton):
    def login_function(self, username, password):
        print(username, password)
        try:
            temp = models.User.objects.get(username=username, password=password)
            resp = {'right': 'True', 'msg': 'login successfully', 'session': 'NULL'}
            return resp
        except models.User.DoesNotExist:
            resp = {'right': 'False', 'msg': 'login failed', 'session': 'NULL'}
            return resp

    def register_function(self, username, password, identity):
        try:
            temp = models.User.objects.get(username=username)
            resp = {'right': 'False', 'msg': 'sign up failed'}
            return resp
        except models.User.DoesNotExist:
            models.User.objects.create(username=username, password=password, identity=identity)
            resp = {'right': 'True', 'msg': 'sign up successfully'}
            return resp

    def new_oder_function(self, student, date, interval, amount, address):
        oderNumber = random.randint(0, 1000000)
        waterman = "null"
        allocation = 0
        complete = 0
        isOK = 0
        while isOK == 0:
            try:
                temp = models.Oder.objects.get(oderNumber=oderNumber)
                oderNumber = random.randint(0, 1000000)
            except models.Oder.DoesNotExist:
                isOK = 1

        models.Oder.objects.create(oderNumber=oderNumber, student=student, waterman=waterman, date=date, interval=interval,
                            amount=amount, address=address, allocation=allocation, complete=complete)

        oderr = models.Oder.objects.get(oderNumber=oderNumber)
        oderjson = {
            'orderNumber': oderr.oderNumber,
            'student': oderr.student,
            'waterman': oderr.waterman,
            'date': oderr.date,
            'interval': oderr.interval,
            'amount': oderr.amount,
            'address': oderr.address,
            'allocation': oderr.allocation,
            'complete': oderr.complete
        }
        resp = {'right': 'True', 'order': oderjson, 'msg': 'order  successfully'}
        return resp

    def get_all_list_by_manager_function(self):
        list = []
        for temp in models.Oder.objects.all():
            temp_list = {
                'orderNumber': temp.oderNumber,
                'student': temp.student,
                'waterman': temp.waterman,
                'date': temp.date,
                'interval': temp.interval,
                'amount': temp.amount,
                'address': temp.address,
                'allocation': temp.allocation,
                'complete': temp.complete
            }
            list.append(temp_list)

        resp = {'right': 'True', 'order': list, 'msg': 'get successfully'}
        return resp

    def handle_list_by_manager_function(self, waterman, oderNumber):
        try:
            obj = models.Oder.objects.get(oderNumber=oderNumber)
            obj.waterman = waterman
            obj.allocation = 1
            obj.save()
            obj = models.Oder.objects.get(oderNumber=oderNumber)
            temp_list = {
                'orderNumber': obj.oderNumber,
                'student': obj.student,
                'waterman': obj.waterman,
                'date': obj.date,
                'interval': obj.interval,
                'amount': obj.amount,
                'address': obj.address,
                'allocation': obj.allocation,
                'complete': obj.complete
            }
            resp = {'right': 'True', 'order': temp_list, 'msg': 'handled successfully'}
            return resp
        except models.Oder.DoesNotExist:
            temp_list = {}
            resp = {'right': 'True', 'order': temp_list, 'msg': 'handled failed'}
            return resp

    def confirm_oder_function(self, oderNumber):
        try:
            obj = models.Oder.objects.get(oderNumber=oderNumber)
            obj.complete = 1
            obj.save()
            obj = models.Oder.objects.get(oderNumber=oderNumber)
            temp_list = {
                'orderNumber': obj.oderNumber,
                'student': obj.student,
                'waterman': obj.waterman,
                'date': obj.date,
                'interval': obj.interval,
                'amount': obj.amount,
                'address': obj.address,
                'allocation': obj.allocation,
                'complete': obj.complete
            }
            resp = {'right': 'True', 'order': temp_list, 'msg': 'confirm successfully'}
            return resp
        except models.Oder.DoesNotExist:
            temp_list = {}
            resp = {'right': 'True', 'order': temp_list, 'msg': 'confirm successfully'}
            return resp

    def get_list_by_student_function(self, username):
        list = []
        for temp in models.Oder.objects.filter(student=username):
            temp_list = {
                'orderNumber': temp.oderNumber,
                'student': temp.student,
                'waterman': temp.waterman,
                'date': temp.date,
                'interval': temp.interval,
                'amount': temp.amount,
                'address': temp.address,
                'allocation': temp.allocation,
                'complete': temp.complete
            }
            list.append(temp_list)
        resp = {'right': 'True', 'order': list, 'msg': 'get successfully'}
        return resp

    def get_list_by_waterman_function(self, username):
        list = []
        for temp in models.Oder.objects.filter(waterman=username):
            temp_list = {
                'orderNumber': temp.oderNumber,
                'student': temp.student,
                'waterman': temp.waterman,
                'date': temp.date,
                'interval': temp.interval,
                'amount': temp.amount,
                'address': temp.address,
                'allocation': temp.allocation,
                'complete': temp.complete
            }
            list.append(temp_list)
        resp = {'right': 'True', 'order': list, 'msg': 'get successfully'}
        return resp

    def check_complain_function(self):
        list = []
        for temp in models.Complain.objects.all():
            temp_list = {
                'username': temp.username,
                'orderNumber': temp.oderNumber,
                'content': temp.content
            }
            list.append(temp_list)
        resp = {'right': 'True', 'complain': list, 'msg': 'check successfully'}
        return resp

    def do_complain_function(self, username, orderNumber, content):
        models.Complain.objects.create(username=username, oderNumber=orderNumber, content=content)
        list = {
            'username': username,
            'orderNumber': orderNumber,
            'content': content
        }
        resp = {'right': 'True', 'complain': list, 'msg': 'do complain successfully'}
        return resp

    def cancel_order_function(self, orderNumber):
        models.Oder.objects.filter(oderNumber=orderNumber).delete()
        resp = {'right': 'True', 'msg': 'Delete successfully'}
        return resp


class ComplainController(Singleton):
    def login_function(self, username, password):
        print(username, password)
        try:
            temp = models.User.objects.get(username=username, password=password)
            resp = {'right': 'True', 'msg': 'login successfully', 'session': 'NULL'}
            return resp
        except models.User.DoesNotExist:
            resp = {'right': 'False', 'msg': 'login failed', 'session': 'NULL'}
            return resp

    def register_function(self, username, password, identity):
        try:
            temp = models.User.objects.get(username=username)
            resp = {'right': 'False', 'msg': 'sign up failed'}
            return resp
        except models.User.DoesNotExist:
            models.User.objects.create(username=username, password=password, identity=identity)
            resp = {'right': 'True', 'msg': 'sign up successfully'}
            return resp

    def new_oder_function(self, student, date, interval, amount, address):
        oderNumber = random.randint(0, 1000000)
        waterman = "null"
        allocation = 0
        complete = 0
        isOK = 0
        while isOK == 0:
            try:
                temp = models.Oder.objects.get(oderNumber=oderNumber)
                oderNumber = random.randint(0, 1000000)
            except models.Oder.DoesNotExist:
                isOK = 1

        models.Oder.objects.create(oderNumber=oderNumber, student=student, waterman=waterman, date=date, interval=interval,
                            amount=amount, address=address, allocation=allocation, complete=complete)

        oderr = models.Oder.objects.get(oderNumber=oderNumber)
        oderjson = {
            'orderNumber': oderr.oderNumber,
            'student': oderr.student,
            'waterman': oderr.waterman,
            'date': oderr.date,
            'interval': oderr.interval,
            'amount': oderr.amount,
            'address': oderr.address,
            'allocation': oderr.allocation,
            'complete': oderr.complete
        }
        resp = {'right': 'True', 'order': oderjson, 'msg': 'order  successfully'}
        return resp

    def get_all_list_by_manager_function(self):
        list = []
        for temp in models.Oder.objects.all():
            temp_list = {
                'orderNumber': temp.oderNumber,
                'student': temp.student,
                'waterman': temp.waterman,
                'date': temp.date,
                'interval': temp.interval,
                'amount': temp.amount,
                'address': temp.address,
                'allocation': temp.allocation,
                'complete': temp.complete
            }
            list.append(temp_list)

        resp = {'right': 'True', 'order': list, 'msg': 'get successfully'}
        return resp

    def handle_list_by_manager_function(self, waterman, oderNumber):
        try:
            obj = models.Oder.objects.get(oderNumber=oderNumber)
            obj.waterman = waterman
            obj.allocation = 1
            obj.save()
            obj = models.Oder.objects.get(oderNumber=oderNumber)
            temp_list = {
                'orderNumber': obj.oderNumber,
                'student': obj.student,
                'waterman': obj.waterman,
                'date': obj.date,
                'interval': obj.interval,
                'amount': obj.amount,
                'address': obj.address,
                'allocation': obj.allocation,
                'complete': obj.complete
            }
            resp = {'right': 'True', 'order': temp_list, 'msg': 'handled successfully'}
            return resp
        except models.Oder.DoesNotExist:
            temp_list = {}
            resp = {'right': 'True', 'order': temp_list, 'msg': 'handled failed'}
            return resp

    def confirm_oder_function(self, oderNumber):
        try:
            obj = models.Oder.objects.get(oderNumber=oderNumber)
            obj.complete = 1
            obj.save()
            obj = models.Oder.objects.get(oderNumber=oderNumber)
            temp_list = {
                'orderNumber': obj.oderNumber,
                'student': obj.student,
                'waterman': obj.waterman,
                'date': obj.date,
                'interval': obj.interval,
                'amount': obj.amount,
                'address': obj.address,
                'allocation': obj.allocation,
                'complete': obj.complete
            }
            resp = {'right': 'True', 'order': temp_list, 'msg': 'confirm successfully'}
            return resp
        except models.Oder.DoesNotExist:
            temp_list = {}
            resp = {'right': 'True', 'order': temp_list, 'msg': 'confirm successfully'}
            return resp

    def get_list_by_student_function(self, username):
        list = []
        for temp in models.Oder.objects.filter(student=username):
            temp_list = {
                'orderNumber': temp.oderNumber,
                'student': temp.student,
                'waterman': temp.waterman,
                'date': temp.date,
                'interval': temp.interval,
                'amount': temp.amount,
                'address': temp.address,
                'allocation': temp.allocation,
                'complete': temp.complete
            }
            list.append(temp_list)
        resp = {'right': 'True', 'order': list, 'msg': 'get successfully'}
        return resp

    def get_list_by_waterman_function(self, username):
        list = []
        for temp in models.Oder.objects.filter(waterman=username):
            temp_list = {
                'orderNumber': temp.oderNumber,
                'student': temp.student,
                'waterman': temp.waterman,
                'date': temp.date,
                'interval': temp.interval,
                'amount': temp.amount,
                'address': temp.address,
                'allocation': temp.allocation,
                'complete': temp.complete
            }
            list.append(temp_list)
        resp = {'right': 'True', 'order': list, 'msg': 'get successfully'}
        return resp

    def check_complain_function(self):
        list = []
        for temp in models.Complain.objects.all():
            temp_list = {
                'username': temp.username,
                'orderNumber': temp.oderNumber,
                'content': temp.content
            }
            list.append(temp_list)
        resp = {'right': 'True', 'complain': list, 'msg': 'check successfully'}
        return resp

    def do_complain_function(self, username, orderNumber, content):
        models.Complain.objects.create(username=username, oderNumber=orderNumber, content=content)
        list = {
            'username': username,
            'orderNumber': orderNumber,
            'content': content
        }
        resp = {'right': 'True', 'complain': list, 'msg': 'do complain successfully'}
        return resp

    def cancel_order_function(self, orderNumber):
        models.Oder.objects.filter(oderNumber=orderNumber).delete()
        resp = {'right': 'True', 'msg': 'Delete successfully'}
        return resp

#  函数

def index(request):
    resp = {'errorcode': 100, 'detail': 'Get success'}
    return HttpResponse(json.dumps(resp), content_type="application/json")


def home(request):
    return HttpResponse("This is our HomePage !")

# 登录
def login(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    print(username, password)
    controller = UserController()
    resp = controller.login_function(username, password)
    if resp.get('right') == 'True':
        request.session['IS_LOGIN'] = True
        request.session['Name'] = username
        se = request.session.session_key
        print(request.session.session_key)
        resp.update(session=se)
    if resp.get('right') == 'True':
        return HttpResponse(json.dumps(resp), content_type="application/json")
    else:
        return HttpResponse(json.dumps(resp), content_type="application/json", status=400)


# 注册
def register(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    identity = data.get('identity')
    controller = UserController()
    resp = controller.register_function(username, password, identity)
    if resp.get('right') == 'True':
        request.session['IS_LOGIN'] = True
        request.session['Name'] = username
        return HttpResponse(json.dumps(resp), content_type="application/json")
    else:
        return HttpResponse(json.dumps(resp), content_type="application/json", status=400)



def new_oder(request):
    v = request.session.get('IS_LOGIN')
    if v:
        vvv = 1
    else:
        resp = {'right': 'False', 'msg': 'no session'}
        return HttpResponse(json.dumps(resp), content_type="application/json")
    data = json.loads(request.body)
    print(data)
    student = data.get('username')
    date = data.get('date')
    interval = data.get('interval')
    amount = data.get('amount')
    address = data.get('address')
    print(student, date, interval, amount, address)
    controller = OderController()
    resp = controller.new_oder_function(student=student, date=date, interval=interval, amount=amount, address=address)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def get_all_list_by_manager(request):
    controller = OderController()
    resp = controller.get_all_list_by_manager_function()
    v = request.session.get('IS_LOGIN')
    if v:
        return HttpResponse(json.dumps(resp), content_type="application/json")
    else:
        resp = {'right': 'False', 'msg': 'no session'}
        return HttpResponse(json.dumps(resp), content_type="application/json")


def handle_list_by_manager(request):
    v = request.session.get('IS_LOGIN')
    if v:
        vvv = 1
    else:
        resp = {'right': 'False', 'msg': 'no session'}
        return HttpResponse(json.dumps(resp), content_type="application/json")
    data = json.loads(request.body)
    waterman = data.get('waterman')
    oderNumber = data.get('orderNumber')
    controller = OderController()
    resp = controller.handle_list_by_manager_function(waterman, oderNumber)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def confirm_oder(request):
    v = request.session.get('IS_LOGIN')
    if v:
        vvv = 1
    else:
        resp = {'right': 'False', 'msg': 'no session'}
        return HttpResponse(json.dumps(resp), content_type="application/json")
    data = json.loads(request.body)
    oderNumber = data.get('orderNumber')
    controller = OderController()
    resp = controller.confirm_oder_function(oderNumber)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def get_list_by_student(request):
    username = request.GET.get('username')
    controller = OderController()
    print(username)
    resp = controller.get_list_by_student_function(username)
    v = request.session.get('IS_LOGIN')
    if v:
        return HttpResponse(json.dumps(resp), content_type="application/json")
    else:
        resp = {'right': 'False', 'msg': 'no session'}
        return HttpResponse(json.dumps(resp), content_type="application/json")



def get_list_by_waterman(request):
    username = request.GET.get('username')
    controller = OderController()
    resp = controller.get_list_by_waterman_function(username)
    v = request.session.get('IS_LOGIN')
    if v:
        return HttpResponse(json.dumps(resp), content_type="application/json")
    else:
        resp = {'right': 'False', 'msg': 'no session'}
        return HttpResponse(json.dumps(resp), content_type="application/json")


def logout(request):
    resp = {'right': 'Logout'}
    return HttpResponse(json.dumps(resp), content_type="application/json")


def check_complain(request):
    data = json.loads(request.body)
    controller = ComplainController()
    resp = controller.check_complain_function()
    v = request.session.get('IS_LOGIN')
    if v:
        return HttpResponse(json.dumps(resp), content_type="application/json")
    else:
        resp = {'right': 'False', 'msg': 'no session'}
        return HttpResponse(json.dumps(resp), content_type="application/json")



def do_complain(request):
    data = json.loads(request.body)
    username = data.get('username')
    orderNumber = data.get('orderNumber')
    content = data.get('content')
    v = request.session.get('IS_LOGIN')
    if v:
        controller = ComplainController()
        resp = controller.do_complain_function(username, orderNumber, content)
        return HttpResponse(json.dumps(resp), content_type="application/json")
    else:
        resp = {'right': 'False', 'msg': 'no session'}
        return HttpResponse(json.dumps(resp), content_type="application/json")


def cancel_order(request):
    data = json.loads(request.body)
    orderNumber = data.get('orderNumber')
    v = request.session.get('IS_LOGIN')
    if v:
        controller = OderController()
        resp = controller.cancel_order_function(orderNumber)
        return HttpResponse(json.dumps(resp), content_type="application/json")
    else:
        resp = {'right': 'False', 'msg': 'no session'}
        return HttpResponse(json.dumps(resp), content_type="application/json")


def do_notic(request):
    global Notice
    data = json.loads(request.body)
    notice = data.get('content')
    Notice = notice
    resp = {'right': 'Truce', 'content': Notice}
    return HttpResponse(json.dumps(resp), content_type="application/json")


def get_notice(request):
    global Notice
    notice = Notice
    print(notice)
    resp = {'right': 'True', 'content': notice}
    return HttpResponse(json.dumps(resp), content_type="application/json")


def get_waterman(requset):
    controller = UserController()
    resp = controller.get_waterman_function()
    return HttpResponse(json.dumps(resp), content_type="application/json")


# 要查询正确的表需要models.User.objects.get(id=1) 而不是 User.objects.get(id=1)
def test(request):
        username = '15331100'
        list = []
        temp = models.User.objects.get(id=1)
        list.append(temp.username)
        return HttpResponse(json.dumps(list), content_type="application/json")


#  特殊判断

