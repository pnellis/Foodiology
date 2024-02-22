<!--  -->
<template>
  <div class="recipe-search-bar">
    <div class="search-section">
      <form @submit.prevent="searchRecipes">
        <label for="search">Search:</label>
        <input v-model="searchValue" id="search" class="input-field" placeholder="Enter ingredients with Space" />
        
      </form>
    </div>
    <div class="filter-sections">
      <div class="filter-section">
        <label for="dietaryPreferencesType">Dietary Preferences:</label>
        <select v-model="dietaryPreferencesType" class="select-field">
          <option value="">Select Dietary Preferences</option>
          <option value="vegetarian">vegetarian</option>
          <option value="vegan">vegan</option>
          <option value="dairy-free">dairy-free</option>
          <option value="tree-nut-free">tree-nut-free</option>
          <option value="shellfish-free">shellfish-free</option>
          <option value="alcohol-free">alcohol-free</option>
          <option value="gluten-free">gluten-free</option>
          <option value="peanut-free">peanut-free</option>
          <option value="sesame-free">sesame-free</option>
          <option value="soy-free">soy-free</option>
        </select>
      </div>
      <div class="filter-section">
        <label for="cuisineType">Cuisine Type:</label>
        <select v-model="cuisineType" class="select-field">
          <option value="">Select Cuisine</option>
          <option value="american">american</option>
          <option value="asian">asian</option>
          <option value="british">british</option>
          <option value="caribbean">caribbean</option>
          <option value="central europe">central europe</option>
          <option value="chinese">chinese</option>
          <option value="easter europe">eastern europe</option>
          <option value="french">greek</option>
          <option value="indian">indian</option>
          <option value="italian">italian</option>
          <option value="japanese">japanese</option>
          <option value="korean">korean</option>
          <option value="kosher">kosher</option>
          <option value="mediterranean">mediterranean</option>
          <option value="mexican">mexican</option>
          <option value="middle eastern">middle eastern</option>
          <option value="nordic">nordic</option>
          <option value="south american">south american</option>
          <option value="south east asian">south east asian</option>
        </select>
      </div>
      <div class="filter-section">
        <label for="mealType">Meal Type:</label>
        <select v-model="mealType" class="select-field">
          <option value="">Select Meal Type</option>
          <option value="breakfast">breakfast</option>
          <option value="lunch/dinner">lunch/dinner</option>
          <option value="snack">snack</option>
          <option value="teatime">teatime</option>
        </select>
      </div>
    </div>
    <div>
      <button @click="searchRecipes" class="search-button">Search</button>
    </div>
    <div id="results"></div>
    
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
  let baseUrl = `https://api.edamam.com/api/recipes/v2`;
  let app_id = `6c7cf088`;
  let app_key = `e7750c557637054d9401d486453748b9`;
  // base query parameters
  let queryParams = `?type=public&q=${encodeURIComponent(this.searchValue)}&app_id=${app_id}&app_key=${app_key}`;


  if (this.dietaryPreferencesType) {
    queryParams += `&cuisineType=${encodeURIComponent(this.dietaryPreferencesType)}`;
  }
  if (this.mealType) {
    queryParams += `&mealType=${encodeURIComponent(this.mealType)}`;
  }
  if (this.cuisineType) {
    queryParams += `&cuisineType=${encodeURIComponent(this.cuisineType)}`;
  }

  const response = await fetch(baseUrl + queryParams);
  
  const data = await response.json();

  console.log(data)
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
  background-color: #f792ac;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.search-button:hover {
  background-color: #ba3850;
}
</style>