<template>
	<el-table
		:row-class-name= "tableRowClassName"
		:data= "tableData">
		<el-table-column
			prop= "orderNumber"
			width= "150"
			label= "订单号">
		</el-table-column>
		<el-table-column
			width= "200"
			label= "下单时间">
			<template slot-scope= "scope">
				<i class= "el-icon-time"></i>
				<el-popover
					placement= "top"
					trigger= "hover">
					<p>期望送达时间： {{ scope.row.interval }}</p>
					<span slot= "reference" class= "name-wrapper">
						<el-tag size= "medium">{{ scope.row.date }}</el-tag>
					</span>
				</el-popover>
			</template>
		</el-table-column>
		<el-table-column 
			prop= "address"
			width= "150"
			label= "宿舍">
		</el-table-column>
		<el-table-column 
			prop= "amount"
			width= "150"
			label= "数量">
		</el-table-column>
		<el-table-column 
			width= "150"
			label= "配送员">
			<template slot-scope= "scope">
				<span v-if= "!Boolean(scope.row.waterman)">未分配</span>
				<span v-show= "Boolean(scope.row.waterman)">{{ scope.row.waterman }}</span>
			</template>
		</el-table-column>
		<el-table-column
			width= "220"
			label= "操作">
			<template slot-scope= "scope">
				<el-button 
					:disabled= "Boolean(scope.row.complete)"
					size= "mini" 
					@click= "ConfirmOrder(scope.$index, scope.row)">
					确认
				</el-button>
				<el-button size= "mini" @click= "CancelOrder(scope.$index, scope.row)" :disabled= "!!scope.row.waterman">
					取消
				</el-button>
				<el-button size= "mini" type= "danger" @click= "toComplaintComponent(scope.$index, scope.row)">
					投诉
				</el-button>
			</template>
		</el-table-column>
	</el-table>
</template>

<script>
import { confirmOrder, getHistoryOrdersByStudent, cancelOrder } from '@/api/order'

export default {
	name: 'HistoryOrder',
	data() {
		return {
			tableData:[
				{
					orderNumber: '1001',
					date: '2018-06-11',
					interval: '09:30',
					address: 'shensiyuan',
					amount: 2,
					waterman: 'xxx',
					complete: true
				},
				{
					orderNumber: '1019',
					date: '2018-06-11',
					interval: '09:30',
					address: 'shensiyuan',
					amount: 1,
					waterman: '',
					complete: false
				}
			]

		}
	},
	methods: {
		ConfirmOrder(index, row) {
			confirmOrder(row.orderNumber).then((res) => {
				row.complete = true
			}).catch(err => {
				this.$alert(err)
			})
		},
		CancelOrder(index, row) {
			cancelOrder(row.orderNumber).then((res) => {
				this.tableData.splice(index, 1)
			}).catch((err) => {
				this.$alert(err)
			})
		},
		toComplaintComponent(index, row) {
			this.$store.commit('SET_ORDERINFO', row)
			this.$router.push({
				path: '/student/complaintOrder'
			})
		},
		tableRowClassName({row, index}) {
			if (row.complete) {
				return 'success-row'
			}
			return 'warning-row'
		}
	},
	created() {
		getHistoryOrdersByStudent(this.$store.getters.username).then((res) => {
			this.tableData = res.data.order
		}).catch(err => {
			this.$alert(err)
		})
	}
}
	
</script>

<style>
</style>