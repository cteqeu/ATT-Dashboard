<template>
    <v-app>
        <v-app-bar app color="primary" dark>
            <v-toolbar-title>{{ this.$route.name }}</v-toolbar-title>
            <v-spacer />
            <v-btn v-if="$route.name === 'Charts'" @click="downloadCSV()" color="white" text
                >Download csv</v-btn
            >
        </v-app-bar>

        <navigation-drawer :items="items" />

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

@Component({
    components: {
        NavigationDrawer,
        Offline,
    },
})
export default class App extends Vue {
    items: NavItems[] = [
        { title: 'Charts', icon: 'mdi-poll', link: '/' },
        { title: 'Map', icon: 'mdi-map', link: '/map' },
        { title: 'ATT - Orange', icon: 'mdi-web', link: '/att' },
    ];

    onlineStatus = false;

    public downloadCSV = () => window.open('http://localhost:3000/api/download', '_blank');

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
