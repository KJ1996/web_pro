<template>
		<el-form :model= "signUpForm" :rules = "signUpRules" ref= "signUpForm" id = "signUp">
			<el-form-item prop= "username">
				<el-input name= "username" type= "text" v-model= "signUpForm.username" placeholder= "学号/工号" />
			</el-form-item>
			<el-form-item prop= "password">
				<el-input name= "password" type= "password" v-model= "signUpForm.password" placeholder= "密码" />
			</el-form-item>
			<el-form-item prop= "confirm">
				<el-input name= "confirm" type= "password" v-model= "signUpForm.confirm" placeholder= "确认密码" />
			</el-form-item>
			<el-form-item  prop="identity">
				<el-radio-group name= "identity" v-model="signUpForm.identity">
					<el-radio-button label="1">学生</el-radio-button>
					<el-radio-button label="2">配送员</el-radio-button>
				</el-radio-group>
			</el-form-item>
			<el-form-item>
				<el-button type= "primary" @click= "signUpClick">注册</el-button>
			</el-form-item>
		</el-form>
</template>

<script>
import { validateUsername, validatePassword } from '@/utils/validator'
import { signUp } from '@/api/account'

export default {
	name: 'Signup',
	data() {
		const validateConfirm = (rule, value, callback) => {
			if (value !== this.signUpForm.password) {
				callback(new Error('两次密码应一致！'))
			} else {
				callback()
			}
		}
		return {
			signUpForm: {
				username: '',
				password: '',
				confirm: '',
				identity: '',
				fn: signUp
			},
			signUpRules: {
				username: [{required: true, trigger: 'blur', validator: validateUsername}],
				password: [{required: true, trigger: 'blur', validator: validatePassword}],
				confirm: [{required: true, trigger: 'blur', validator: validateConfirm}],
				identity: [{required: true, trigger: 'blur', message: '请选择账户类型。'}]
			}
		}
	},
	methods: {
		signUpClick: function() {
			this.$refs.signUpForm.validate(valid => {
				if (valid) {
					this.$store.dispatch('GetAuth', this.signUpForm).then(() => {
						this.$router.push({
							name: 'Success'
						})
					}).catch(err => {
						this.$alert(err)
					})
				}
			})

		}
	}
}
</script>

<style scoped>
.el-form-item {
	position: relative;
	left: 45px;
}
.el-button,
.el-input {
	width: 70%;
}
</style>