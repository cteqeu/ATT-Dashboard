// frontend\src\plugins\connectionBuilder.js
// Author: Author : Andre Baldo (http://github.com/andrebaldo/)
/* eslint-disable */
import axios from 'axios';

const axiosInstance = axios.create({
    baseURL: 'http://localhost:5000',
});

if (sessionStorage.loginToken) {
    axiosInstance.defaults.headers.common['Authorization'] = sessionStorage.loginToken;
}

export default axiosInstance;
