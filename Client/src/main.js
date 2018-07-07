// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import Header from './components/Header'
import Footer from './components/Footer'
import router from './router'
import Element from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import store from './store'
import './permission'

Vue.use(Element)
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
	el: '#app',
	router,
	store,
	components: { App},
	template: '<App/>'
})

new Vue({
	el: '#header',
	components: {Header},
	template : '<Header/>'
})

new Vue({
	el: '#footer',
	components: {Footer},
	template: '<Footer/>'
})



