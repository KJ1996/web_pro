import request from '@/utils/request'

export function login(username, password, identity) {
	const params = {
		username, 
		password,
		identity
	}
	return request({
		url: '/login',
		method: 'get', 
		params
	})
}

export function signUp(username, password, identity) {
	const data = {
		username, 
		password,
		identity
	}
	return request({
		url: '/register',
		method: 'post', 
		data
	})
}

export function logout() {
	return request({
		url: '/logout',
		method: 'get'
	})
}

export function getWatermen() {
	return request({
		url: '/get_waterman',
		method: 'get'
	})
}