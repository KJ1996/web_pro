import Footer from '@/components/Footer';

import Vue from 'vue';

describe('Footer.vue', () => {
    
    // 描述要测试的最小单元
    it('组件加载后', () => {

        const Constructor = Vue.extend(Footer);
		
		const VM = new Constructor().$mount();
        expect(VM.$el.textContent).to.contain('@copyright YoungKid 2018');
        
    });

  	

});
