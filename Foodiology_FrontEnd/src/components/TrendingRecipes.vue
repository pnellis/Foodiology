<template>
    <div class="p-4 bg-white border border-gray-200 rounded-lg">
        <h3 class="mb-6 text-xl">Recipe of the Day</h3>

        <div v-if="randomRecipe">
            <div class="relative mx-4 mt-4 overflow-hidden text-gray-700 bg-white shadow-lg bg-clip-border rounded-xl h-52">
                <img :src="randomRecipe.image_url" alt="Recipe Image" class="w-full h-full object-cover">
            </div>
            <div class="p-6">
                <h5 class="block mb-2 font-sans text-xl antialiased font-semibold leading-snug tracking-normal text-blue-gray-900">{{ randomRecipe.title }}</h5>
            </div>
            <div class="p-6 pt-0">
                <router-link :to="{ name: 'postview', params: { id: randomRecipe.id } }"
                    class="align-middle select-none font-sans font-bold text-center uppercase transition-all text-xs py-3 px-6 rounded-lg bg-pink-600 text-white shadow-md shadow-gray-900/10 hover:shadow-lg hover:shadow-gray-900/20 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none">
                    View Recipe
                </router-link>
            </div>
        </div>

        <div v-else>
            <p>No recipe available.</p>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'recipes',

    data() {
        return {
            randomRecipe: null
        }
    },

    mounted() {
        this.getRandomRecipe()
    },

    methods: {
        getRandomRecipe() {
            axios
                .get('/api/posts/random/')
                .then(response => {
                    this.randomRecipe = response.data
                })
                .catch(error => {
                    console.log('Error: ', error)
                })
        }
    }
}
</script>