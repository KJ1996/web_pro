import axios from 'axios'
import store from '@/store'
import router from '@/router'
import { MessageBox } from 'element-ui'


const service = axios.create({
	baseURL: 'http://172.18.156.217:8888',
	timeout: 5000,
	withCredentials: true
})
//ajax拦截器 给每次请求都加上token
/*service.interceptors.request.use(
	config => {
		if (store.getters.token) {
			// token名应该和后端协商
			config.headers['X-Token'] = getToken()
		}
		return config
	}, err => {
		return Promise.reject(err)
	}
)*/

service.interceptors.response.use(
	response => {
		return response
	}, err => {
		if (err.response) {
			switch (err.response.status) {
				case '401': 
					MessageBox.alert('登录已失效！')
					router.push({
						path:'/'
					})
			}
		}
		return Promise.reject(err)
	}
)
export default service