<template>
	<el-table
		:row-class-name= "tableRowClassName"
		:data= "tableData">
		<el-table-column
			v-for= "item in options"
			:key= "item.prop"
			:prop= "item.prop"
			width= "180"
			:label= "item.label">
		</el-table-column>
	</el-table>
</template>

<script>
import { getHistoryOrdersByAdmin } from '@/api/order'
export default {
	name: 'historyOrder',
	data() {
		return {
			tableData: [
				{
					orderNumber: '1001',
					date: '2018-06-11',
					interval: '09:30',
					address: 'shensiyuan',
					amount: 2,
					waterman: 'xxx',
					complete: true
				}
			],
			options: [
				{
					prop: 'orderNumber',
					label: '订单号'
				},
				{
					prop: 'date',
					label: '下单时间'
				},
				{
					prop: 'address',
					label: '宿舍'
				},
				{
					prop: 'amount',
					label: '桶装水数量'
				},
				{
					prop: 'waterman',
					label: '配送员'
				}
			]
		}
	},
	methods: {
		tableRowClassName({row, index}) {
			if (row.complete) {
				return 'success-row'
			}
			return 'warning-row'
		}
	},
	created() {
		getHistoryOrdersByAdmin().then((res) => {
			this.tableData= res.data.order.filter(v => v.complete)
		}).catch(err => {
			this.$alert(err)
		})
	}
}
</script>