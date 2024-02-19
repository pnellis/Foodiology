<template>
    <div class="recipe-list">
      <h2>Recipes</h2>
      <ul>
        <li v-for="recipe in recipes" :key="recipe.id">
          {{ recipe.title }}
          <button @click="viewRecipeDetails(recipe.id)" class="details-button">View Details</button>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    props: ['recipes'],
    methods: {
      viewRecipeDetails(recipeId) {
        // Emit an event to notify the parent component to show recipe details
        this.$emit('view-details', recipeId);
      }
    }
  };
  </script>
  
  <style scoped>
  .recipe-list {
    margin-top: 20px;
  }
  
  ul {
    list-style-type: none;
    padding: 0;
  }
  
  li {
    margin-bottom: 10px;
  }
  
  .details-button {
    padding: 5px;
    background-color: #f792ac;
    color: white;
    border: none;
    cursor: pointer;
  }
  </style>
  