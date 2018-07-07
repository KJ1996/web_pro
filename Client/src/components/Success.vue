<template>
	<div class="container">
		<p id = "info">已成功注册，<b>{{seconds}}</b> 秒后进入用户界面</p>	
	</div>
</template>

<script>

export default {
	name: 'Success',
	data() {
		return {
			seconds:3
		}
	},
	mounted: function() {
		console.log('I have been mounted');
		setInterval(() => {
			this.seconds--;
		}, 1000);
	},
	watch: {
		seconds: function(val, oldVal) {
			if (val == 0) {
				this.$router.push({
					name: this.$store.getters.identity
				})
			}
		}
	}
}
</script>

<style scoped>
#info {
	text-align: center;
	font-size: 28px;
}
</style>

