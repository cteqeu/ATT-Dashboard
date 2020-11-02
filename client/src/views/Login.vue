<template>
    <v-container>
        <r-row>
            <v-col cols="10">
                <v-card>
                    <v-title>Login</v-title>
                    <v-form>
                        <v-text-field label="E-mail"></v-text-field>
                        <v-text-field label="Password"></v-text-field>
                        <v-btn type="submit">Login</v-btn>
                    </v-form>
                    <v-subtitle><v-btn>Not registered yet?</v-btn></v-subtitle>
                </v-card>
            </v-col>
        </r-row>
    </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component
export default class Login extends Vue {}
</script>

<style scoped></style>
