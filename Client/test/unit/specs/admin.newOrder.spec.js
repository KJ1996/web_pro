import newOrder from '@/components/student/newOrder';
import Vue from 'vue';


describe('newOrder.vue', () => {
    
    // 描述要测试的最小单元
    it('组件加载后', () => {

        const Constructor = Vue.extend(newOrder);
		const tableData=[
               {
                    orderNumber: '1019',
                    date: '2018-06-11',
                    interval: '10:30',
                    address: 'shensiyuan',
                    amount: 2,
                    waterman: '',
                    complete: false
                }
            ];
		const VM = new Constructor().$mount();
        expect(VM.tableData[0].orderNumber).to.equal(tableData[0].orderNumber);
        expect(VM.tableData[0].date).to.equal(tableData[0].date);
        expect(VM.tableData[0].address).to.equal(tableData[0].address);
        expect(VM.tableData[0].amount).to.equal(tableData[0].amount);
        expect(VM.tableData[0].waterman).to.equal(tableData[0].waterman);
        expect(VM.tableData[0].complete).to.equal(tableData[0].complete);

            expect(true).to.equal(true);
    });
     it('AllocateOrder函数1',  ()  => {

        const Constructor = Vue.extend(HistoryOrder);
        
        const VM = new Constructor().$mount();
        const row=VM.tableData[0];
        const index = VM.tableData.indexOf(row);
      
        
       
        VM.AllocateOrder(index,row);
       expect(VM.tableData[0].waterman).to.equal("");
   

    });

     it('AllocateOrder函数2',  ()  => {

        const Constructor = Vue.extend(HistoryOrder);
        
        const VM = new Constructor().$mount();
        VM.tableData.push({
             orderNumber: '1019',
                    date: '2018-06-11',
                    interval: '10:30',
                    address: 'shensiyuan',
                    amount: 2,
                    waterman: '',
                    complete: false
        });
        VM.tableData[0].waterman="XX";
        const row=VM.tableData[0];
        const index = VM.tableData.indexOf(row);
      
        
       
        VM.AllocateOrder(index,row);
        expect(VM.tableData[0].waterman).to.equal("");
   

    });


 

});
