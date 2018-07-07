import Vue from 'vue'
import Router from 'vue-router'
import Entrance from '@/components/Entrance'
import Student from '@/components/Student'
import Admin from '@/components/Admin'
import Logout from '@/components/Logout'
import Success from '@/components/Success'
import Dispatcher from '@/components/Dispatcher'
Vue.use(Router)

export default new Router({
  routes: [
	{
	  path: '/',
	  name: 'Entrance',
	  component: Entrance,
	  redirect: '/login',
	  children: [
		{ path: '/login', component: () => import('@/components/entrance/Login') },
		{ path: '/signUp', component: () => import('@/components/entrance/SignUp') }
	  ]
	},
	{
		path: '/student/',
		name: 'Student',
		component: Student,
	  	redirect: '/student/newOrder',
	  	children: [
		{ path: '/student/newOrder', component:() => import('@/components/student/NewOrder'), meta: { requireAuth: true } },
		{ path: '/student/historyOrder', component:() => import('@/components/student/HistoryOrder'), meta: { requireAuth: true } },
		{ path: '/student/complaintOrder', component:() => import('@/components/student/ComplaintOrder'), meta: { requireAuth: true } }
	  ]
	},
	{
	  path: '/admin',
	  name: 'Admin',
	  meta: {
		requireAuth: true
	  },
	  redirect: '/admin/newOrder',
	  component: Admin,
	  children: [
		{ path: '/admin/newOrder', component:() => import('@/components/admin/NewOrder'), meta: { requireAuth: true } },
		{ path: '/admin/historyOrder', component:() => import('@/components/admin/HistoryOrder'), meta: { requireAuth: true } },
		{ path: '/admin/notice', component:() => import('@/components/admin/Notice'), meta: { requireAuth: true } }
	  ]
	},
	{
	  path: '/logout',
	  name: 'Logout',
	  component: Logout
	},
	{
	  path: '/success',
	  name: 'Success',
	  component: Success
	},
	{
	  path: '/dispatcher',
	  name: 'Dispatcher',
	  meta: {
		requireAuth: true
	  },
	  component: Dispatcher
	}
  ]
})
