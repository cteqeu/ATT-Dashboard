<template>
    <map-component :markers="markers" />
</template>

<script lang="ts">
/* eslint-disable */
import { Vue } from 'vue-property-decorator';
import axios from 'axios';
import MapComponent from '@/components/MapComponent.vue';
import { Coordinate, Airquality } from '../types';

export default Vue.extend({
    components: {
        MapComponent,
    },
    data() {
        return {
            markers: [] as Coordinate[],
        };
    },
    created() {
        // @ts-ignore
        const URL = `${this.$REST_URL}/api/gps`;

        axios
            .get(URL)
            .then((response: any) => {
                this.markers = response.data;
            })
            .catch((error: any) => {
                console.error(error.message);
            });
    },
    methods: {
        log(values: any) {
            this.markers.push(
                new Coordinate(
                    values.altitude,
                    values.latitude,
                    values.longitude,
                    values.pm1,
                    values.pm10,
                    values.pm25,
                ),
            );
        },
    },
    sockets: {
        gps(data: string) {
            const jsonString = data.substring(1, data.length - 1);

            const message = JSON.parse(jsonString);
            console.log(message);
            // eslint-disable-next-line
            // @ts-ignore
            this.log(message.value);
        },
    },
});
</script>
