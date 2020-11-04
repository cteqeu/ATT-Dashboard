import Vue from 'vue';
import L from 'leaflet';
import VueSocketIO from 'vue-socket.io';
import SocketIO from 'socket.io-client';
import VueApexCharts from 'vue-apexcharts';
import VuePageTransition from 'vue-page-transition';
import axios from 'axios';
import App from './App.vue';
import 'leaflet/dist/leaflet.css';
import router from './router';
import vuetify from './plugins/vuetify';

Vue.prototype.$http = axios;
Vue.prototype.$API_URL = `ws://${document.domain}:${window.location.port}`;
// Vue.prototype.$API_URL = 'http://att-dashboard.herokuapp.com/';
Vue.config.productionTip = false;

Vue.component('apexchart', VueApexCharts);

/* eslint-disable */
// @ts-ignore
delete L.Icon.Default.prototype._getIconUrl;

L.Icon.Default.mergeOptions({
    iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
    iconUrl: require('leaflet/dist/images/marker-icon.png'),
    shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
});

Vue.use(VuePageTransition);
Vue.use(
    new VueSocketIO({
        debug: false,
        connection: SocketIO(Vue.prototype.$API_URL, {
            transports: ['websocket'],
            transportOptions: {
                polling: {
                    extraHeaders: {
                        Authorization: 'cQfTjWnZr4u7x!A%D*G-KaPdSgUkXp2s',
                    },
                },
            },
        }),
    }),
);

new Vue({
    router,
    vuetify,
    render: (h) => h(App)
}).$mount('#app');
