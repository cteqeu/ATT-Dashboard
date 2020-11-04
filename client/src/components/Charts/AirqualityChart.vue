<template>
    <div>
        <v-card-title class="justify-center pb-0">Air quality</v-card-title>

        <apexchart :height="chartSize"
            :options="chartOptions" ref="airqualityChart" :series="series"/>
    </div>
</template>

<script lang="ts">
import { Vue } from 'vue-property-decorator';
import { Airquality } from '../../types';

export default Vue.extend({
    computed: {
        chartSize: () => {
            const width = window.innerWidth;
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
            series: [0, 0, 150],
            chartOptions: {
                chart: {
                    type: 'radialBar',
                },
                tooltip: {
                    shared: false,
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
                                /* eslint-disable */
                                formatter: (w: any) => {
                                    return (w.globals.series[1] * 1.5).toFixed();
                                },
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
            this.$data.series.splice(1, 1, (value / 1.5).toFixed(2));
            if ((value / 1.5) <= (this.$data.series[2])) {
                this.$data.series.splice(2, 1, (value / 1.5).toFixed(2));
            } else if ((value / 1.5) >= (this.$data.series[0])) {
                this.$data.series.splice(0, 1, (value / 1.5).toFixed(2));
            }
        },
    },
});
</script>
