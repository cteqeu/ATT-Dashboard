<template>
    <grid-layout
        :col-num="12"
        :is-draggable="true"
        :is-resizable="false"
        :layout="layout"
        :row-height="30"
        :use-css-transforms="true"
        :vertical-compact="true"
    >
        <grid-item
            v-for="(item, i) in layout"
            :key="i"
            :h="item.h"
            :i="item.i"
            :static="item.static"
            :w="item.w"
            :x="item.x"
            :y="item.y"
        >
            <v-card align="center" height="100%">
                <TempChart v-if="item.type === 'temperature'"/>
                <PressureChart v-else-if="item.type === 'pressure'"/>
                <AirqualityChart v-else-if="item.type === 'airquality'"/>
                <HumidityChart v-else-if="item.type === 'humidity'" />
            </v-card>
        </grid-item>
    </grid-layout>
</template>

<script lang="ts">
import { Vue } from 'vue-property-decorator';
import { GridItem, GridLayout } from 'vue-grid-layout';
import TempChart from '../components/Charts/TempChart.vue';
import PressureChart from '../components/Charts/PressureChart.vue';
import AirqualityChart from '../components/Charts/AirqualityChart.vue';
import HumidityChart from '../components/Charts/HumidityChart.vue';

export default Vue.extend({
    components: {
        GridItem,
        GridLayout,
        TempChart,
        PressureChart,
        AirqualityChart,
        HumidityChart,
    },

    data() {
        return {
            index: 0,
            layout: [
                {
                    type: 'temperature',
                    x: 0,
                    y: 0,
                    w: 6,
                    h: 11,
                    i: '0',
                    static: false,
                },
                {
                    type: 'pressure',
                    x: 6,
                    y: 7,
                    w: 6,
                    h: 10,
                    i: '1',
                    static: false,
                },
                {
                    type: 'airquality',
                    x: 0,
                    y: 12,
                    w: 3,
                    h: 10,
                    i: '2',
                    static: false,
                },
                {
                    type: 'humidity',
                    x: 6,
                    y: 0,
                    w: 6,
                    h: 11,
                    i: '3',
                    static: false,
                },
            ],
        };
    },
});
</script>

<style lang="scss" scoped>
.vue-grid-layout {
    background: transparent;
}
.vue-grid-item {
    .resizing {
        opacity: 0.9;
    }
    .static {
        background: #cce;
    }
    .no-drag {
        height: 100%;
        width: 100%;
    }
    .minMax {
        font-size: 12px;
    }
    .add {
        cursor: pointer;
    }
}
.vue-draggable-handle {
    position: absolute;
    width: 20px;
    height: 20px;
    top: 0;
    left: 0;
    padding: 0 8px 8px 0;
    background: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='10' height='10'><circle cx='5' cy='5' r='5' fill='#999999'/></svg>")
        no-repeat bottom right;
    background-origin: content-box;
    box-sizing: border-box;
    cursor: pointer;
}
</style>
