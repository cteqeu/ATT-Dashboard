<template>
    <div id="chart">
        <div id="chart-timeline">
            <apexchart
                type="area"
                height="350"
                :options="chartOptions"
                ref="humidityChart"
                :series="series"
            />
        </div>
    </div>
</template>

<script lang="ts">
import { Vue } from 'vue-property-decorator';

interface Humidity {
    at: string;
    value: number;
}

export default Vue.extend({
    data() {
        return {
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
                    toolbar: {
                        autoSelected: 'zoom',
                    },
                },
                dataLabels: {
                    enabled: false,
                },
                markers: {
                    size: 0,
                },
                title: {
                    text: 'Stock Price Movement',
                    align: 'left',
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
                    labels: {
                        formatter: (val: any) => (val).toFixed(0),
                    },
                    title: {
                        text: 'Price',
                    },
                },
                tooltip: {
                    shared: false,
                    y: {
                        formatter: (val: any) => (val).toFixed(0),
                    },
                },
            },
        };
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
