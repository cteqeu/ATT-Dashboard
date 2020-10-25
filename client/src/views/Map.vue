<template>
    <map-component :markers="markers" />
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import MapComponent from '@/components/MapComponent.vue';
import { Coordinate } from '../components/Map/MapTypes';

@Component({
    components: {
        MapComponent,
    },
})
export default class Map extends Vue {
    markers: Coordinate[] = new Array<Coordinate>();

    mounted() {
        this.markers.push(new Coordinate('PXL', 20, 20));
    }
}
</script>
