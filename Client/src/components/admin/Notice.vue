<template>
	<el-form
		@submit.native.prevent
		label-width="80px"
		ref= "noticeForm" 
		:model= "noticeForm">
		<el-form-item label= "公告类型:">
			<el-select placeholder= "请选择公告对何人可见" v-model= "noticeForm.type">
				<el-option label= "仅学生" value= "1"></el-option>
				<el-option label= "仅配送员" value= "2"></el-option>
				<el-option label= "全体可见" value= "3"></el-option>
			</el-select>
		</el-form-item>
		<el-form-item label= "公告内容:">
			<el-input type= "textarea" v-model= "noticeForm.content" :rows= "8" style= "width:380px;"></el-input>
		</el-form-item>
		<el-form-item>
			<el-button type= "primary" @click= "PublishNotice">发布公告</el-button>
		</el-form-item>
	</el-form>
</template>

<script>
import { publishNotice } from '@/api/notice'
export default {
	name: 'notice',
	data() {
		return {
			noticeForm: {
				type: '',
				content: ''
			}
		}
	},
	methods: {
		PublishNotice() {
			publishNotice(this.noticeForm).then(res => {
				this.$refs.noticeForm.resetFields()
			}).catch(err => {
				this.$alert(err)
			})
		}
	}
}
</script>

<style></style>