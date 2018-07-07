<template>
	<el-table
		stripe
		:data= "tableData">
		<el-table-column
			prop= "orderNumber"
			width= "150"
			label= "订单号">
		</el-table-column>
		<el-table-column
			width= "180"
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
				<el-select
					v-model= "scope.row.waterman"
					placeholder= "请选择">
					<el-option
						v-for= "(item, index) in watermen"
						:key= "item.username"
						:label= "`${index+1}号`"
						:value= "item.username">
						</el-option>
				</el-select>
			</template>
		</el-table-column>
		<el-table-column
			width= "150"
			label= "操作">
			<template slot-scope= "scope">
				<el-button 
					size= "mini" 
					@click= "AllocateOrder(scope.$index, scope.row)">
					确认
				</el-button>
			</template>
		</el-table-column>
	</el-table>
</template>

<script>
import { allocateOrder, getHistoryOrdersByAdmin } from '@/api/order'
import { getWatermen } from '@/api/account'

export default {
	name: 'newOrder',
	data() {
		return {
			tableData: [
				{
					orderNumber: '1019',
					date: '2018-06-11',
					interval: '10:30',
					address: 'shensiyuan',
					amount: 2,
					waterman: '',
					complete: false
				}
			],
			watermen: [
				{
					value: '1',
					label: '1号'
				},
				{
					value: '2',
					label: '2号'
				},
				{
					value: '3',
					label: '3号'
				}
			]
		}
	},
	methods: {
		AllocateOrder(index, row) {
			if (!row.waterman) {
				this.$alert('送水员必选！')
			}
			allocateOrder(row.waterman, row.orderNumber).then(() => {
				this.tableData.splice(row, 1)
			}).catch(err => {
				this.$alert(err)
			})
		}
	},
	created() {

		getHistoryOrdersByAdmin().then(res => {
			this.tableData= res.data.order.filter(v => !v.complete)
		}).catch(err => {
			this.$alert(err)
		})
		
		getWatermen().then(res => {
			this.watermen= res.data.waterman
		}).catch(err => {
			this.$alert(err)
		})
		

	}
}
</script>

<style></style>