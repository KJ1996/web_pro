import Dispatcher from '@/components/Dispatcher';
import Vue from 'vue';
import 'babel-polyfill';

describe('Dispatcher.vue', () => {
    
    // 描述要测试的最小单元
    it('组件加载后', () => {

        const Constructor = Vue.extend(Dispatcher);
		
		const VM = new Constructor().$mount();

        expect(true).to.equal(true);
        
    });

    

});
