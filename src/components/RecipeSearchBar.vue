<!--  -->
<template>
  <div class="recipe-search-bar">
    <div class="search-section">
      <form @submit.prevent="searchRecipes">
        <label for="search">Search:</label>
        <input v-model="searchValue" id="search" class="input-field" placeholder="Enter ingredients" />
        <button type="submit" class="search-button">Search</button>
      </form>
    </div>
    <div class="filter-sections">
      <div class="filter-section">
        <label for="dietaryPreferencesType">Dietary Preferences:</label>
        <select v-model="dietaryPreferencesType" class="select-field">
          <option value="">Select Dietary Preferences</option>
          <option value="vegetarian">Vegetarian</option>
          <option value="vegan">Vegan</option>
          <option value="dairyfree">Dairy-Free</option>
          <!-- Add more options as needed -->
        </select>
      </div>
      <div class="filter-section">
        <label for="cuisineType">Cuisine Type:</label>
        <select v-model="cuisineType" class="select-field">
          <option value="">Select Cuisine</option>
          <option value="italian">Italian</option>
          <option value="mexican">Mexican</option>
          <option value="chinese">Chinese</option>
          <option value="korean">Korean</option>
          <option value="indian">Indian</option>
          <option value="french">French</option>
          <!-- Add more options as needed -->
        </select>
      </div>
      <div class="filter-section">
        <label for="mealType">Meal Type:</label>
        <select v-model="mealType" class="select-field">
          <option value="">Select Meal Type</option>
          <option value="breakfast">Breakfast</option>
          <option value="lunch">Lunch</option>
          <option value="dinner">Dinner</option>
          <!-- Add more options as needed -->
        </select>
      </div>
    </div>
    <div id="results"></div>
    <button @click="searchRecipes" class="search-button">Search</button>
  </div>
</template>
<script>
export default {
  data() {
    return {
      ingredients: '',
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
        <div>
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
.recipe-search-bar {
  display: flex;
  flex-direction: column; /* Stack items vertically */
  align-items: center;
  margin-bottom: 20px;
}

.search-section {
  width: 100%;
  margin-bottom: 15px;
}

.filter-sections {
  display: flex;
  justify-content: space-between;
  width: 100%;
}

.filter-section {
  flex: 1;
  margin-right: 10px;
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
  background-color: #fabbe0;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.search-button:hover {
  background-color: #45a049;
}
</style>