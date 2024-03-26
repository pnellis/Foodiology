<template>
    <div class="flex min-h-screen">
      <!-- Left Side: Form Area -->
      <div class="flex-1 flex flex-col grid-cols-2 px-5 py-5">
        <div class="max-w-md w-full mx-auto">
          <h2 class="text-3xl font-bold text-center mb-4">Log in to your Foodiology Account</h2>
          <h2 class="text text-center mb-2">Start Exploring Recipes Today!</h2>
          <div class="text-center mt-2">
            Not a member? 
            <RouterLink to="/signup" class="text-pink-600">Create an Account Today!</RouterLink>
          </div>
  
          <div class="mt-8">
            <form @submit.prevent="submitForm">
              <div class="space-y-6">
                <input v-model="form.email" type="email" placeholder="Email address" class="w-full px-5 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent" required>
                <input v-model="form.password" type="password" placeholder="Password" class="w-full px-5 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent" required>
                <div class="flex items-center justify-between">
                  <div class="flex items-center">
                    <input id="remember_me" type="checkbox" class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded">
                    <label for="remember_me" class="ml-2 block text-sm text-gray-900"> Remember me </label>
                  </div>
                  <div class="text-sm">
                    <a href="#" class="font-medium text-pink-600 hover:text-pink-700"> Forgot your password? </a>
                  </div>
                </div>
                <button class="w-full py-3 bg-pink-600 text-white rounded-lg hover:bg-pink-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50">Sign in</button>
              </div>
            </form>
          </div>
        </div>
      </div>
  
      <!-- Right Side: Image Area -->
      <div class="flex-1 hidden lg:block">
        <img class="object-cover w-full h-full" src="@/assets/HomePhoto.jpg" alt="Workspace">
      </div>
    </div>
  </template>


<script>
import axios from 'axios'

import { useUserStore } from '@/stores/user'

export default {
    setup() {
        const userStore = useUserStore()

        return {
            userStore
        }
    },

    data() {
        return {
            form: {
                email: '',
                password: '',
            },
            errors: []
        }
    },
    methods: {
        async submitForm() {
            this.errors = []

            if (this.form.email === '') {
                this.errors.push('Your e-mail is missing')
            }

            if (this.form.password === '') {
                this.errors.push('Your password is missing')
            }

            if (this.errors.length === 0) {
                await axios
                    .post('/api/login/', this.form)
                    .then(response => {
                        this.userStore.setToken(response.data)

                        console.log(response.data.access)

                        axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access;
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
                
                await axios
                    .get('/api/me/')
                    .then(response => {
                        this.userStore.setUserInfo(response.data)

                        this.$router.push('/feed')
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
            }
        }
    }
}
</script>

