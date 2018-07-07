import request from '@/utils/request'

export function newOrder(newOrderForm) {
	const data= newOrderForm

	return request({
		url: '/new_order',
		method: 'post',
		data
	})
}

export function confirmOrder(orderNumber) {
	const data = {
		orderNumber
	}

	return request({
		url: '/confirm_order',
		method: 'post',
		data	
	})
}

export function cancelOrder(orderNumber) {
	const data= {
		orderNumber
	}

	return request({
		url: '',
		method: 'post',
		data
	})
}

export function getHistoryOrdersByStudent(username) {
	const params =  {
		username
	}

	return request({
		url: '/student_order',
		method: 'get',
		params
	})
}

export function complaintOrder(username, orderNumber, content) {
	const data= {
		username,
		orderNumber,
		content
	}

	return request({
		url: '/do_complain',
		method: 'post',
		data
	})
}



export function getHistoryOrdersByAdmin() {

	return request({
		url: '/manager_order',
		method: 'get'
	})
}

export function allocateOrder(waterman, orderNumber) {
	const data= {
		waterman,
		orderNumber
	}

	return request({
		url: '/handle_list',
		method: 'post',
		data
	})
}

export function getHistoryOrdersByWaterman(username) {
	const params =  {
		username
	}

	return request({
		url: '/waterman_order',
		method: 'get',
		params
	})
}