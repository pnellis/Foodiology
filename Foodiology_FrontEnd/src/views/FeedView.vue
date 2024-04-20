<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-center col-span-3 space-y-4">
            <div class="bg-white border border-gray-200 rounded-lg">
                <form v-on:submit.prevent="submitForm" method="post">
                    <div class="p-4">  
                        <label for="title" class="block text-sm font-medium text-gray-700">Recipe Name:</label>
                        <textarea v-model="title" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="title"></textarea>
                    </div>

                    <div class="p-4">  
                        <label for="ingredients" class="block text-sm font-medium text-gray-700">Ingredients:</label>
                        <textarea v-model="ingredients" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="Ingredients (separate by comma)"></textarea>
                    </div>

                    <div class="p-4">  
                        <label for="instructions" class="block text-sm font-medium text-gray-700">Steps:</label>
                        <textarea v-model="instructions" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="instructions"></textarea>
                    </div>

                    <div class="p-4 border-t border-gray-100 flex justify-between">
                        <a href="#" class="inline-block py-4 px-6 bg-gray-600 text-white rounded-lg">Attach image</a>

                        <button class="inline-block py-4 px-6 bg-pink-600 text-white rounded-lg">Post</button>
                    </div>
                </form>
            </div>

            <div 
                class="p-4 bg-white border border-gray-200 rounded-lg"
                v-for="post in posts"
                v-bind:key="post.id"
            >
                <FeedItem v-bind:post="post" />
            </div>

        </div>

        <div class="main-right col-span-1 space-y-4">
            <RecommendedRecipes/>
            <TrendingRecipes/>
              
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import RecommendedRecipes from '../components/RecommendedRecipes.vue'
import TrendingRecipes from '../components/TrendingRecipes.vue'
import FeedItem from '../components/FeedItem.vue'

export default {
    name: 'FeedView',
    components: {
        RecommendedRecipes,
        TrendingRecipes,
        FeedItem
    },

    data() {
        return {
            posts: [],
            title: '',
            ingredients: '',
            instructions: '',
            // image: null,
        }
    },

    mounted() {
        this.getFeed()
    },

    computed: {
        canSubmit() {
            return this.title.trim() && this.ingredients.trim() && this.instructions.trim();
            // return this.recipe_name.trim() && this.ingredients.trim() && this.steps.trim() && this.image;
        }
    },

    methods: {
        getFeed() {
            axios
                .get('/api/posts/')
                .then(response => {
                    console.log('data', response.data)

                    this.posts = response.data
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        triggerFileInput() {
            this.$refs.fileInput.click();
        },

        submitForm() {
            let formData = new FormData()
            formData.append('title', this.title)
            formData.append('ingredients', this.ingredients)
            formData.append('instructions', this.instructions)
            // formData.append('image', this.image)

            axios
                .post('/api/posts/create/', formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                })
                .then(response => {
                    console.log('data', response.data)

                    this.posts.unshift(response.data)
                    this.title = ''
                    this.ingredients = ''
                    this.instructions = ''
                    // this.image = null
                })
                .catch(error => {
                    console.log('error', error)
                })
        }

        // submitForm() {
        //     console.log('submitForm', this.body)

        //     axios
        //         .post('/api/posts/create/', {
        //             'body': this.body
        //         })
        //         .then(response => {
        //             console.log('data', response.data)

        //             this.posts.unshift(response.data)
        //             this.body = ''
        //         })
        //         .catch(error => {
        //             console.log('error', error)
        //         })
        // }
    }
}
</script>