<template>
    <div>
      <recipe-search-bar @search="searchRecipes"></recipe-search-bar>
      <recipe-list :recipes="searchedRecipes" @view-details="viewRecipeDetails"></recipe-list>
    </div>
  </template>
  
  <script>
  import RecipeSearchBar from '@/components/RecipeSearchBar.vue';
  import RecipeList from '@/components/RecipeList.vue';

  import Logo from '@/assets/logo.png';
  
  export default {
    components: {
      RecipeSearchBar,
      RecipeList
    },
    data() {
      return {
        searchedRecipes: [],
        Logo: Logo
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
  