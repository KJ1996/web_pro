<template>
		<el-form :model= "loginForm" :rules = "loginRules" ref= "loginForm" id = "login">
			<el-form-item prop= "username">
				<el-input name= "username" type= "text" v-model= "loginForm.username" placeholder= "学号/工号" />
			</el-form-item>
			<el-form-item prop= "password">
				<el-input name= "password" type= "password" v-model= "loginForm.password" placeholder= "密码" />
			</el-form-item>
			<el-form-item  prop="identity">
				<el-radio-group name= "identity" v-model="loginForm.identity">
					<el-radio-button label="1">学生</el-radio-button>
					<el-radio-button label="2">配送员</el-radio-button>
					<el-radio-button label="3">管理员</el-radio-button>
				</el-radio-group>
			</el-form-item>
			<el-form-item>
				<el-button type= "primary" @click= "loginClick">登录</el-button>
			</el-form-item>
		</el-form>
		

		
</template>

<script>
import { validateUsername, validatePassword } from '@/utils/validator'
import { login } from '@/api/account'

export default {
	name : 'Login',
	data() {  
		return {
			loginForm: {
				username: '',
				password: '',
				identity: '',
				fn: login
			},
			loginRules:{
				username:[{required: true, trigger: 'blur', validator: validateUsername}],
				password:[{required: true, trigger: 'blur',validator: validatePassword}],
				identity:[{required: true, message:'请选择账户类型。'}]
			}    
		}
	},
	methods: {
		loginClick: function() {
			this.$refs.loginForm.validate(valid => {
				if (valid) {
					this.$store.dispatch('GetAuth', this.loginForm).then(() => {
						this.$router.push({
								name:this.$store.getters.identity
							})
					}).catch(err => {
						console.log(this.$store.getters.username)
						console.log('here2')
						this.$alert(err)
					})
				} else {
					console.log('error before login')
				}
			})
			
		}
	}
}
</script>

<style scoped>
.el-form-item {
	position:  relative;
	left: 45px;
}
.el-button,
.el-input {
	width: 70%;
}
</style>