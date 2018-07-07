const getters = {
	username: state => state.user.username,
	identity: state => state.user.identity,
	orderInfo: state => state.order.orderInfo
}

export default getters