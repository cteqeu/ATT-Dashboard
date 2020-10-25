<template>
  <div>
    <v-row>
        <v-col cols="6">
            <v-card>
                <v-title> Battery #1 </v-title>
                    <v-progress-linear color="light-blue"
                    height="20" value="10" striped></v-progress-linear>
                <v-text> Battery indicator #1 </v-text>
            </v-card>
        </v-col>

        <v-col cols="6">
            <v-card>
                <v-title> Battery #2 </v-title>
                    <v-progress-linear color="light-green darken-4"
                    height="20" value="80" striped></v-progress-linear>
                <v-text> Battery indicator #2 </v-text>
            </v-card>
        </v-col>
    </v-row>

    <v-row>
        <v-col cols="6">
            <v-card>
                <v-title> Battery #3 </v-title>
                    <v-progress-linear color="deep-orange"
                    height="20" value="54" striped></v-progress-linear>
                <v-text> Battery indicator #3 </v-text>
            </v-card>
        </v-col>

        <v-col cols="6">
            <v-card>
                <v-title> Battery #4 </v-title>
                    <v-progress-linear color="lime"
                    height="20" value="23" striped></v-progress-linear>
                <v-text> Battery indicator #4 </v-text>
            </v-card>
        </v-col>
    </v-row>
  </div>
</template>
