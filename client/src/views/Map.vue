<template>
    <map-component :markers="markers" />
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import MapComponent from '@/components/MapComponent.vue';
import { Coordinate, Markers } from '@/components/Map/MapTypes.ts';

@Component({
    components: {
        MapComponent,
    },
})
export default class Map extends Vue {
    markers: Markers = [new Coordinate('hasselt', 10, 30)];
}
</script>
