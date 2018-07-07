import Student from '@/components/Student';
import AsideBar from '@/components/AsideBar';
import Vue from 'vue';

describe('AsideBar.vue', () => {
    
    // 描述要测试的最小单元
    it('组件加载后', () => {

        const Constructor = Vue.extend(AsideBar);
		
		const VM = new Constructor().$mount();
        expect(VM.asideBar.isCollapse).to.equal(false);
        
    });

     it('barOut后', () => {

        const Constructor = Vue.extend(AsideBar);
        
        const VM = new Constructor().$mount();
        VM.barIn();
        VM.barOut();
        expect(VM.asideBar.isCollapse).to.equal(false);
        

    });

     it('barIn后', () => {

        const Constructor = Vue.extend(AsideBar);
        
        const VM = new Constructor().$mount();
        VM.barIn();
        //VM.barOut();
        expect(VM.asideBar.isCollapse).to.equal(true);
        

    });

});
