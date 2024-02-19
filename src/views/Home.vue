<template>
    <div>
      <h2>Welcome to Foodiology!</h2>
      <p>Transforming Kitchen Confusion into Delicious Discoveries.</p>
      <p>Discover delicious recipes based on your ingredients and preferences!</p>
      <recipe-search-bar @search="searchRecipes"></recipe-search-bar>
      <recipe-list :recipes="searchedRecipes" @view-details="viewRecipeDetails"></recipe-list>
    </div>
  </template>
  
  <script>
  import RecipeSearchBar from '@/components/RecipeSearchBar.vue';
  import RecipeList from '@/components/RecipeList.vue';
  
  export default {
    components: {
      RecipeSearchBar,
      RecipeList
    },
    data() {
      return {
        searchedRecipes: [],
      };
  
      
    },
    methods: {
      searchRecipes(ingredients) {
        // Call backend API to get recipes based on ingredients
        // Update searchedRecipes data property
      },
      viewRecipeDetails(recipeId) {
        // Navigate to the recipe details page or show a modal
      }
    }
  };
  
  </script>

<style scoped>
.logo {
  width: auto; /* Adjust the width to your preferred size */
  height: 100px; /* Maintain the aspect ratio */
}
</style>
  