<template>
    <v-card :loading="loading" align="center" height="100%">
        <v-card-title class="justify-center pb-0">Humidity</v-card-title>
        <apexchart
            type="area"
            height="280px"
            :options="chartOptions"
            ref="humidityChart"
            :series="series"
        />
    </v-card>
</template>

<script lang="ts">
/* eslint-disable */
import { Vue } from 'vue-property-decorator';
import { Humidity } from '../../types';

export default Vue.extend({
    props: {
        initialData: {
            type: Array,
        },
    },
    data() {
        return {
            loading: false,
            humidityData: [],
            timestamps: [],
            series: [
                {
                    name: 'Humidity',
                    data: [],
                },
            ],
            chartOptions: {
                chart: {
                    type: 'area',
                    stacked: false,
                    height: 350,
                    zoom: {
                        enabled: false,
                    },
                },
                dataLabels: {
                    enabled: true,
                },
                zoom: {
                    enabled: false,
                },
                markers: {
                    size: 0,
                },
                fill: {
                    type: 'gradient',
                    gradient: {
                        shadeIntensity: 1,
                        inverseColors: false,
                        opacityFrom: 0.5,
                        opacityTo: 0,
                        stops: [0, 90, 100],
                    },
                },
                yaxis: {
                    min: 0,
                    max: 100,
                    labels: {
                        formatter: (val: number) => val.toFixed(0),
                    },
                    title: {
                        text: 'Percentage',
                    },
                },
                xaxis: {
                    title: {
                        text: 'Time',
                    },
                },
                tooltip: {
                    shared: false,
                    y: {
                        formatter: (val: number) => val.toFixed(0),
                    },
                },
            },
        };
    },

    mounted() {
        this.initialData.forEach((element: any) => {
            // @ts-ignore
            this.humidityData.push(element.value.toFixed(2));
            const [t, _] = new Date(element.timestamp).toTimeString().split(' ');
            // @ts-ignore
            this.timestamps.push(t);
        });
        this.updateChart();
    },

    methods: {
        updateChart() {
            // @ts-ignore
            this.$refs.humidityChart.updateSeries([
                {
                    data: this.$data.humidityData,
                },
            ]);

            // @ts-ignore
            this.$refs.humidityChart.updateOptions({
                xaxis: {
                    categories: this.$data.timestamps,
                },
            });
        },
    },
    watch: {
        /* eslint-disable */
        humidityData: function() {
            this.updateChart();
        },
    },

    sockets: {
        humidity(data: string) {
            const message: Humidity = JSON.parse(data);
            const value = message.value.toFixed(2);
            const [timestamp, _] = new Date(message.at).toTimeString().split(' ');

            if (this.$data.humidityData.length > 9) {
                this.$data.humidityData.shift();
                this.$data.timestamps.shift();
            }

            this.$data.humidityData.push(value);
            this.$data.timestamps.push(timestamp);
        },
    },
});
</script>
