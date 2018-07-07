import Success from '@/components/Success';

import Vue from 'vue';

describe('AsideBar.vue', () => {
    
    // 描述要测试的最小单元
    it('组件加载后', () => {

        const Constructor = Vue.extend(Success);
		
		const VM = new Constructor().$mount();
        expect(VM.seconds).to.equal(3);
        
    });


});
