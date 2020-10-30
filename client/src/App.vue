<template>
    <v-app>
        <v-app-bar app color="primary" dark>
            <v-toolbar-title>All things talk - {{ this.$route.name }}</v-toolbar-title>
        </v-app-bar>

        <navigation-drawer name="Vincent Cleas" :items="items" />

        <intro-stepper />

        <Offline @detected-condition="handleConnectivityChange" />

        <v-snackbar v-model="onlineStatus" bottom color="red" text timeout="-1">
            You are disconnected.
        </v-snackbar>

        <v-main>
            <v-container fluid>
                <vue-page-transition name="fade">
                    <router-view />
                </vue-page-transition>
            </v-container>
        </v-main>
    </v-app>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Offline from 'v-offline';
import { NavItems } from './types';
import NavigationDrawer from './components/NavigationDrawer.vue';
import IntroStepper from './components/IntroStepper.vue';

@Component({
    components: {
        NavigationDrawer,
        IntroStepper,
        Offline,
    },
})
export default class App extends Vue {
    items: NavItems[] = [
        { title: 'Charts', icon: 'mdi-poll', link: '/' },
        { title: 'Map', icon: 'mdi-map', link: '/map' },
        { title: 'Battery', icon: 'mdi-battery-70', link: '/battery' },
        { title: 'ATT - Orange', icon: 'mdi-web', link: '/att' },
        { title: 'Settings', icon: 'mdi-cog-outline', link: 'settings' },
    ];

    onlineStatus = false;

    handleConnectivityChange(status: boolean) {
        if (!status) {
            this.onlineStatus = true;
        } else {
            this.onlineStatus = false;
        }
    }
}
</script>

<style lang="scss">
body {
    padding: 0;
    margin: 0;
}
html,
body {
    height: 100%;
    width: 100%;
}
</style>
