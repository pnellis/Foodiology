import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import './assets/base.css';
import './assets/main.css';

const app = createApp(App);
app.use(router);
app.mount('#app');


// import './assets/main.css'
// import 'bootstrap/dist/css/bootstrap.css'
// import bootstrap from 'bootstrap/dist/js/bootstrap.bundle.js'
// createApp(App).use(bootstrap).mount('#app')
