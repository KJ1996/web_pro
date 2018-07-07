<template>
	<div>
		<p>订单号：{{ $store.getters.orderInfo.orderNumber }}</p>
		<p>下单时间：{{ $store.getters.orderInfo.date }}</p>
		<p>配送员：{{ $store.getters.orderInfo.waterman }}</p>

		<el-form style= "width:380px">
			<el-form-item>
				<el-input type= "textarea" :rows= "8"
					v-model= "complaintForm.textarea"
					placeholder= "请输入内容">
					
				</el-input>
			</el-form-item>
			<el-form-item>
				<el-button type= "primary" @click= "ComplaintOrder">提交
				</el-button>
			</el-form-item>
		</el-form>
	</div>
</template>

<script>
import { complaintOrder } from '@/api/order'

export default {
	name: 'ComplaintOrder',
	data() {
		return {
			complaintForm: {
				textarea: ''
			}
		}
	},
	methods: {
		ComplaintOrder() {
			complaintOrder(this.$store.getters.username, 
				this.$store.getters.orderInfo.orderNumber, 
				this.complaintForm.textarea).then(() => {
					this.$router.push({
						name: 'Student'
					})
				}).catch(err => {
					this.$alert(err)
				})
		}
	},
	created() {
		if (!this.$store.getters.orderInfo) {
			this.$alert('订单信息已丢失').then(() => {
				this.$router.go(-1)
			})
		}
	}
}
</script>

<style>
</style>