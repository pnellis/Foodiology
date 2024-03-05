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
     <!-- Random Recipes Section -->
     <div v-if="showRandomRecipes" class="random-recipes-container">
      <h2>Some Random Recipes You Might Like</h2>
      <swiper :slidesPerView="3" :spaceBetween="30" class="random-recipes-swiper">
        <swiper-slide v-for="recipe in randomRecipes" :key="recipe.id">
          <div class="recipe-card">
            <!-- Display random recipe -->
          </div>
        </swiper-slide> 
      </swiper>
    </div>

    <recipe-list :recipes="searchedRecipes" @view-details="viewRecipeDetails"></recipe-list>

    </div>
  
  </template>
  
  <script>
  import { Swiper, SwiperSlide } from 'swiper/vue';
  import 'swiper/swiper-bundle.css';
  import RecipeSearchBar from '@/components/RecipeSearchBar.vue';
  
  export default {
    components: {
      RecipeSearchBar,  
      Swiper,
      SwiperSlide,
    },
    data() {
      return {
        searchedRecipes: [],
        randomRecipes: [],
        showRandomRecipes: true,
      };
    },
    created() {
      this.fetchRandomRecipes();
    },
    methods: {
      async fetchRandomRecipes() {
        // Fetch random recipes and assign them to randomRecipes
        // Set showRandomRecipes to true
        let baseUrl = `https://api.edamam.com/api/recipes/v2`;
        let app_id = `6c7cf088`; // Replace with your actual app_id
        let app_key = `e7750c557637054d9401d486453748b9`; // Replace with your actual app_key
        const randomIngredients = ['chicken', 'beef', 'fish', 'carrot', 'apple', 'banana', 'tomato', 'cheese'];
        const randomQuery = randomIngredients[Math.floor(Math.random() * randomIngredients.length)];
        // Random query parameter
        let queryParams = `?type=public&q=${encodeURIComponent(randomQuery)}&app_id=${app_id}&app_key=${app_key}`;

        try {
          const response = await fetch(baseUrl + queryParams);
          const data = await response.json();
          this.displayRecipes(data.hits);
        } catch (error) {
          console.error('Error fetching random recipes:', error);
        }
        
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
            <a href ="${recipe.recipe.url}" target="_blank" class="recipe-button">View Recipe</a>
          </div> 
          `;
        });
        document.getElementById('results').innerHTML = html;
      },
      searchRecipes() {
        // Perform the search and update searchedRecipes
        // Hide the random recipes section
        this.showRandomRecipes = false;
      },
    },
  };
  
  </script>

<style scoped>

.random-recipes-container {
    margin-top: 2rem;
  }

  .random-recipes-swiper {
    width: 100%;
    overflow: hidden;
  }

  .swiper-slide {
    width: auto; /* Adjust the width of the slides to fit the content */
    flex-shrink: 0; /* Prevent slides from shrinking */
  }

  .recipe-card {
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
    transition: 0.3s;
    width: 200px; /* Set a fixed width for the recipe cards */
    margin: 0 15px; /* Add some space between cards */
    border-radius: 5px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }
.recipe-card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); /* Adds a subtle shadow around the card */
  transition: 0.3s; /* Smooth transition for mouse-over effects */
  width: 40%; /* Set the width of the card */
  margin: 1rem; /* Add some space around the card */
  border-radius: 5px; /* Slightly rounded corners for aesthetics */
  overflow: hidden; /* Ensures the content fits within the card */
}

.recipe-card img {
  width: 100%; /* Ensure the image covers the card width */
  height: auto; /* Maintain aspect ratio */
}

.recipe-card-container {
  padding: 2px 16px; /* Padding inside the card */
}

.recipe-card h3 {
  font-weight: 500; /* Font weight for the recipe title */
}

.recipe-card ul {
  list-style-type: none; /* Removes the default list styling */
  padding: 0; /* Removes the default padding */
}

.recipe-button {
  background-color: #4CAF50; /* Green background for the button */
  color: white; /* White text for the button */
  padding: 10px 24px; /* Padding around the text in the button */
  text-align: center; /* Center the text inside the button */
  text-decoration: none; /* Remove the underline from the text */
  display: inline-block; /* Allows margin to be applied correctly */
  font-size: 16px; /* Size of the button text */
  margin: 4px 2px; /* Margin around the button */
  cursor: pointer; /* Changes the cursor to signify this can be clicked */
  border-radius: 5px; /* Rounded corners on the button */
  border: none; /* No border for the button */
}

.recipe-button:hover {
  background-color: #45a049; /* Darker shade of green for hover effect */
}

/* Add styles for the random recipes section */
.random-recipes {
  margin-top: 2rem; /* Space above the random recipes section */
}

/* Adjustments for when recipe cards are displayed side by side */
@media (min-width: 600px) {
  .recipe-card {
    width: calc(50% - 2rem); /* Half the container width minus margin */
  }
}

/* Adjustments for when recipe cards are in a grid layout */
@media (min-width: 900px) {
  .recipe-card {
    width: calc(33% - 2rem); /* One third of the container width minus margin */
  }
}



.random-recipes {
    /* styles for the random recipes section */
    display: flex; 
  }

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
  