import Admin from '@/components/Admin';

import Vue from 'vue';

describe('Admin.vue', () => {
    
    // 描述要测试的最小单元
    it('组件加载后', () => {

        const Constructor = Vue.extend(Admin);
		
		const VM = new Constructor().$mount();
       const options = [
                {
                    index: '/admin/newOrder',
                    class: 'el-icon-circle-plus-outline',
                    title: '未处理订单'
                },
                {
                    index: '/admin/historyOrder',
                    class: 'el-icon-date',
                    title: '已处理订单'
                },
                {
                    index: '/admin/notice',
                    class: 'el-icon-edit-outline',
                    title: '发布公告'
                },
                {
                    index: '/logout',
                    class: 'el-icon-arrow-left',
                    title: '退出登录'
                }
            ];

        expect(VM.options[0].index).to.equal(options[0].index);
        expect(VM.options[1].index).to.equal(options[1].index);
        expect(VM.options[2].index).to.equal(options[2].index);
        expect(VM.options[3].index).to.equal(options[3].index);
        expect(VM.options[0].class).to.equal(options[0].class);
        expect(VM.options[1].class).to.equal(options[1].class);
        expect(VM.options[2].class).to.equal(options[2].class);
        expect(VM.options[3].class).to.equal(options[3].class);
        expect(VM.options[0].title).to.equal(options[0].title);
        expect(VM.options[1].title).to.equal(options[1].title);
        expect(VM.options[2].title).to.equal(options[2].title);
        expect(VM.options[3].title).to.equal(options[3].title);
    });

 

});
