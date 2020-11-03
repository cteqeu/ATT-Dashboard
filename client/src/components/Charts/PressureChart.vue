<template>
    <div>
        <v-card-title class="justify-center pb-0">Pressure</v-card-title>
        <apexchart height="280px" :options="chartOptions" ref="pressureChart" :series="series" />
    </div>
</template>

<script lang="ts">
import { Vue } from 'vue-property-decorator';

interface Pressure {
    at: string;
    value: number;
}

export default Vue.extend({
    data() {
        return {
            pressureData: [],
            timestamps: [],
            series: [
                {
                    name: 'Pressure',
                    data: [],
                },
            ],
            chartOptions: {
                chart: {
                    type: 'bar',
                    height: 350,
                },
                plotOptions: {
                    bar: {
                        colors: {
                            ranges: [
                                {
                                    from: 0,
                                    to: 5,
                                    color: '#F15B46',
                                },
                                {
                                    from: -5,
                                    to: 0,
                                    color: '#FEB019',
                                },
                            ],
                        },
                        columnWidth: '60px',
                    },
                },
                dataLabels: {
                    enabled: false,
                },
                yaxis: {
                    title: {
                        text: 'Percentage',
                    },
                    min: -5,
                    max: 5,
                    labels: {
                        /* eslint-disable */
                        formatter: function(y: any) {
                            return y.toFixed(2) + '%';
                        },
                    },
                },
                tooltip: {
                    y: {
                        formatter: (val: any) => (val / 100) * 1013.25 + 1013.25,
                    },
                },
                xaxis: {
                    title: {
                        text: 'Time',
                    },
                    categories: [],
                    labels: {
                        rotate: -90,
                    },
                },
            },
        };
    },

    methods: {
        updateChart() {
            this.$refs.pressureChart.updateSeries([
                {
                    data: this.$data.pressureData,
                },
            ]);

            this.$refs.pressureChart.updateOptions({
                xaxis: {
                    categories: this.$data.timestamps,
                },
            });
        },
    },
    watch: {
        /* eslint-disable */
        pressureData: function() {
            this.updateChart();
        },
    },
    sockets: {
        pressure(data: string) {
            const message: Pressure = JSON.parse(data);
            const value: number = Number(message.value.toFixed(2));
            const [timestamp, _] = new Date(message.at).toTimeString().split(' ');
            if (this.$data.pressureData.length > 9) {
                this.$data.pressureData.shift();
                this.$data.timestamps.shift();
            }
            this.$data.pressureData.push(((value - 1013.25) / 1013.25) * 100);
            this.$data.timestamps.push(timestamp);
        },
    },
});
</script>
