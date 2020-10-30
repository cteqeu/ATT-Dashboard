<template>
    <v-navigation-drawer app overflow permanent>
        <v-list-item class="px-2">
            <v-list-item-avatar>
                <v-avatar color="primary" size="36">
                    <span class="white--text">{{ initials }}</span>
                </v-avatar>
            </v-list-item-avatar>

            <v-list-item-title>{{ username }}</v-list-item-title>
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
import { Component, Prop, Vue } from 'vue-property-decorator';
import { PropType } from 'vue';
import { NavItems } from '../types';

@Component
export default class NavigationDrawer extends Vue {
    @Prop({ required: true, type: String })
    name = '';

    @Prop({ required: true, type: Array as PropType<NavItems[]> })
    items!: NavItems[];

    openPXLWebsite = () => window.open('http://www.pxl.be');

    get username() {
        return this.name;
    }

    private get initials(): string {
        // Function used to get initials : https://stackoverflow.com/questions/33076177/getting-name-initials-using-js
        const n = this.name.split(' ');
        if (n.length === 1) return `${n[0].charAt(0)}`;
        return `${n[0].charAt(0)}${n[n.length - 1].charAt(0)}`;
    }
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
