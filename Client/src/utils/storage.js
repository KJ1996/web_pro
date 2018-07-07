export function getUserInfo() {
	return JSON.parse(sessionStorage.getItem('userInfo'))
}

export function setUserInfo(userInfo) {
	sessionStorage.setItem('userInfo', JSON.stringify(userInfo))
}

export function clearStorage() {
	sessionStorage.clear()
}

export function getOrderInfo() {
	return JSON.parse(sessionStorage.getItem('orderInfo'))
}

export function setOrderInfo(orderInfo) {
	sessionStorage.setItem('orderInfo', JSON.stringify(orderInfo))
}