<template>
    <map-component :markers="markers" />
</template>

<script lang="ts">
import { Vue } from 'vue-property-decorator';
import MapComponent from '@/components/MapComponent.vue';
import { Coordinate } from '../types';

export default Vue.extend({
    components: {
        MapComponent,
    },
    data() {
        return {
            markers: [] as Coordinate[],
        };
    },
    sockets: {
        gps(data: string) {
            const message = JSON.parse(data);
            const values = message.value;

            this.$data.markers.push(
                new Coordinate(values.altitude, values.latitude, values.longitude),
            );
        },
    },
});
</script>
