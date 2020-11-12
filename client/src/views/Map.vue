<template>
    <map-component :markers="markers" />
</template>

<script lang="ts">
import { Vue } from 'vue-property-decorator';
import MapComponent from '@/components/MapComponent.vue';
import { Coordinate, Airquality } from '../types';

export default Vue.extend({
    components: {
        MapComponent,
    },
    data() {
        return {
            markers: [] as Coordinate[],
            airqualityData: Number,
        };
    },
    mounted() {
        this.markers.push(new Coordinate(20, 50, 5, 10));
    },
    methods: {
        log(values: any) {
            this.$data.markers.push(
                new Coordinate(
                    values.altitude,
                    values.latitude,
                    values.longitude,
                    this.$data.airquality,
                ),
            );
        },
    },
    sockets: {
        airquality(data: string) {
            const message: Airquality = JSON.parse(data);
            const value = Number(message.value.toFixed(2));
            this.$data.airquality = value;
        },
        gps(data: string) {
            const message = JSON.parse(data);
            // eslint-disable-next-line
            // @ts-ignore
            this.log(message.value);
        },
    },
});
</script>
