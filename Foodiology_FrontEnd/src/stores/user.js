import { defineStore } from 'pinia'
import axios from 'axios'

export const useUserStore = defineStore({
    id: 'user',

    state: () => ({
        user: {
            isAuthenticated: false,
            id: null,
            name: null,
            email: null,
            access: null,
            refresh: null,
            avatar: null
        }
    }),

    actions: {
        async initStore() {
            console.log('initStore');

            if (localStorage.getItem('user.refresh')) {
                console.log('Attempting to restore session');

                await this.refreshToken(); // Validate refresh token and update access token

                this.user.id = localStorage.getItem('user.id');
                this.user.name = localStorage.getItem('user.name');
                this.user.email = localStorage.getItem('user.email');
                this.user.avatar = localStorage.getItem('user.avatar');
                this.user.isAuthenticated = true;

                console.log('Session restored:', this.user);
            } else {
                console.log('No session to restore');
            }
        },

        setToken(data) {
            console.log('setToken', data)

            this.user.access = data.access
            this.user.refresh = data.refresh
            this.user.isAuthenticated = true

            localStorage.setItem('user.access', data.access)
            localStorage.setItem('user.refresh', data.refresh)

            console.log('user.access: ', localStorage.getItem('user.access'))
        },

        removeToken() {
            console.log('removeToken')

            this.user.refresh = null
            this.user.access = null
            this.user.isAuthenticated = false
            this.user.id = false
            this.user.name = false
            this.user.email = false
            this.user.avatar = null

            localStorage.setItem('user.access', '')
            localStorage.setItem('user.refresh', '')
            localStorage.setItem('user.id', '')
            localStorage.setItem('user.name', '')
            localStorage.setItem('user.email', '')
             localStorage.setItem('user.avatar', '')
        },

        setUserInfo(user) {
            console.log('setUserInfo', user)

            this.user.id = user.id
            this.user.name = user.name
            this.user.email = user.email
            this.user.avatar = user.avatar

            localStorage.setItem('user.id', this.user.id)
            localStorage.setItem('user.name', this.user.name)
            localStorage.setItem('user.email', this.user.email)
            localStorage.setItem('user.avatar', this.user.avatar)

            console.log('User', this.user)
        },

        refreshToken() {
            axios.post('/api/account/refresh/', {
                refresh: this.user.refresh
            })
                .then((response) => {
                    this.user.access = response.data.access

                    localStorage.setItem('user.access', response.data.access)

                    axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access
                })
                .catch((error)=>{
                    console.log(error)

                    this.removeToken()
                })
        },
    }
})