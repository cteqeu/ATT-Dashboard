<template>
    <v-navigation-drawer app overflow permanent>
        <v-list-item class="px-2">
            <v-img
                height="85px"
                src="https://www.thethingsnetwork.org/conference/wp-content/uploads/2018/12/AllThingsTalk-1.png"
            />
        </v-list-item>

        <v-divider />

        <v-list dense nav>
            <v-list-item v-for="item in items" :key="item.title" link :to="item.link">
                <v-list-item-icon>
                    <v-icon>{{ item.icon }}</v-icon>
                </v-list-item-icon>

                <v-list-item-content>
                    <v-list-item-title>{{ item.title }}</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
        </v-list>

        <template v-slot:append>
            <v-row class="px-12 pb-5 justify-center">
                <v-img @click="openPXLWebsite" id="pxl-logo" src="../assets/logo_pxl.png" />
            </v-row>
        </template>
    </v-navigation-drawer>
</template>

<script lang="ts">
/* eslint-disable */
import { Component, Prop, Vue } from 'vue-property-decorator';
import { PropType } from 'vue';
import { NavItems } from '../types';

@Component
export default class NavigationDrawer extends Vue {
    @Prop({ required: true, type: Array as PropType<NavItems[]> })
    items!: NavItems[];

    openPXLWebsite = () => window.open('http://www.pxl.be');
}
</script>

<style lang="scss" scoped>
#pxl-logo {
    width: 80% !important;
    &:hover {
        cursor: pointer;
    }
}
</style>
