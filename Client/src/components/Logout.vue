<template>
	
</template>

<script>

export default {
	name: 'Logout',
	created() {
		this.$store.dispatch('RemoveAuth').then(() => {
			this.$alert('退出登录成功，即将返回首页').then(() => {
				this.$router.push({
					name: 'Entrance'
				})
			})
		}).catch(err => {
			if (err.response) {
				console.log(err.response)
			}
			this.$alert('退出登录失败，返回用户界面').then(() => {
				this.$router.go(-1)
			})
			
			
		})
	}
}
</script>

<style scoped>
#info {
	text-align: center;
	font-size: 28px;
}
</style>

