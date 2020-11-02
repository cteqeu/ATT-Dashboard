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
            markers: [],
        };
    },

    mounted() {
        this.markers.push(new Coordinate('PXL', 50.953245, 5.354043));
        this.markers.push(new Coordinate('PXHell', 50.95175, 5.35055));
    },

    sockets: {
        gps(data: string) {
            const message = JSON.parse(data);
            const values = message.value;
            this.markers.push(new Coordinate(values.altitude, values.latitude, values.longitude));
        },
    },
});
</script>
