<template>
  <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">

    <div class="main-left col-span-3 space-y-4">
      <div class="bg-white border border-gray-200 rounded-lg">
        <form v-on:submit.prevent="submitForm" class="p-4 flex flex-col space-y-4">
          <div class="flex space-x-4">
            <input v-model="query" type="search" class="p-4 w-full bg-gray-100 rounded-lg"
              placeholder="What are you looking for?">
            <button class="inline-block py-4 px-6 bg-pink-600 text-white rounded-lg">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round"
                  d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"></path>
              </svg>
            </button>
          </div>
          <div class="flex flex-wrap">
            <input v-model.number="filters.totalTime" type="number" class="p-2 w-full md:w-1/4 bg-gray-100 rounded-lg"
              placeholder="Total time (min)">
            <select v-model="filters.yields" class="p-2 w-full md:w-1/4 bg-gray-100 rounded-lg">
              <option disabled value="">Select yields</option>
              <option>1-2</option>
              <option>3-4</option>
              <option>5+</option>
            </select>
            <select v-model="filters.mealType" class="p-2 w-full md:w-1/4 bg-gray-100 rounded-lg">
              <option disabled value="">Select meal type</option>
              <option>Breakfast</option>
              <option>Lunch</option>
              <option>Dinner</option>
              <option>Snack</option>
            </select>
            <select v-model="filters.cuisineType" class="p-2 w-full md:w-1/4 bg-gray-100 rounded-lg">
              <option disabled value="">Select cuisine type</option>
              <option>Italian</option>
              <option>Mexican</option>
              <option>Chinese</option>
              <option>Indian</option>
            </select>
            <input v-model="filters.nutrients" type="text" class="p-2 w-full md:w-1/4 bg-gray-100 rounded-lg"
              placeholder="Nutrients (e.g., high protein)">
          </div>
        </form>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-3 p-4">
        <div v-for="post in posts" :key="post.id">
          <FeedItemCard :post="post" />
        </div>
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
import FeedItemCard from '@/components/FeedItemCard.vue'
import { useToastStore } from '@/stores/toast'

export default {
  name: 'SearchView',
  components: {
    RecommendedRecipes,
    TrendingRecipes,
    FeedItemCard
  },
  setup() {
      const toastStore = useToastStore()

      return {
          toastStore
      }
  },
  data() {
    return {
      searchValue: '',
      dietaryPreferencesType: [],
      cuisineType: '',
      mealType: '',
      query: '',
      posts: [],
      pantryIngredients: [],
      filters: {
        totalTime: null,
        yields: '',
        mealType: '',
        cuisineType: '',
        nutrients: ''
      }
    };
  },
  created() {
    this.fetchPantryIngredients();  // Fetch pantry ingredients when component is created
  },
  methods: {
    fetchPantryIngredients() {
      axios
        .get('/api/pantry/')
        .then(response => {
          this.pantryIngredients = response.data.map(item => item.ingredient_name);
        }).catch(error => console.error('Failed to load pantry ingredients:', error));
    },
    submitForm() {
      let searchQuery = this.query;
      if (!searchQuery) {
        searchQuery = this.pantryIngredients.join(' '); // Join the ingredients into a single string if no direct query
      }

      console.log('submitForm', searchQuery);

      axios.post('/api/search/', {
        query: searchQuery,
        filters: this.filters // Send the filters object to the backend
      })
        .then(response => {
          console.log('response:', response.data);
          if (response.data.posts.length === 0) {
            this.toastStore.showToast(5000, 'No matching recipes based on inputted ingredient(s)', 'bg-red-300');
          } else {
            this.posts = response.data.posts;
          }
        })
        .catch(error => {
          console.log('error:', error);
        });
    },
  }
};
</script>