<template>
    <div class="recipe-search-bar">
      <div class="filter-section">
        <label for="ingredients">Ingredients:</label>
        <input v-model="ingredients" placeholder="Enter ingredients" class="input-field">
      </div>
  
      <div class="filter-section">
        <label for="dietaryPreferences">Dietary Preferences:</label>
        <div>
          <label>
            <input type="checkbox" v-model="dietaryPreferences.vegetarian"> Vegetarian
          </label>
          <label>
            <input type="checkbox" v-model="dietaryPreferences.vegan"> Vegan
          </label>
          <label>
            <input type="checkbox" v-model="dietaryPreferences.dairyfree"> Dairy-Free
          </label>
          <!-- Add more dietary preferences as needed -->
        </div>
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
          <!-- Add more cuisine types as needed -->
        </select>
      </div>
  
      <div class="filter-section">
        <label for="mealType">Meal Type:</label>
        <select v-model="mealType" class="select-field">
          <option value="">Select Meal Type</option>
          <option value="breakfast">Breakfast</option>
          <option value="lunch">Lunch</option>
          <option value="dinner">Dinner</option>
          <!-- Add more meal types as needed -->
        </select>
      </div>
  
      <button @click="searchRecipes" class="search-button">Search</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        ingredients: '',
        dietaryPreferences: {
          vegetarian: false,
          vegan: false
          // Add more dietary preferences as needed
        },
        cuisineType: '',
        mealType: ''
      };
    },
    methods: {
      searchRecipes() {
        // Call backend API to search for recipes based on filters
        this.$emit('search', {
          ingredients: this.ingredients,
          dietaryPreferences: this.dietaryPreferences,
          cuisineType: this.cuisineType,
          mealType: this.mealType
        });
      }
    }
  };
  </script>
  

<style scoped>
.recipe-search-bar {
  margin-bottom: 20px;
}

.filter-section {
  margin-bottom: 15px;
}

.input-field,
.select-field {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.checkbox-label {
  display: block;
  margin-bottom: 5px;
}

.checkbox-label input {
  margin-right: 5px;
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
  
<!-- <template>
    <div class="recipe-search-bar">
      <input v-model="ingredients" placeholder="Enter ingredients" class="input-field">
      <button @click="searchRecipes" class="search-button">Search</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        ingredients: ''
      };
    },
    methods: {
      searchRecipes() {
        // Call backend API to search for recipes based on ingredients
        this.$emit('search', this.ingredients);
      }
    }
  };
  </script>
  
  <style scoped>
  .recipe-search-bar {
    margin-bottom: 20px;
  }
  
  .input-field {
    padding: 8px;
    margin-right: 10px;
  }
  
  .search-button {
    padding: 10px;
    background-color: #fabbe0;
    color: white;
    border: none;
    cursor: pointer;
  }
  </style>
   -->