<template>
    <v-card>
        <v-card-title primary-title>
            <h1>Register</h1>
        </v-card-title>
        <v-card-text>
            <v-form rounded v-model="isRegisterFormValid">
                <v-text-field
                    name="email"
                    label="Email*"
                    id="email"
                    v-model="email"
                    required
                    type="email"
                />

                <v-text-field
                    name="password"
                    label="Password*"
                    id="password"
                    v-model="password"
                    counter="50"
                    required
                />

                <div class="text-center">
                    <v-progress-circular indeterminate color="primary" v-if="isProcessing" />
                </div>
            </v-form>
        </v-card-text>
        <v-card-actions>
            <router-link to="login">Go to login</router-link>
            <v-spacer />
            <v-btn
                color="success"
                :disabled="!isRegisterFormValid || isProcessing"
                @click="registerNewUser({ email: email, password: password })"
            >
                <v-icon left>mdi-account-plus</v-icon>Register
            </v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
import Vue from 'vue';
import { mapActions, mapGetters } from 'vuex';

export default Vue.extend({
    name: 'Register',
    data() {
        return {
            isRegisterFormValid: false,
            email: '',
            password: '',
        };
    },

    methods: {
        ...mapActions(['registerNewUser']),
    },
    computed: {
        ...mapGetters([
            'getIsRegistrationProcessSucceed',
            'getRegistrationProcessMessage',
            'isProcessing',
        ]),
    },
});
</script>
