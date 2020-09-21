import Vue from "vue";
import ElementUI from "element-ui";
import "element-ui/lib/theme-chalk/index.css";
import App from "./App.vue";

Vue.use(ElementUI);
Vue.config.productionTip = false;

export const eventEmitter = new Vue();

new Vue({
  render: function(h) {
    return h(App);
  }
}).$mount("#app");
