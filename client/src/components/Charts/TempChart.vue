<template>
    <v-card :loading="loading" align="center" height="100%">
        <v-card-title class="justify-center pb-0">Temperature</v-card-title>
        <apexchart
            height="280px"
            type="area"
            :options="chartOptions"
            ref="temperatureChart"
            :series="series"
        />
    </v-card>
</template>

<script lang="ts">
import { Vue } from 'vue-property-decorator';
import { Temperature } from '../../types';

export default Vue.extend({
    data() {
        return {
            loading: false,
            temperatureData: [],
            timestamps: [],
            series: [
                {
                    data: [],
                },
            ],
            chartOptions: {
                yaxis: {
                    title: {
                        text: 'Temperature',
                    },
                    max: 50,
                    min: -20,
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
    created() {
        this.loading = true;
        this.$http
            .get('http://localhost:3000/api/temperature/10')
            .then((response) => {
                console.log(response.data);
                this.temperatureData = response.data.map((el) => el.value.toFixed(2));
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
            this.$refs.temperatureChart.updateSeries([
                {
                    data: this.$data.temperatureData,
                },
            ]);
            this.$refs.temperatureChart.updateOptions({
                xaxis: {
                    categories: this.$data.timestamps,
                },
            });
        },
    },
    watch: {
        /* eslint-disable */
        temperatureData: function() {
            this.updateChart();
        },
    },
    sockets: {
        temperature(data: string) {
            const message: Temperature = JSON.parse(data);
            const value = message.value.toFixed(2);
            const [timestamp, _] = new Date(message.at).toTimeString().split(' ');
            if (this.$data.temperatureData.length > 9) {
                this.$data.temperatureData.shift();
                this.$data.timestamps.shift();
            }
            this.$data.temperatureData.push(value);
            this.$data.timestamps.push(timestamp);
        },
    },
});
</script>
