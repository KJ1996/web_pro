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
import { fetchNotice } from '@/api/notice'
export default {
	name: 'Student',
	components: {
		AsideBar
	},
  	data() {
		return {
			options: [
				{
					index: '/student/newOrder',
					class: 'el-icon-circle-plus-outline',
					title: '新的订单'
				},
				{
					index: '/student/historyOrder',
					class: 'el-icon-date',
					title: '历史订单'
				},
				{
					index: '/logout',
					class: 'el-icon-arrow-left',
					title: '退出登录'
				}
			]
		}
	},
	created() {
		fetchNotice().then((res) => {
			const content= res.data.content
			if (content) {
				this.$message(`公告: ${content}`)
			}
		}).catch(err => {
			this.$alert(err)
		})
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