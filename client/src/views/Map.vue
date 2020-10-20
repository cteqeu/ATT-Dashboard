<template>
    <div class="map-wrapper text-center">
        <div id="map" class="map ma-3"></div>
    </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import L from 'leaflet';

@Component({
    components: {},
})
export default class extends Vue {
    loading = false;

    map: any = '';

    tileLayer: any = '';

    layers: any = [];

    mounted() {
        this.initMap();
        this.initLayers();
    }

    /*
        https://stackoverflow.com/questions/40195136/leaflet-map-event-load-does-not-fire
    */

    private initMap() {
        this.map = L.map('map').setView([50.953245, 5.354043], 16);
        this.tileLayer = L.tileLayer(
            'https://cartodb-basemaps-{s}.global.ssl.fastly.net/rastertiles/voyager/{z}/{x}/{y}.png',
            {
                maxZoom: 17,
                attribution:
                    '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, &copy; <a href="https://carto.com/attribution">CARTO</a>',
            },
        );
    }

    private initLayers() {
        this.tileLayer.addTo(this.map);
    }
}
</script>

<style scoped>
.map-wapper {
    position: relative;
}
#map {
    position: absolute;
    top: 0;
    bottom: 0;
    right: 0;
    left: 0;
}
</style>
