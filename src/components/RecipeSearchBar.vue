<!--  -->

<template>
  <div class="recipe-search-bar">
    <div class="combined-search">
      <form @submit.prevent="searchRecipes" class="form-section">
        <div class="search-section">
          <label for="search">Type in your ingredients:</label>
          <input v-model="searchValue" id="search" class="input-field" placeholder="Enter ingredients with Space" />
        </div>
        <div class="filter-section">
          <label for="dietaryPreferencesType">Dietary Preferences:</label>
          <select v-model="dietaryPreferencesType" class="select-field">
            <option value="">Select Dietary Preferences</option>
            <option value="vegetarian">Vegetarian</option>
            <option value="vegan">Vegan</option>
            <option value="dairyfree">Dairy-Free</option>
          </select>
        </div>
        <div class="filter-section">
          <label for="cuisineType">Cuisine Type:</label>
          <select v-model="cuisineType" class="select-field">
            <option value="">Select Cuisine</option>
            <option value="Italian">Italian</option>
            <option value="Mexican">Mexican</option>
            <option value="Chinese">Chinese</option>
            <!-- Add other options as needed -->
          </select>
        </div>
        <div class="filter-section">
          <label for="mealType">Meal Type:</label>
          <select v-model="mealType" class="select-field">
            <option value="">Select Meal Type</option>
            <option value="breakfast">Breakfast</option>
            <option value="lunch">Lunch</option>
            <option value="dinner">Dinner</option>
            <!-- Add other options as needed -->
          </select>
        </div>
      </form>
    </div>
  
    <div id="results"></div>
        <button @click="searchRecipes" class="search-button">Search</button>
      
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchValue: '',
      dietaryPreferencesType: '',
      cuisineType: '',
      mealType: ''
    };
  },
  methods: {
    async searchRecipes() {
      const response = await fetch(`https://api.edamam.com/api/recipes/v2?q=${this.searchValue}&app_id=6c7cf088&app_key=e7750c557637054d9401d486453748b9&type=public`);
      const data = await response.json();
      this.displayRecipes(data.hits);
    },
    displayRecipes(recipes) {
  let html = '';
  recipes.forEach((recipe) => {
    html += `
    <div class="recipe-card">
      <img src="${recipe.recipe.image}" alt="${recipe.recipe.label}">
      <h3>${recipe.recipe.label}</h3>
      <ul>
        ${recipe.recipe.ingredientLines.map(ingredient => `<li>${ingredient}</li>`).join('')}
      </ul>
      <a href="${recipe.recipe.url}" target="_blank">View Recipe</a>
    </div> 
    `;
  });
  document.getElementById('results').innerHTML = html;
}
  }
};
</script>
<style scoped>

#results {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around; /* This will space out the items evenly */
  gap: 20px; /* This adds space between the items */
}

.recipe-card {
  flex: 0 1 calc(33.333% - 20px); /* Take up one-third minus gap */
  display: flex;
  flex-direction: column;
  align-items: center; /* Center-align the items for aesthetic purposes */
  box-shadow: 0 2px 4px rgba(0,0,0,0.1); /* Optional: adds a slight shadow for depth */
  padding: 10px;
  margin-bottom: 20px; /* Space at the bottom of each card */
}

.recipe-card img {
  width: 100%; /* Make images responsive within the card */
  height: auto;
  border-radius: 5px; /* Optional: rounds the corners of the images */
}

.combined-search {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap; /* Ensure responsiveness */
  width: 100%;
}
.recipe-search-bar {
  display: flex;
  flex-direction: column; /* Stack items vertically */
  align-items: center;
  margin-bottom: 20px;
  margin-left: 20px;
  margin-right: 20px;
  width: 100%;
}

.search-section label,
.filter-section label {
  font-size: 1.5em; /* Adjust the font size as needed */
  font-weight: bold;
}


.search-section, .filter-section {
  display: flex;
  flex-direction: column;
  margin-right: 10px; /* Adjust spacing as needed */
  width: 100%;
}

.form-section {
  display: flex;
  flex-direction: row; /* Align form elements side by side */
  align-items: center;
  gap: 10px; /* Space between form elements */
  width: 100%;
}

.input-field,
.select-field {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.search-button {
  padding: 12px;
  background-color: rgb(134, 212, 208);
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.search-button:hover {
  background-color: rgb(52, 136, 131);
}
</style>