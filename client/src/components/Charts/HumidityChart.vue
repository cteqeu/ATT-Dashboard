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
import { Vue } from 'vue-property-decorator';
import { Humidity } from '../../types';

export default Vue.extend({
    data() {
        return {
            loading: false,
            humidityData: [],
            timestamps: [],
            series: [
                {
                    data: [],
                },
            ],
            chartOptions: {
                chart: {
                    type: 'area',
                    stacked: false,
                    height: 350,
                    zoom: {
                        type: 'x',
                        enabled: true,
                        autoScaleYaxis: true,
                    },
                },
                dataLabels: {
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

    created() {
        this.loading = true;
        this.$http
            .get('http://localhost:3000/api/humidity/10')
            .then((response) => {
                console.log(response.data);
                this.humidityData = response.data.map((el) => el.value.toFixed(2));
                this.timestamps = response.data.map((el) => {
                    const date = new Date(el.timestamp);
                    /* eslint-disable */
                    const dateStr =
                        ('00' + date.getHours()).slice(-2) +
                        ':' +
                        ('00' + date.getMinutes()).slice(-2) +
                        ':' +
                        ('00' + date.getSeconds()).slice(-2);

                    console.log(dateStr);
                    return dateStr;
                });
                this.updateChart();
                this.loading = false;
            })
            .catch((error) => {
                console.log(error);
            });
    },

    methods: {
        updateChart() {
            this.$refs.humidityChart.updateSeries([
                {
                    data: this.$data.humidityData,
                },
            ]);

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
