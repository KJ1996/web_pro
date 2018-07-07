
import { logout } from '@/api/account'
import { setUserInfo } from '@/utils/storage'
const roles = ["Student", "Dispatcher", "Admin"]

const user = {
	state: {
		username: '',
		identity: ''
	},
	

	mutations: {
		SET_USERNAME: (state, username) => {
			state.username = username
		},
		SET_IDENTITY: (state, identity) => {
			state.identity = identity
		}
	}, 

	actions: {
		GetAuth(context, userInfo) {
			const username = userInfo.username.trim()
			const identity = userInfo.identity
			return new Promise((resolve, reject) => {
				userInfo.fn(username, userInfo.password, identity).then((res) => {
					const data = res.data
					context.commit('SET_USERNAME', username)
					context.commit('SET_IDENTITY', roles[identity-1])
					setUserInfo(userInfo)
					resolve()
				}).catch((err) => {
					reject(err)
				})
			})
		},
		RemoveAuth(context) {
			return new Promise((resolve, reject) => {
				logout().then(() => {
					context.commit('SET_USERNAME', '')
					context.commit('SET_IDENTITY', '')
					console.log('here1')
					resolve()
				}).catch(err => {
					reject(err)
				})
			})
		}
	}
}

export default user