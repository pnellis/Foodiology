<template>
  <div class="grid grid-cols-6 gap-3">
    <div class="search-left col-span-4">
      <div class="bg-white border border-gray-200 rounded-lg">
        <div class="p-4 flex space-x-4">
          <div class="recipe-search-bar">
            <div class="combined-search">
              <form @submit.prevent="searchRecipes" class="form-section">
                <div class="search-section">
                  <label for="search">Type in your ingredients:</label>
                  <input v-model="searchValue" id="search" class="input-field"
                    placeholder="Enter ingredients with Space" />
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
            <div id="recipe-card"></div>
          </div>
        </div>
      </div>
    </div>

    <div class="recommendations-right col-span-2">
      <PantryComponent />
      <RecommendedRecipes />
      <TrendingRecipes />
    </div>

  </div>
</template>

<script>
import RecommendedRecipes from '../components/RecommendedRecipes.vue'
import TrendingRecipes from '../components/TrendingRecipes.vue'
import PantryComponent from '../components/PantryComponent.vue';

export default {
  name: 'SearchView',
  components: {
    RecommendedRecipes,
    TrendingRecipes,
    PantryComponent
  },
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

      // Fetch the ingredients list from local storage or global state
      // let ingredientsList = localStorage.getItem('ingredients') || ''; // Assuming ingredients are stored as a comma-separated string

      // Combine the user-input ingredients with the stored ingredients list
      // let combinedIngredients = this.searchValue + (ingredientsList ? `, ${ingredientsList}` : '');

      // Base query parameters
      // let queryParams = `?type=public&q=${encodeURIComponent(combinedIngredients)}&app_id=${app_id}&app_key=${app_key}`;

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
      let userIngredients = this.searchValue.split(' ').map(ingredient => ingredient.toLowerCase());
      recipes.forEach((recipe) => {
        // let ingredientLines = recipe.recipe.ingredientLines;
        let recipeIngredients = recipe.recipe.ingredientLines.map(ingredient => ingredient.toLowerCase());

        // Determine which ingredients the user has and which are missing
        let ingredientsYouHave = [];
        let ingredientsYouNeed = [];

        recipeIngredients.forEach(ingredient => {
          if (userIngredients.some(userIngredient => ingredient.includes(userIngredient.toLowerCase()))) {
            ingredientsYouHave.push(ingredient);
          } else {
            ingredientsYouNeed.push(ingredient);
          }
        });
        html += `
                <div class="recipe-card">
                    <img src="${recipe.recipe.image}" alt="${recipe.recipe.label}">
                    <h3>${recipe.recipe.label}</h3>
                    <div>
                        <strong>Ingredients you have:</strong>
                        <ul>${ingredientsYouHave.map(ingredient => `<li>${ingredient}</li>`).join('')}</ul>
                    </div>
                    <div>
                        <strong>Ingredients you need:</strong>
                        <ul>${ingredientsYouNeed.map(ingredient => `<li>${ingredient}</li>`).join('')}</ul>
                    </div>
                    <ul>
                        ${recipe.recipe.ingredientLines.map(ingredient => `<li>${ingredient}</li>`).join('')}
                    </ul>
                    <a href ="${recipe.recipe.url}" target="_blank" class="recipe-button">View Recipe</a>
                </div>
                `;
      });
      document.getElementById('results').innerHTML = html;
    }
  }
};
</script>

<style >
.recipe-card ul {
  list-style-type: none;
  /* This removes the bullets */
  padding-left: 0;
  /* This removes the padding where bullets would normally be */
}

.recipe-button {
  background-color: rgb(134, 212, 208);
  /* Green background */
  color: rgb(255, 255, 255);
  /* White text */
  padding: 10px 20px;
  /* Some padding */
  text-align: center;
  /* Centered text */
  text-decoration: none;
  /* No underline */
  display: inline-block;
  /* Needed for padding and background color */
  font-size: 16px;
  /* Font size */
  margin: 4px 2px;
  /* Some margin */
  cursor: pointer;
  /* Pointer cursor on hover */
  border-radius: 5px;
  /* Rounded corners */
}

.recipe-button:hover {
  background-color: rgb(52, 136, 131);
  /* Darker shade of green on hover */
}


#results {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  /* Creates 3 columns */
  gap: 40px;
  /*  add space between the s */
}

.recipe-card {
  border: 1px solid #edd5db9f;
  /* Adds a border around the card */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  /* Adds a subtle shadow for depth */
  border-radius: 10px;
  /* Rounds the corners of the card */
  background-color: #edd5db9f;
  /* Set background */

}

.recipe-card:hover {
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
  /* Enhances the shadow when hovered */
}

.recipe-card img {
  width: 70%;
  /* Makes the image fill the card width */
  border-radius: 10px 10px 10px 10px;
  /* Rounds the top left, top right, bottom left, bottom right */
}

.recipe-card h3 {
  font-size: 2em;
  font-weight: bold;
  margin-top: 20px;
  /* Adds space above the title */
}

.recipe-card li {
  margin-bottom: 10px;
  /* Adds space between list items */
}

.combined-search {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  /* Ensure responsiveness */
  width: 100%;
}

.recipe-search-bar {
  display: flex;
  flex-direction: column;
  /* Stack items vertically */
  align-items: center;
  margin-bottom: 20px;
  margin-left: 20px;
  margin-right: 20px;
  width: 100%;
}

.search-section label,
.filter-section label {
  font-size: 1.5em;
  /* Adjust the font size as needed */
  font-weight: bold;
}


.search-section,
.filter-section {
  display: flex;
  flex-direction: column;
  margin-right: 10px;
  /* Adjust spacing as needed */
  width: 100%;
}

.form-section {
  display: flex;
  flex-direction: row;
  /* Align form elements side by side */
  align-items: center;
  gap: 10px;
  /* Space between form elements */
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