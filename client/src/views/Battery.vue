<template>
    <div>
        <v-row>
            <v-col cols="6">
                <v-card>
                    <v-card-title> Battery #1 </v-card-title>
                        <v-progress-linear color="light-blue"
                        height="20" value="10" striped></v-progress-linear>
                    <v-card-text> Battery indicator #1 </v-card-text>
                </v-card>
            </v-col>

            <v-col cols="6">
                <v-card>
                    <v-card-title> Battery #2 </v-card-title>
                        <v-progress-linear color="light-green darken-4"
                        height="20" value="80" striped></v-progress-linear>
                    <v-card-text> Battery indicator #2 </v-card-text>
                </v-card>
            </v-col>
        </v-row>

        <v-row>
            <v-col cols="6">
                <v-card>
                    <v-card-title> Battery #3 </v-card-title>
                        <v-progress-linear color="deep-orange"
                        height="20" value="54" striped></v-progress-linear>
                    <v-card-text> Battery indicator #3 </v-card-text>
                </v-card>
            </v-col>

            <v-col cols="6">
                <v-card>
                    <v-card-title> Battery #4 </v-card-title>
                        <v-progress-linear color="lime"
                        height="20" value="23" striped></v-progress-linear>
                    <v-card-text> Battery indicator #4 </v-card-text>
                </v-card>
            </v-col>
        </v-row>
        {{temperatureF}}
    </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import App from 'vue';

@Component<App>({
    data() {
        return {
            temperatureF: [],
        };
    },
    sockets: {
        connect() {
            console.log('connected');
        },

        temperature(data: any) {
            this.$data.temperatureF.push(data.data);
        },
    },
})

export default class Battery extends Vue {

}
</script>
