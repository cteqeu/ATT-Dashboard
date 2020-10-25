<template>
    <v-app>
        <v-app-bar app color="primary" dark>
            <v-toolbar-title>All things talk - {{ this.$route.name }}</v-toolbar-title>
        </v-app-bar>

        <v-dialog v-model="dialog" width="700">
            <v-stepper flat v-model="step" alt-labels>
                <v-stepper-header>
                    <v-stepper-step :complete="step > 1" step="1">
                        Welcome !
                    </v-stepper-step>

                    <v-divider />

                    <v-stepper-step :complete="step > 2" step="2">
                        Pick a Username
                    </v-stepper-step>

                    <v-divider />

                    <v-stepper-step :complete="step > 3" step="3">
                        Add ATT Sensor
                    </v-stepper-step>

                    <v-divider />

                    <v-stepper-step :complete="step > 4" step="4">
                        Enter device ID's
                    </v-stepper-step>

                    <v-divider />

                    <v-stepper-step step="5">
                        Complete!
                    </v-stepper-step>
                </v-stepper-header>

                <v-stepper-items>
                    <v-stepper-content step="1">
                        <v-card class="mb-12  text-center" flat height="200px">
                            <v-card-title class="justify-center ">
                                Welcome to the All things talk dashboard !
                            </v-card-title>
                            <v-card-text>
                                On this dashboard you can manually add your ATT device id, we will
                                do the rest for you.
                            </v-card-text>
                        </v-card>

                        <v-btn color="primary" @click="step = 2">
                            Continue
                        </v-btn>

                        <v-btn text>
                            Cancel
                        </v-btn>
                    </v-stepper-content>

                    <v-stepper-content step="2">
                        <v-card class="mb-12" flat height="200px">
                            <v-card-title class="justify-center "
                                >Please enter a username.
                            </v-card-title>
                            <v-card-text>
                                <v-row class="pa-0 ma-0 justify-content-center align-center">
                                    <v-col cols="3" class="pa-0 ma-0"></v-col>
                                    <v-col cols="6" class="pa-0 ma-0">
                                        <v-text-field
                                            v-model="username"
                                            :counter="10"
                                            label="Name"
                                        />
                                    </v-col>
                                </v-row>
                            </v-card-text>
                        </v-card>

                        <v-btn color="primary" @click="step = 3">
                            Continue
                        </v-btn>

                        <v-btn text>
                            Cancel
                        </v-btn>
                    </v-stepper-content>

                    <v-stepper-content step="3">
                        <v-card class="mb-12" flat height="200">
                            <v-card-title class="justify-center">
                                Add your sensors to ATT
                            </v-card-title>

                            <v-card-text class="text-center">
                                <v-row>
                                    <v-col cols="6">
                                        To add your sensors, go to
                                        <a href="https://maker.allthingstalk.com/" color="primary"
                                            >AllThingsTalk - Orange</a
                                        >.<br />You can follow the instructions from the video
                                    </v-col>

                                    <v-col cols="6">
                                        <iframe
                                            fluid
                                            width="300"
                                            height="200"
                                            src="https://www.youtube.com/embed/7EmXCyJPwS8"
                                        >
                                        </iframe
                                    ></v-col>
                                </v-row>
                            </v-card-text>
                        </v-card>

                        <v-btn color="primary" @click="step = 4">
                            Continue
                        </v-btn>

                        <v-btn text>
                            Cancel
                        </v-btn>
                    </v-stepper-content>

                    <v-stepper-content step="4">
                        <v-card class="mb-12" color="grey lighten-1" height="200px"></v-card>

                        <v-btn color="primary" @click="step = 5">
                            Continue
                        </v-btn>

                        <v-btn text>
                            Cancel
                        </v-btn>
                    </v-stepper-content>

                    <v-stepper-content step="5">
                        <v-card class="mb-12" color="grey lighten-1" height="200px"></v-card>

                        <v-btn color="primary" @click="step = 1">
                            Done!
                        </v-btn>

                        <v-btn text>
                            Cancel
                        </v-btn>
                    </v-stepper-content>
                </v-stepper-items>
            </v-stepper>
        </v-dialog>

        <v-navigation-drawer app overflow v-model="drawer" :mini-variant.sync="mini" permanent>
            <v-list-item class="px-2">
                <v-list-item-avatar>
                    <v-avatar color="primary" size="36">
                        <span class="white--text">VC</span>
                    </v-avatar>
                </v-list-item-avatar>

                <v-list-item-title>Vincent Claes</v-list-item-title>

                <v-btn icon @click.stop="mini = !mini">
                    <v-icon>mdi-chevron-left</v-icon>
                </v-btn>
            </v-list-item>

            <v-divider></v-divider>

            <v-list dense>
                <v-list-item v-for="item in items" :key="item.title" link :to="item.link">
                    <v-list-item-icon>
                        <v-icon>{{ item.icon }}</v-icon>
                    </v-list-item-icon>

                    <v-list-item-content>
                        <v-list-item-title>{{ item.title }}</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-navigation-drawer>

        <v-main>
            <v-container fluid>
                <router-view />
            </v-container>
        </v-main>
    </v-app>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component({
    components: {},
})
export default class App extends Vue {
    drawer = true;

    dialog = false;

    mini = true;

    step = 1;

    items = [
        { title: 'Charts', icon: 'mdi-poll', link: '/' },
        { title: 'Map', icon: 'mdi-map', link: '/map' },
        { title: 'Battery', icon: 'mdi-battery-70', link: '/battery' },
        { title: 'ATT - Orange', icon: 'mdi-web', link: '/att' },
        { title: 'Settings', icon: 'mdi-cog-outline', link: 'settings' },
    ];

    valid = false;

    // Form Stepper
    username = '';
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
