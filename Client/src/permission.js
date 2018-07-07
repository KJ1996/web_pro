import router from './router'
import store from './store'
import { MessageBox } from 'element-ui'
import { getUserInfo } from '@/utils/storage'

const roles = ["Student", "Dispatcher", "Admin"]

router.beforeEach((to, from, next) => {
	if (to.meta.requireAuth) {
		console.log('it needs auth')
		const userInfo = getUserInfo()
		if (userInfo) {
			store.commit('SET_USERNAME', userInfo.username)
			store.commit('SET_IDENTITY', roles[userInfo.identity-1])
			next()
		} else {
			MessageBox.alert('请先登录').then(() => {
				next({
					path: '/'
				})
			})
			
		}
	} else {
		console.log('it does not need auth')
		next()
	}
})

