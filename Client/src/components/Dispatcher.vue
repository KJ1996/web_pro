<template>
	<div class= "container">
		<el-menu
			text-color= "#fff"
			background-color= "rgb(0,88,37)"
			active-text-color= "#ffd04b"
			:default-active= "$route.path"
			mode= "horizontal"
			router>
			<el-menu-item index= "/dispatcher">我的订单</el-menu-item>
			<el-menu-item index= "/logout">退出登录</el-menu-item>
		</el-menu>
		<div v-for= "item in list" :class= "{item: true, success: item.complete, warning: !item.complete}">
			<p>下单时间：{{ item.date }}</p>
			<p>宿舍：{{ item.address }}</p>
			<span>{{ item.amount }}桶</span>
			<span>期望送达时间：{{ item.interval }}</span>
		</div>
	</div>
</template>

<script>
import { getHistoryOrdersByWaterman } from '@/api/order'

export default {
	name: 'Dispatcher',
  	data() {
		return {
			list:[
				//Order(Date.now(), "shensiyuan", 1, false),
				{
					date:(new Date()).toLocaleString(),
					address:"慎思园六号502",
					amount:2,
					complete:true,
					allocation: true,
					orderNumber: 5,
					interval: '09:30'
				},
				{
					date:(new Date()).toLocaleString(),
					address:"慎思园六号502",
					amount:2,
					complete:false,
					allocation: true,
					orderNumber: 7,
					interval: '10:30'
				},
				{
					date:(new Date()).toLocaleString(),
					address:"慎思园六号502",
					amount:2,
					complete:true,
					allocation: true,
					orderNumber: 5,
					interval: '09:30'
				},
				{
					date:(new Date()).toLocaleString(),
					address:"慎思园六号502",
					amount:2,
					complete:false,
					allocation: true,
					orderNumber: 7,
					interval: '10:30'
				},
				{
					date:(new Date()).toLocaleString(),
					address:"慎思园六号502",
					amount:2,
					complete:true,
					allocation: true,
					orderNumber: 5,
					interval: '09:30'
				},
				{
					date:(new Date()).toLocaleString(),
					address:"慎思园六号502",
					amount:2,
					complete:false,
					allocation: true,
					orderNumber: 7,
					interval: '10:30'
				},
				{
					date:(new Date()).toLocaleString(),
					address:"慎思园六号502",
					amount:2,
					complete:true,
					allocation: true,
					orderNumber: 5,
					interval: '09:30'
				},
				{
					date:(new Date()).toLocaleString(),
					address:"慎思园六号502",
					amount:2,
					complete:false,
					allocation: true,
					orderNumber: 7,
					interval: '10:30'
				}
			]
		};
	},
	methods:{
		toLogout: function () {
			this.$router.push('/logout');
		}
	},
	created() {
		getHistoryOrdersByWaterman(this.$store.getters.username).then((res) => {
			this.list= res.data.order
		}).catch(err => {
			this.$alert(err)
			if (err.response) {
				console.log(err.response)
			}
		})
	}
}

</script>

<style  scoped>
.container {
	text-align: center;
	padding: 0;
	border: 1px solid black;
	width: 380px;
	overflow-y: auto;
}

.item {
	width: 100%;
	border-bottom: 1px solid black;
}
.success {
	background-color: #f0f9eb;
}
.warning {
	background-color: oldlace;
}
</style>