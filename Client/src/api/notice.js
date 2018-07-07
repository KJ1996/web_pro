import request from '@/utils/request'

export function publishNotice(noticeForm) {
	const data= {
		content: noticeForm.content
	}

	return request({
		url: '/do_notice',
		method: 'post',
		data
	})
}

export function fetchNotice() {

	return request({
		url: '/get_notice',
		method: 'get'
	})
}