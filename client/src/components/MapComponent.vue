<template>
    <div class="map-wrapper">
        {{ markers }}
        <!-- <l-map id="map" :zoom="zoom" :center="center" :options="mapOptions">
            <l-tile-layer :url="url" :attribution="attribution" />
        </l-map> -->
    </div>
</template>

<script lang="ts">
import { Prop, Vue } from 'vue-property-decorator';
import { latLng } from 'leaflet';
import { PropType } from 'vue';
/* eslint-disable */
import { LMap, LTileLayer, LMarker, LPopup, LTooltip } from 'vue2-leaflet';
/* eslint-enable */
import { Markers } from '@/components/Map/MapTypes.ts';

export default class MapCompontent extends Vue {
    // Props
    @Prop({ required: true, type: Array as PropType<Markers> })
    public readonly markers!: Markers;

    // Data
    showMap = false;

    zoom = 16;

    center = latLng(50.953245, 5.354043);

    url = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';

    attribution = '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors';

    mapOptions = {
        zoomSnap: 0.5,
    };
}
</script>

<style scoped>
.map-wapper {
    position: relative;
    width: 100%;
}
#map {
    height: 100%;
    z-index: 0;
    position: absolute;
    top: 0;
    bottom: 0;
    right: 0;
    left: 0;
}
</style>
