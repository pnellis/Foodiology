<template>
    <div class="max-w-7xl mx-auto grid grid-cols-5 gap-4">
        <div class="main-left col-span-1">
            <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
                <img :src="user.get_avatar" class="mb-6 rounded-full">

                <p><strong>{{ user.name }}</strong></p>

                <div class="mt-6 flex space-x-8 justify-around" v-if="user.id">
                    <RouterLink :to="{ name: 'friends', params: { id: user.id } }" class="text-xs text-gray-500">{{
                        user.friends_count }} friends</RouterLink>
                    <p class="text-xs text-gray-500"> {{ user.posts_count }} recipes</p>
                </div>

                <div class="mt-6">
                    <button class="inline-block py-4 px-6 bg-purple-600 text-xs text-white rounded-lg"
                        @click="sendFriendshipRequest" v-if="userStore.user.id !== user.id && can_send_friendship_request">
                        Send friendship request
                    </button>

                    <RouterLink class="inline-block mr-2 py-4 px-3 bg-pink-600 text-xs text-white rounded-lg"
                        to="/profile/edit" v-if="userStore.user.id == user.id">
                        Edit Profile
                    </RouterLink>

                    <button class="inline-block py-4 px-6 bg-red-600 text-xs text-white rounded-lg" @click="logout"
                        v-if="userStore.user.id == user.id">
                        Log Out
                    </button>

                </div>

            </div>
        </div>

        <div class="main-center col-span-2 space-y-4">
            <div class="bg-white border border-gray-200 rounded-lg" v-if="userStore.user.id === user.id">
                <form v-on:submit.prevent="submitForm" method="post">
                    <div class="p-4">
                        <textarea v-model="body" class="p-4 w-full bg-gray-100 rounded-lg"
                            placeholder="Input recipe"></textarea>
                    </div>

                    <div class="p-4 border-t border-gray-100 flex justify-between">
                        <a href="#" class="inline-block py-4 px-6 bg-gray-600 text-white rounded-lg">Attach image</a>

                        <button class="inline-block py-4 px-6 bg-pink-600 text-white rounded-lg">Post</button>
                    </div>
                </form>
            </div>

            <div class="p-4 bg-white border border-gray-200 rounded-lg" v-for="post in posts" v-bind:key="post.id">
                <FeedItem v-bind:post="post" />
            </div>

        </div>

        <div class="main-right col-span-2 space-y-4">
            <PantryComponent />
            <RecommendedRecipes />
            <TrendingRecipes />
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import RecommendedRecipes from '../components/RecommendedRecipes.vue'
import TrendingRecipes from '../components/TrendingRecipes.vue'
import FeedItem from '../components/FeedItem.vue'
import PantryComponent from '../components/PantryComponent.vue';
import { useUserStore } from '@/stores/user'
import { useToastStore } from '@/stores/toast'

export default {
    name: 'FeedView',

    setup() {
        const userStore = useUserStore()
        const toastStore = useToastStore()

        return {
            userStore,
            toastStore
        }
    },

    components: {
        RecommendedRecipes,
        TrendingRecipes,
        FeedItem,
        PantryComponent
    },

    data() {
        return {
            posts: [],
            user: {
                id: null
            },
            can_send_friendship_request: null,
            body: '',
        }
    },

    mounted() {
        this.getFeed()
    },

    watch: {
        '$route.params.id': {
            handler: function () {
                this.getFeed()
            },
            deep: true,
            immediate: true
        }
    },

    methods: {
        sendFriendshipRequest() {
            axios
                .post(`/api/friends/${this.$route.params.id}/request/`)
                .then(response => {
                    console.log('data', response.data)

                    this.can_send_friendship_request = false

                    if (response.data.message == 'request already sent') {
                        this.toastStore.showToast(5000, 'The request has already been sent!', 'bg-red-300')
                    } else {
                        this.toastStore.showToast(5000, 'The request was sent!', 'bg-emerald-300')
                    }
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        getFeed() {
            axios
                .get(`/api/posts/profile/${this.$route.params.id}/`)
                .then(response => {
                    console.log('data', response.data)

                    this.posts = response.data.posts
                    this.user = response.data.user
                    this.can_send_friendship_request = response.data.can_send_friendship_request

                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        submitForm() {
            console.log('submitForm', this.body)

            axios
                .post('/api/posts/create/', {
                    'body': this.body
                })
                .then(response => {
                    console.log('data', response.data)

                    this.posts.unshift(response.data)
                    this.body = ''
                    this.user.posts_count += 1
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        logout() {
            console.log('Log out')

            this.userStore.removeToken()

            this.$router.push('/login')
        }
    }
}
</script>