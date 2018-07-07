<template>
	<el-container>
		<el-aside>
			<aside-bar :options= "options"></aside-bar>
		</el-aside>
		<el-main>
			<router-view/>
		</el-main>
	</el-container>
</template>

<script>
import AsideBar from './AsideBar'
export default {
	name: 'Admin',
	components: {
		AsideBar
	},
	data() {
		return {
			options: [
				{
					index: '/admin/newOrder',
					class: 'el-icon-circle-plus-outline',
					title: '未处理订单'
				},
				{
					index: '/admin/historyOrder',
					class: 'el-icon-date',
					title: '已处理订单'
				},
				{
					index: '/admin/notice',
					class: 'el-icon-edit-outline',
					title: '发布公告'
				},
				{
					index: '/logout',
					class: 'el-icon-arrow-left',
					title: '退出登录'
				}
			]
		}
	}
}


</script>

<style scoped>

.el-container {
	position: absolute;
    top: 85px;
    bottom: 0px;
}
.el-main {
	overflow-y: auto;
}
</style>