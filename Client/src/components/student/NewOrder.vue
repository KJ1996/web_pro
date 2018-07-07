<template>
	<el-form  ref= "newOrderForm" :model= "newOrderForm" :rules= "newOrderRules" label-width= "110px">
		<el-form-item prop= "address" label= "宿舍地址">
			<el-input name= "address" v-model= "newOrderForm.address" placeholder= "精确至门牌号"></el-input>
		</el-form-item>
		<el-form-item label= "期望送达时间" prop= "interval">
			<el-time-select
				name= "interval"
				:picker-options= "{
					start: '09:00',
					step: '00:60',
					end: '18:00'	
					}"
				v-model= "newOrderForm.interval">
			</el-time-select>
		</el-form-item>
		<el-form-item label= "数量" prop= "amount">
			<el-radio-group name= "amount" v-model="newOrderForm.amount">
	          <el-radio-button label="1">一桶</el-radio-button>
	          <el-radio-button label="2">两桶</el-radio-button>
	        </el-radio-group>
		</el-form-item>
		<el-form-item >
			<el-button type= "primary" @click= "submit">
				提交
			</el-button>
		</el-form-item>
	</el-form>
</template>

<script>
import { newOrder } from '@/api/order'
export default {
	name: 'NewOrder',
	data() {
		
		return {
			newOrderForm: {
				username: this.$store.getters.username,
				address: '',
				interval: '',
				amount: '',
				date:''
			},
			newOrderRules: {
				address: [{required: true, message: '请填写宿舍信息'}],
				interval: [{required: true, message: '请选择收货时间'}],
				amount: [{required: true, message: '请选择桶装水数量'}]
			}
		}
	},
	methods: {
		submit() {
			this.$refs.newOrderForm.validate(valid => {
				if (valid) {
					this.newOrderForm.date= (new Date()).toLocaleString()
					newOrder(this.newOrderForm).then(() => {
						this.$refs.newOrderForm.resetFields()
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
.el-form {
	margin-top: 60px;
}
</style>