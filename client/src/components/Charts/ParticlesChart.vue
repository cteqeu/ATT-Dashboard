<template>
    <v-card :loading="loading" align="center" height="100%">
        <v-card-title class="justify-center pb-0">Particles</v-card-title>
        <apexchart
            ref="particlesChart"
            type="line"
            height="350"
            :options="chartOptions"
            :series="series"
        ></apexchart>
    </v-card>
</template>

<script lang="ts">
import { Vue } from 'vue-property-decorator';
import { Particles } from '../../types';

/* eslint-disable */
export default Vue.extend({
    data() {
        return {
            loading: false,
            pm1: [],
            pm10: [],
            pm25: [],
            timestamps: [],
            series: [
                {
                    name: 'pm1',
                    data: [],
                },
                {
                    name: 'pm10',
                    data: [],
                },
                {
                    name: 'pm25',
                    data: [],
                },
            ],
            chartOptions: {
                chart: {
                    height: 350,
                    type: 'line',
                    zoom: {
                        enabled: false,
                    },
                },
                dataLabels: {
                    enabled: false,
                },
                stroke: {
                    width: [5, 7, 5],
                    curve: 'straight',
                    dashArray: [0, 8, 5],
                },
                legend: {
                    tooltipHoverFormatter: (val: any, opts: any) =>
                        `${val} - ${opts.w.globals.series[opts.seriesIndex][opts.dataPointIndex]}`,
                },
                markers: {
                    size: 0,
                    hover: {
                        sizeOffset: 6,
                    },
                },
                datetimeUTC: true,
                datetimeFormatter: {
                    year: 'yyyy',
                    month: "MMM 'yy",
                    day: 'dd MMM',
                    hour: 'HH:mm',
                },
                xaxis: {
                    categories: [],
                },
                yaxis: {
                    min: 0,
                    max: 20,
                },
                grid: {
                    borderColor: '#f1f1f1',
                },
            },
        };
    },

    methods: {
        updateChart() {
            this.$refs.particlesChart.updateSeries([
                {
                    data: this.$data.pm1,
                },
                {
                    data: this.$data.pm10,
                },
                {
                    data: this.$data.pm25,
                },
            ]);

            this.$refs.particlesChart.updateOptions({
                xaxis: {
                    categories: this.$data.timestamps,
                },
            });
        },
    },
    watch: {
        /* eslint-disable */
        timestamps: function() {
            this.updateChart();
        },
    },
    sockets: {
        particles(data: Particles) {
            if (this.$data.pm1.length > 9) {
                this.$data.pm1.shift();
                this.$data.pm10.shift();
                this.$data.pm25.shift();
                this.$data.timestamps.shift();
            }

            this.$data.pm1.push(data.values.pm1);
            this.$data.pm10.push(data.values.pm10);
            this.$data.pm25.push(data.values.pm25);
            const [timestamp, _] = new Date(data.timestamp).toTimeString().split(' ');
            this.$data.timestamps.push(timestamp);
        },
    },
});
</script>
