<template>
    <grid-layout
        :col-num="12"
        :is-draggable="true"
        :is-resizable="false"
        :layout="layout"
        :row-height="40"
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
            <v-card :loading="!isActive" align="center" height="100%">
                <TempChart v-if="item.type === 'temperature' && isActive"/>
                <PressureChart v-else-if="item.type === 'pressure' && isActive"/>
                <AirqualityChart v-else-if="item.type === 'airquality' && isActive"/>
                <HumidityChart v-else-if="item.type === 'humidity' && isActive" />
                <LightChart v-else-if="item.type === 'light' && isActive" />
                <LoudnessChart v-else-if="item.type === 'loudness' && isActive" />
                <MotionChart v-else-if="item.type === 'motion' && isActive" />
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
import LightChart from '../components/Charts/LightChart.vue';
import LoudnessChart from '../components/Charts/LoudnessChart.vue';
import MotionChart from '../components/Charts/MotionChart.vue';

export default Vue.extend({
    components: {
        GridItem,
        GridLayout,
        TempChart,
        PressureChart,
        AirqualityChart,
        HumidityChart,
        LightChart,
        LoudnessChart,
        MotionChart,
    },

    mounted() {
        setTimeout(() => {
            this.isActive = true;
        }, 1000);
    },

    data() {
        return {
            isActive: false,
            index: 0,
            layout: [
                {
                    type: 'temperature',
                    x: 0,
                    y: 0,
                    w: 6,
                    h: 7,
                    i: '0',
                    static: false,
                },
                {
                    type: 'pressure',
                    x: 3,
                    y: 7,
                    w: 6,
                    h: 7,
                    i: '1',
                    static: false,
                },
                {
                    type: 'airquality',
                    x: 0,
                    y: 12,
                    w: 3,
                    h: 7,
                    i: '2',
                    static: false,
                },
                {
                    type: 'humidity',
                    x: 6,
                    y: 0,
                    w: 6,
                    h: 7,
                    i: '3',
                    static: false,
                },
                {
                    type: 'loudness',
                    x: 9,
                    y: 7,
                    w: 3,
                    h: 7,
                    i: '4',
                    static: false,
                },
                {
                    type: 'light',
                    x: 0,
                    y: 13,
                    w: 6,
                    h: 7,
                    i: '5',
                    static: false,
                },
                {
                    type: 'motion',
                    x: 6,
                    y: 13,
                    w: 6,
                    h: 7,
                    i: '6',
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
