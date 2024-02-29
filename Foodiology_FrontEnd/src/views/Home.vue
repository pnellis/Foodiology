<template>
    <div>
      <div class="content-container">
    <img src="@/assets/HomePhoto.jpg" alt="Delicious food" class="home-photo">
    <div class="text-description">
      <!-- Your text description here -->
      <p>Welcome to Foodiology! </p>
      <p>Transforming kitchen confusion into delicious discoveries.</p>
      <p>Discover delicious recipes based on your ingredients and preferences!</p>
    </div>
    </div>
    <header>
      <recipe-search-bar @search="searchRecipes"></recipe-search-bar>
      
    </header>
    <recipe-list :recipes="searchedRecipes" @view-details="viewRecipeDetails"></recipe-list>
    </div>
  
  </template>
  
  <script>
  import RecipeSearchBar from '@/components/RecipeSearchBar.vue';
  
  export default {
    components: {
      RecipeSearchBar
    },
    data() {
      return {
        searchedRecipes: [],
      };
    },
  };
  
  </script>

<style scoped>

header {
  display: flex; /* Use flex display to align items in a row */
  align-items: center; /* Align items to the start of the flex container */
  background-color: #ffffff;
  color: rgb(134, 212, 208);
  width: 100%;
  padding: 10px 0;
  /* height: 100px;  */
  /* OR use min-height if you want it to be able to grow in certain conditions */
}
.content-container {
  display: flex;
  align-items: center; 
  justify-content: left; /* This will horizontally center the content */
  color: rgb(0, 0, 0);
  padding: 20px;
}

.text-description p:nth-of-type(1) {
  font-size: 3.5em; /* Adjust the size as needed for the first paragraph */
  font-weight: bold; /* Makes the text bold */
}

.text-description p:nth-of-type(2) {
  font-size: 2em; /* Adjust the size as needed for the second paragraph */
 /* Makes the text bold */
}

.text-description p:nth-of-type(3) {
  font-size: 2em; /* Adjust the size as needed for the second paragraph */
 /* Makes the text bold */
}

.home-photo {
  max-width: 50%; /* Adjust the width as necessary */
  height: auto; /* Keep the aspect ratio of the image */
}

.text-description {
  max-width: 50%;
  margin-left: 20px; /* Adjust spacing between image and text as necessary */
}

</style>
  