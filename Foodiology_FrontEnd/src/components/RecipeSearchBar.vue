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
        <select v-model="dietaryPreferencesType" class="select-field" multiple>
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
          <option value="lunch">lunch</option>
          <option value="dinner">dinner</option>
          <option value="snack">snack</option>
          <option value="teatime">teatime</option>
        </select>
      </div>
      </form>
    </div>
    <button @click="searchRecipes" class="search-button">Search</button>
  <div id="results"></div>

  </div>
</template>

<script>
export default {
  data() {
    return {
      searchValue: '',
      dietaryPreferencesType: [],
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


    if (this.dietaryPreferencesType.length) {
        this.dietaryPreferencesType.forEach((diet) => {
          queryParams += `&health=${encodeURIComponent(diet)}`;
        });
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
    <div class="recipe-card">
      <img src="${recipe.recipe.image}" alt="${recipe.recipe.label}">
      <h3>${recipe.recipe.label}</h3>
      <ul>
        ${recipe.recipe.ingredientLines.map(ingredient => `<li>${ingredient}</li>`).join('')}
      </ul>
      <a href="${recipe.recipe.url}" target="_blank" class="recipe-button">View Recipe</a>
    </div> 
    `;
  });
  document.getElementById('results').innerHTML = html;
}
  }
  };

</script>

<style scoped>
.recipe-button {
  display: inline-block; /* Allows setting padding and margins */
  padding: 10px 15px; /* Adjust the padding to your liking */
  background-color: #784caf; /* Example button color, change as desired */
  color: rgb(69, 36, 36); /* Text color */
  text-align: center;
  text-decoration: none; /* Removes underline from links */
  border: none; /* Removes border */
  border-radius: 5px; /* Optional: rounds the corners */
  cursor: pointer; /* Changes cursor to pointer on hover */
  margin-top: 10px; /* Space above the button */
  transition: background-color 0.3s; /* Smooth transition for hover effect */
}

.recipe-button:hover {
  background-color: #454ca0; /* Darker shade for hover effect */
}

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
  margin-bottom: 10px;
  transition: background-color 0.3s;
}

.search-button:hover {
  background-color: rgb(52, 136, 131);
}
</style>