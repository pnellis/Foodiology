<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-center col-span-3 space-y-4">
            <div class="bg-white border border-gray-200 rounded-lg">
                <form v-on:submit.prevent="submitForm" method="post">
                    <div class="p-4">  
                        <label for="title" class="block text-sm font-medium text-gray-700">Recipe Name<span class="text-red-500">*</span>:</label>
                        <input v-model="title" type="text" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="Recipe Name" required>
                    </div>

                    <div class="p-4">  
                        <label for="ingredients" class="block text-sm font-medium text-gray-700">Ingredients<span class="text-red-500">*</span>:</label>
                        <div v-for="(ingredient, index) in ingredients" :key="index" class="flex items-center mb-2">
                            <input v-model="ingredients[index]" type="text" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="Ingredient" required>
                            <button type="button" @click="removeIngredient(index)" class="ml-2 px-3 py-1 bg-pink-600 text-white rounded-lg">-</button>
                        </div>
                        <button type="button" @click="addIngredient" class="mt-2 px-3 py-1 bg-pink-600 text-white rounded-lg">+</button>
                    </div>

                    <div class="p-4">  
                        <label for="instructions" class="block text-sm font-medium text-gray-700">Instructions<span class="text-red-500">*</span>:</label>
                        <textarea v-model="instructions" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="Instructions" required></textarea>
                    </div>
                    
                    <div class="p-4 flex flex-wrap justify-between">
                        <div class="w-1/4 pr-2">
                            <label for="total_time" class="block text-sm font-medium text-gray-700">Total Time:</label>
                            <input v-model="total_time" type="text" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="Total Time">
                        </div>

                        <div class="w-1/4 pr-2">
                            <label for="yields" class="block text-sm font-medium text-gray-700">Yields:</label>
                            <input v-model="yields" type="text" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="Yields">
                        </div>

                        <div class="w-1/4 pr-2">
                            <label for="meal_type" class="block text-sm font-medium text-gray-700">Meal Type:</label>
                            <input v-model="meal_type" type="text" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="Meal Type">
                        </div>

                        <div class="w-1/4">
                            <label for="cuisine_type" class="block text-sm font-medium text-gray-700">Cuisine Type:</label>
                            <input v-model="cuisine_type" type="text" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="Cuisine Type">
                        </div>
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
            instructions: '',
            total_time: '',
            yields: '',
            meal_type: '',
            cuisine_type: '',
            ingredients: [''],
            // image: null,
        }
    },

    mounted() {
        this.getFeed()
    },

    computed: {
        canSubmit() {
            return this.title.trim() && this.instructions.trim() && this.total_time.trim() && this.yields.trim() && this.meal_type.trim() && this.cuisine_type.trim();
            // return this.image;
        }
    },

    methods: {
        addIngredient() {
            this.ingredients.push('');
        },
        removeIngredient(index) {
            this.ingredients.splice(index, 1);
        },
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
            formData.append('instructions', this.instructions)
            formData.append('total_time', this.total_time)
            formData.append('yields', this.yields)
            formData.append('meal_type', this.meal_type)
            formData.append('cuisine_type', this.cuisine_type)
            // formData.append('image', this.image)

            // Append ingredients as an array
            this.ingredients.forEach(ingredient => {
                formData.append('ingredients', ingredient)
            })

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
                    this.instructions = ''
                    this.total_time = ''
                    this.yields = ''
                    this.meal_type = ''
                    this.cuisine_type = ''
                    this.ingredients = []
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