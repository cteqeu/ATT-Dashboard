import Vue from 'vue';
import L from 'leaflet';
import VueSocketIO from 'vue-socket.io';
import SocketIO from 'socket.io-client';
import VueApexCharts from 'vue-apexcharts';
import App from './App.vue';
// Import the whole Leaflet CSS
import 'leaflet/dist/leaflet.css';
import router from './router';
import vuetify from './plugins/vuetify';

/* eslint-disable */
// @ts-ignore
delete L.Icon.Default.prototype._getIconUrl;

L.Icon.Default.mergeOptions({
    iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
    iconUrl: require('leaflet/dist/images/marker-icon.png'),
    shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
});

Vue.component('apexchart', VueApexCharts);
Vue.use(new VueSocketIO({
    debug: true,
    connection: SocketIO('http://localhost:5000', {
        transportOptions: {
            polling: {
                extraHeaders: {
                  Authorization: 'cQfTjWnZr4u7x!A%D*G-KaPdSgUkXp2s'
                }
              }
        }
    }), //options object is Optional
  })
);

Vue.config.productionTip = false;

new Vue({
    router,
    vuetify,
    render: (h) => h(App),
}).$mount('#app');
