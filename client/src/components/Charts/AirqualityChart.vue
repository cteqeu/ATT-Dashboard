<template>
    <div>
        <v-card-title class="justify-center pb-0">Air quality</v-card-title>

        <apexchart :height="chartSize"
            :options="chartOptions" ref="airqualityChart" :series="series"/>
    </div>
</template>

<script lang="ts">
import { Vue } from 'vue-property-decorator';

interface Airquality {
    at: string;
    value: number;
}

export default Vue.extend({
    computed: {
        chartSize: () => {
            const width = window.innerWidth;
            const height = window.innerHeight;

            const widthMain = width - 256;

            const widthAirQuality = ((widthMain - 24) / 4);
            const heightAirQuality = 340 - 20;

            if (widthAirQuality > heightAirQuality) {
                return `${heightAirQuality}px`;
            }
            return `${widthAirQuality}px`;
        },
    },
    data() {
        return {
            // Max, Curr, Min
            series: [0, 0, 100],
            chartOptions: {
                chart: {
                    type: 'radialBar',
                },
                plotOptions: {
                    radialBar: {
                        dataLabels: {
                            name: {
                                fontSize: '22px',
                            },
                            value: {
                                fontSize: '16px',
                            },
                            total: {
                                show: true,
                                label: 'Live - Air quality',
                                formatter: (w: any) => w.globals.series[1],
                            },
                        },
                    },
                },
                labels: ['Max 24h', 'Current', 'Min 24h'],
            },
        };
    },

    sockets: {
        airquality(data: string) {
            const message: Airquality = JSON.parse(data);
            const value = Number(message.value.toFixed(2));
            this.$data.series.splice(1, 1, value);
            if (value <= this.$data.series[2]) {
                this.$data.series.splice(2, 1, value);
            } else if (value >= this.$data.series[0]) {
                this.$data.series.splice(0, 1, value);
            }
        },
    },
});
</script>
