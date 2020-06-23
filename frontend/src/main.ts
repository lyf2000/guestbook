import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/element.js'
import AXIOS from './plugins/axios.js'


Vue.config.productionTip = false

Vue.prototype.$http = AXIOS;

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
