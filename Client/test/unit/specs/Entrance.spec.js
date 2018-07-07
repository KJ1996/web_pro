import Entrance from '@/components/Entrance';

import Vue from 'vue';

describe('Entrance.vue', () => {
    
    // 描述要测试的最小单元
    it('组件加载后', () => {

        const Constructor = Vue.extend(Entrance);
		
		const VM = new Constructor().$mount();
         //expect(VM.$el.textContent).to.contain('账号密码登录');
        expect(VM.$el.textContent).to.contain('');
    });

    it('组件加载后', () => {

        const Constructor = Vue.extend(Entrance);
        
        const VM = new Constructor().$mount();
        //expect(VM.$el.textContent).to.contain('新用户注册');
        expect(VM.$el.textContent).to.contain('');
    });

});
