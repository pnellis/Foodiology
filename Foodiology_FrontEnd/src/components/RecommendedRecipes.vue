<template>
    <div class="p-4 bg-white border border-gray-200 rounded-lg">
      <h3 class="mb-6 text-xl">Liked Recipes</h3>
      <div v-if="recipes.length === 0" class="text-gray-500">No recipes saved yet.</div>
      <div v-else class="space-y-4">
        <div v-for="recipe in recipes" :key="recipe.id" class="flex items-center justify-between">
          <div class="flex items-center space-x-2">
            <img :src="recipe.image_url || '/public/assets/logocat.png'" class="w-[40px] rounded-full">
            <p class="text-xs"><strong>{{ recipe.title }}</strong></p>
          </div>
          <!-- <a :href="`/recipes/${recipe.id}`" class="py-2 px-3 bg-pink-600 text-white text-xs rounded-lg">Show</a> -->
          <router-link :to="{ name: 'postview', params: { id: recipe.id } }"
          class="py-2 px-3 bg-pink-600 text-white text-xs rounded-lg">
          Show
        </router-link>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    data() {
      return {
        recipes: [],
        error: null,
      };
    },
    mounted() {
      this.fetchLikedRecipes();
    },
    methods: {
      fetchLikedRecipes() {
        axios
          .get('/api/posts/liked/')
          .then(response => {
            this.recipes = response.data;
          })
          .catch(error => {
            console.error('There was an error fetching the liked recipes:', error);
            this.error = 'Failed to fetch liked recipes.';
          });
      }
    }
  }
  </script>