<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-center col-span-3 space-y-4">
            <div class="bg-white border border-gray-200 rounded-lg">
                <form v-on:submit.prevent="submitForm" method="post">
                    <div class="p-4">
                        <label for="title" class="block text-sm font-medium text-gray-700">Recipe Name<span
                                class="text-red-500">*</span>:</label>
                        <input v-model="title" type="text" class="p-4 w-full bg-gray-100 rounded-lg"
                            placeholder="Recipe Name" required>
                    </div>

                    <div class="p-4">
                        <label for="ingredients" class="block text-sm font-medium text-gray-700">Ingredients<span
                                class="text-red-500">*</span>:</label>
                        <textarea v-model="ingredients" class="p-4 w-full bg-gray-100 rounded-lg"
                            placeholder="Ingredients (separate by comma)"></textarea>
                    </div>

                    <div class="p-4">
                        <label for="instructions" class="block text-sm font-medium text-gray-700">Steps<span
                                class="text-red-500">*</span>:</label>
                        <textarea v-model="instructions" class="p-4 w-full bg-gray-100 rounded-lg"
                            placeholder="instructions"></textarea>
                    </div>

                    <div class="p-4">
                        <button type="button" @click="toggleAdditionalFields"
                            class="inline-block py-2 px-4 bg-pink-600 text-white rounded-lg">Show Additional Fields</button>
                    </div>

                    <div v-show="showAdditionalFields" class="p-4 flex flex-wrap gap-4">
                        <div class="flex-1">
                            <label for="total_time" class="block text-sm font-medium text-gray-700">Total Time:</label>
                            <input v-model="total_time" type="text" class="p-2 w-full bg-gray-100 rounded-lg"
                                placeholder="Total Time">
                        </div>

                        <div class="flex-1">
                            <label for="yields" class="block text-sm font-medium text-gray-700">Yields:</label>
                            <input v-model="yields" type="text" class="p-2 w-full bg-gray-100 rounded-lg"
                                placeholder="Yields">
                        </div>

                        <div class="flex-1">
                            <label for="meal_type" class="block text-sm font-medium text-gray-700">Meal Type:</label>
                            <input v-model="meal_type" type="text" class="p-2 w-full bg-gray-100 rounded-lg"
                                placeholder="Meal Type">
                        </div>

                        <div class="flex-1">
                            <label for="cuisine_type" class="block text-sm font-medium text-gray-700">Cuisine Type:</label>
                            <input v-model="cuisine_type" type="text" class="p-2 w-full bg-gray-100 rounded-lg"
                                placeholder="Cuisine Type">
                        </div>
                    </div>

                    <div v-show="showAdditionalFields" class="p-4">
                        <label for="nutirents" class="block text-sm font-medium text-gray-700">Nutrients:</label>
                        <textarea v-model="nutirents" class="p-2 w-full bg-gray-100 rounded-lg"
                            placeholder="Nutrients (separate by comma)"></textarea>
                    </div>

                    <div id="preview" v-if="url" class="p-4">
                        <img :src="url" class="w-[100px] mt-3 rounded-xl" />
                    </div>

                    <div class="p-4 border-t border-gray-100 flex justify-between">
                        <label class="inline-block py-4 px-6 bg-gray-600 text-white rounded-lg">
                            <input type="file" ref="file" @change="onFileChange">
                            Attach image
                        </label>

                        <button class="inline-block py-4 px-6 bg-pink-600 text-white rounded-lg">Post</button>
                    </div>
                </form>
            </div>

            <div class="p-4 bg-white border border-gray-200 rounded-lg" v-for="post in posts" v-bind:key="post.id">
                <FeedItem v-bind:post="post" v-on:deletePost="deletePost" />
            </div>

        </div>

        <div class="main-right col-span-1 space-y-4">
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
            total_time: '',
            yields: '',
            meal_type: '',
            cuisine_type: '',
            nutirents: '',
            showAdditionalFields: false,
            url: null,
            // image: null,
        }
    },

    mounted() {
        this.getFeed()
    },

    computed: {
        canSubmit() {
            return this.title.trim() && this.ingredients.trim() && this.instructions.trim();
        }
    },

    methods: {
        onFileChange(e) {
            const file = e.target.files[0];
            this.url = URL.createObjectURL(file);
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
            formData.append('ingredients', this.ingredients)
            formData.append('instructions', this.instructions)
            formData.append('total_time', this.total_time)
            formData.append('yields', this.yields)
            formData.append('meal_type', this.meal_type)
            formData.append('cuisine_type', this.cuisine_type)
            formData.append('nutirents', this.nutirents)
            formData.append('image', this.$refs.file.files[0])

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
                    this.total_time = ''
                    this.yields = ''
                    this.meal_type = ''
                    this.cuisine_type = ''
                    this.nutirents = ''
                    this.showAdditionalFields = false
                    this.$refs.file.value = null
                    this.url = null
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        toggleAdditionalFields() {
            this.showAdditionalFields = !this.showAdditionalFields;
        },

        deletePost(id) {
            this.posts = this.posts.filter(post => post.id !== id)
        },
    }
}
</script>

<style>
input[type="file"] {
    display: none;
}

.custom-file-upload {
    border: 1px solid #ccc;
    display: inline-block;
    padding: 6px 12px;
    cursor: pointer;
}

.Responsive image styling .responsive-image {
    width: 100%;
    /* Makes the image responsive  */
    height: auto;
    /* Maintains aspect ratio  */
    max-width: 400px;
}
</style>

