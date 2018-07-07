<template>
		<div id="app">
			<router-view/>
		</div>
</template>

<script>
export default {
	name: 'App'
}




</script>

<style>
body {
	margin: 0;
}
#app {
	font-family: 'Avenir', Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	color: #2c3e50;
}

.el-table .success-row {
	background: #f0f9eb;
}
.el-table .warning-row {
	background: oldlace;
}
</style>
