import HistoryOrder from '@/components/student/HistoryOrder';
import Vue from 'vue';


describe('HistoryOrder.vue', () => {
    
    // 描述要测试的最小单元
    it('组件加载后', () => {

        const Constructor = Vue.extend(HistoryOrder);
		const tableData=[
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
            ];
		const VM = new Constructor().$mount();
        expect(VM.tableData[1].orderNumber).to.equal(tableData[1].orderNumber);
        expect(VM.tableData[1].date).to.equal(tableData[1].date);
        expect(VM.tableData[1].address).to.equal(tableData[1].address);
        expect(VM.tableData[1].amount).to.equal(tableData[1].amount);
        expect(VM.tableData[1].waterman).to.equal(tableData[1].waterman);
        expect(VM.tableData[1].complete).to.equal(tableData[1].complete);
        expect(VM.tableData[0].orderNumber).to.equal(tableData[0].orderNumber);
        expect(VM.tableData[0].date).to.equal(tableData[0].date);
        expect(VM.tableData[0].address).to.equal(tableData[0].address);
        expect(VM.tableData[0].amount).to.equal(tableData[0].amount);
        expect(VM.tableData[0].waterman).to.equal(tableData[0].waterman);
        expect(VM.tableData[0].complete).to.equal(tableData[0].complete);
       //  const VM = new Constructor().$mount();
            expect(true).to.equal(true);
    });
     it('ConfirmOrder函数1',  ()  => {

        const Constructor = Vue.extend(HistoryOrder);
        
        const VM = new Constructor().$mount();
        const row=VM.tableData[0];
        const index = VM.tableData.indexOf(row);
        //VM.ConfirmOrder(row,index);
        
       
        VM.ConfirmOrder(row,index);
        expect(VM.tableData[0].complete).to.equal(true);
   

    });

     it('ConfirmOrder函数2',  ()  => {

        const Constructor = Vue.extend(HistoryOrder);
        
        const VM = new Constructor().$mount();
        const row=VM.tableData[1];
        const index = VM.tableData.indexOf(row);
        //VM.ConfirmOrder(row,index);
        
       
        VM.ConfirmOrder(index,row);
        expect(VM.tableData[1].complete).to.equal(true);
   

    });
      it('CancelOrder函数',  () => {

        const Constructor = Vue.extend(HistoryOrder);
        
        const VM = new Constructor().$mount();

       const button = VM.$el.querySelector('#delete_button');
        const clickEvent = new window.Event('click');
        button.dispatchEvent(clickEvent);
        VM._watcher.run();
      const row=VM.tableData[0];
        const index = VM.tableData.indexOf(row);
        //VM.ConfirmOrder(row,index);
        
       
        VM.CancelOrder(VM.tableData[0],index);*/
        expect(VM.tableData[1].complete).to.equal(false);
   

    });

 

});
