from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.home, name='home'),
    path('login', views.login, name='login'),  # 登录
    path('register', views.register, name='register'),  # 注册
    path('new_order', views.new_oder, name='new_oder'),  # 下新订单
    path('manager_order', views.get_all_list_by_manager, name='get_all_list_by_manager'),  # 经理得到所有订单
    path('handle_list', views.handle_list_by_manager, name='handle_list_by_manager'),  # 经理得到所有需要处理的订单
    path('confirm_order', views.confirm_oder, name='confirm_oder'),  # 确认订单
    path('student_order', views.get_list_by_student, name='get_list_by_student'),  # 学生订单
    path('waterman_order', views.get_list_by_waterman, name='get_list_by_waterman'),  # 送水员订单
    path('check_complain', views.check_complain, name='check_complain'),  # 查询投诉
    path('do_complain', views.do_complain, name='do_complain'),  # 进行投诉
    path('cancle_complain', views.cancel_order, name='cancel_order'),  # 取消订单
    path('do_notice', views.do_notic, name='do_notice'),  # 发布公告
    path('get_notice', views.get_notice, name='get_notice'),  # 得到公告
    path('test', views.test, name='test'),
    path('get_waterman', views.get_waterman, name='get_waterman'), # 返回配送员
    path('logout', views.logout, name='logout') # 退出
]

