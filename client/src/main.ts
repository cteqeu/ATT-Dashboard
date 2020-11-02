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
import store from './store';

Vue.prototype.$http = axios;

/* eslint-disable */
// @ts-ignore
delete L.Icon.Default.prototype._getIconUrl;

L.Icon.Default.mergeOptions({
    iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
    iconUrl: require('leaflet/dist/images/marker-icon.png'),
    shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
});

Vue.use(VuePageTransition);

Vue.component('apexchart', VueApexCharts);
Vue.use(
    new VueSocketIO({
        debug: true,
        connection: SocketIO('http://localhost:5000', {
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

Vue.config.productionTip = false;

new Vue({
    router,
    vuetify,
    store,
    render: (h) => h(App)
}).$mount('#app');
