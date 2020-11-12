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
import { Vue } from 'vue-property-decorator';
import { Motion } from '../../types';

export default Vue.extend({
    data() {
        return {
            loading: false,
            motionData: [],
            timestamps: [],
            series: [
                {
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
                    legend: {
                        show: false,
                    },
                },
            },
            selection: 'one_year',
        };
    },
    methods: {
        updateChart() {
            this.$refs.motionChart.updateSeries([
                {
                    data: this.$data.motionData,
                },
            ]);
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
