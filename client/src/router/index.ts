import Vue from 'vue';
import VueRouter, { RouteConfig } from 'vue-router';

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
    {
        path: '/',
        name: 'Charts',
        component: () => import(/* webpackChunkName: "charts" */ '../views/Charts.vue'),
    },
    {
        path: '/map',
        name: 'Map',
        component: () => import(/* webpackChunkName: "map" */ '../views/Map.vue'),
    },
    {
        path: '/att',
        name: 'Att',
        component: () => import(/* webpackChunkName: "att" */ '../views/Att.vue'),
    },
    {
        path: '/settings',
        name: 'Settings',
        component: () => import(/* webpackChunkName: "settings" */ '../views/Settings.vue'),
    },
    {
        path: '/login',
        name: 'Login',
        component: () => import(/* webpackChunkName: "settings" */ '../views/Login.vue'),
    },
    {
        path: '/register',
        name: 'Register',
        component: () => import(/* webpackChunkName: "settings" */ '../views/Register.vue'),
    },
];

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes,
});

export default router;
