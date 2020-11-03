<template>
    <div>
        <v-card-title class="justify-center pb-0">Temperature</v-card-title>
        <apexchart height="130%" type="area"
            :options="chartOptions" ref="temperatureChart" :series="series" />
    </div>

</template>

<script lang="ts">
import { Vue } from 'vue-property-decorator';

interface Temperature {
    at: string;
    value: number;
}
export default Vue.extend({
    data() {
        return {
            temperatureData: [],
            timestamps: [],
            series: [
                {
                    data: [],
                },
            ],
            chartOptions: {
                // title: {
                //     text: 'Temperature',
                //     align: 'center',
                //     margin: 50,
                //     style: {
                //         fontSize: '18px',
                //     },
                // },
                yaxis: {
                    max: 50,
                    min: -20,
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
                    toolbar: {
                        show: false,
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
