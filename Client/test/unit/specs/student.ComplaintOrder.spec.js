import ComplaintOrder from '@/components/student/ComplaintOrder';
import Vue from 'vue';


describe('ComplaintOrder.vue', () => {
    
    // 描述要测试的最小单元
    it('用户输入后', () => {

        const Constructor = Vue.extend(ComplaintOrder);
        const VM = new Constructor().$mount();
        VM.complaintForm.textarea="test";
        expect(VM.complaintForm.textarea).to.equal("test");
		
    });



 

});
