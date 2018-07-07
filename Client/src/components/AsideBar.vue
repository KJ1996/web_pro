<template>
	<el-menu
		router				
		:collapse= "asideBar.isCollapse"
		@mouseenter.native= "barOut"
		@mouseleave.native= "barIn"
		:default-active= "$route.path"
		text-color= "#fff"
		active-text-color= "#ffd04b"
		background-color= "rgb(0,88,37)">
		<el-menu-item v-for= "item in options" :index= "item.index" :key= "item.index">
			<i :class= "item.class"></i>
			<span slot= "title">{{ item.title }}</span>
		</el-menu-item>
	</el-menu>
</template>

<script>
export default {
	name: 'AsideBar',
	props:['options'],
	data() {
		return {
			asideBar: {
				isCollapse: false
			}
		}
	},
	methods: {
		barOut() {
			this.asideBar.isCollapse = false
		},
		barIn() {
			this.asideBar.isCollapse = true
		}
	}
}
</script>

<style scoped>
.el-menu {
	height: 100%;
}
</style>