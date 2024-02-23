import { createRouter, createWebHashHistory } from 'vue-router';
import Home from '@/views/Home.vue';
import Login from '@/views/Login.vue';
import CreateAccount from '@/views/CreateAccount.vue';

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
];

const router = createRouter({
  history: createWebHashHistory(),
  routes
});

export default router;