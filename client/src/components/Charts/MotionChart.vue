<template>
    <v-card :loading="loading" align="center" height="100%">
        <v-card-title class="justify-center pb-0">Motion</v-card-title>
        <apexchart
            height="280px"
            type="area"
            :options="chartOptions"
            ref="motionChart"
            :series="series"
        />
    </v-card>
</template>

<script lang="ts">
/* eslint-disable */
import { Vue } from 'vue-property-decorator';
import { Motion } from '../../types';

export default Vue.extend({
    props: {
        initialData: {
            type: Array,
        },
    },
    data() {
        return {
            loading: false,
            motionData: [],
            timestamps: [],
            series: [
                {
                    name: 'Motion',
                    data: [],
                },
            ],
            chartOptions: {
                yaxis: {
                    title: {
                        text: 'Motion',
                    },
                    max: 100,
                    min: 0,
                },
                xaxis: {
                    title: {
                        text: 'Time',
                    },
                },
                chart: {
                    id: 'area-datetime',
                    type: 'area',
                    height: 350,
                    zoom: {
                        enabled: false,
                    },
                    animations: {
                        enabled: true,
                        easing: 'linear',
                        dynamicAnimation: {
                            speed: 1000,
                        },
                    },
                    stroke: {
                        curve: 'smooth',
                    },
                    title: {
                        text: 'Dynamic Updating Chart',
                        align: 'left',
                    },
                    markers: {
                        size: 0,
                    },
                },
            },
            selection: 'one_year',
        };
    },
    methods: {
        updateChart() {
            // @ts-ignore
            this.$refs.motionChart.updateSeries([
                {
                    data: this.$data.motionData,
                },
            ]);
            // @ts-ignore
            this.$refs.motionChart.updateOptions({
                xaxis: {
                    categories: this.$data.timestamps,
                },
            });
        },
    },
    watch: {
        /* eslint-disable */
        motionData: function() {
            this.updateChart();
        },
    },

    mounted() {
        this.initialData.forEach((element: any) => {
            // @ts-ignore
            this.motionData.push(element.value);
            const [t, _] = new Date(element.timestamp).toTimeString().split(' ');
            // @ts-ignore
            this.timestamps.push(t);
        });
        this.updateChart();
    },

    sockets: {
        motion(data: string) {
            const message: Motion = JSON.parse(data);
            const value = message.value.toFixed(2);
            const [timestamp, _] = new Date(message.at).toTimeString().split(' ');
            if (this.$data.motionData.length > 9) {
                this.$data.motionData.shift();
                this.$data.timestamps.shift();
            }
            this.$data.motionData.push(value);
            this.$data.timestamps.push(timestamp);
        },
    },
});
</script>
