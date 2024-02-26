import { createRouter, createWebHashHistory } from 'vue-router';
import Home from '@/views/Home.vue';
import Login from '@/views/Login.vue';
import CreateAccount from '@/views/CreateAccount.vue';
import AboutUs from '@/views/AboutUs.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/create-account',
    name: 'CreateAccount',
    component: CreateAccount
  },
  {
    path: '/AboutUs',
    name: 'AboutUs',
    component: AboutUs
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes
});

export default router;