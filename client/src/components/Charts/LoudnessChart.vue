<template>
    <v-card :loading="loading" align="center" height="100%">
        <v-card-title class="justify-center pb-0">Loudness</v-card-title>

        <apexchart
            :height="chartSize"
            :options="chartOptions"
            ref="loudnessChart"
            :series="series"
        />
    </v-card>
</template>

<script lang="ts">
/* eslint-disable */
import { Vue } from 'vue-property-decorator';
import { Loudness } from '../../types';

export default Vue.extend({
    props: {
        initialData: {
            type: Array,
        },
    },
    computed: {
        chartSize: () => {
            const width = window.innerWidth;
            const height = window.innerHeight;

            const widthMain = width - 256;

            const widthLoudness = (widthMain - 24) / 4;
            const heightLoudness = 340 - 20;

            if (widthLoudness > heightLoudness) {
                return `${heightLoudness}px`;
            }
            return `${widthLoudness}px`;
        },
    },

    data() {
        return {
            loading: false,
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
                                label: 'Loudness (dB)',
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

    mounted() {
        this.initialData.forEach((element: any) => {
            // @ts-ignore
            this.series.push(element.value);
        });
    },

    sockets: {
        loudness(data: string) {
            const message: Loudness = JSON.parse(data);
            const value = Number(message.value.toFixed(2));
            this.$data.series.splice(1, 1, (value / 1.5).toFixed(2));
            if (value / 1.5 <= this.$data.series[2]) {
                this.$data.series.splice(2, 1, (value / 1.5).toFixed(2));
            } else if (value / 1.5 >= this.$data.series[0]) {
                this.$data.series.splice(0, 1, (value / 1.5).toFixed(2));
            }
        },
    },
});
</script>
