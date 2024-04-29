<template>
    <div class="relative flex flex-col mt-6 text-gray-700 bg-white shadow-md bg-clip-border rounded-xl w-70">
      <div class="relative mx-4 mt-4 overflow-hidden text-gray-700 bg-white shadow-lg bg-clip-border rounded-xl h-52">
        <img v-if="!post.image_url" 
         v-for="image in post.attachments" 
         :key="image.id" 
         :src="image.get_image" 
         alt="recipe-image" 
         class="w-full h-full object-cover">
    
        <img v-else 
            :src="post.image_url" 
            alt="recipe-image" 
            class="w-full h-full object-cover">
      </div>
      <div class="p-6">
        <h5 class="block mb-2 font-sans text-xl antialiased font-semibold leading-snug tracking-normal text-blue-gray-900">
        {{ post.title }}
        </h5>
        <div class="block font-sans text-base antialiased font-light leading-relaxed text-inherit">
          <h6 class="font-semibold">Ingredients you have:</h6>
          <ul>
            <li v-for="ingredient in ingredientsHave" :key="ingredient">{{ ingredient }}</li>
          </ul>
          <div style="margin-top: 10px;"></div>
          <h6 class="font-semibold">Ingredients you need:</h6>
          <ul>
            <li v-for="(ingredient, index) in ingredientsNeed" :key="index">{{ ingredient }}</li>
          </ul>
        </div>
      </div>
      <div class="p-6 pt-0">
        <router-link :to="{ name: 'postview', params: { id: post.id } }"
          class="align-middle select-none font-sans font-bold text-center uppercase transition-all text-xs py-3 px-6 rounded-lg bg-pink-600 text-white shadow-md shadow-gray-900/10 hover:shadow-lg hover:shadow-gray-900/20 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none">
          View Recipe
        </router-link>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      post: Object,
    },
    computed: {
      // ingredientsHave() {
      //   const ingredientsArray = this.post.ingredients.split(',');
      //   return ingredientsArray.map(ingredient => ingredient.trim()).filter(ingredient => this.isIngredientMatch(ingredient));
      // },
      ingredientsHave() {
        const searchTerms = this.$parent.query.toLowerCase().split(',');
        const ingredientsArray = this.post.ingredients.split(',');
        return ingredientsArray.map(ingredient => ingredient.trim()).filter(ingredient => this.isIngredientMatch(ingredient, searchTerms));
      },
      // ingredientsNeed() {
      //   const ingredientsArray = this.post.ingredients.split(',');
      //   const trimmedIngredients = ingredientsArray.map(ingredient => ingredient.trim());
      //   const filteredIngredients = trimmedIngredients.filter(ingredient => !this.isIngredientMatch(ingredient));
      //   const ingredientCounts = filteredIngredients.reduce((acc, ingredient) => {
      //     acc[ingredient] = (acc[ingredient] || 0) + 1;
      //     return acc;
      //   }, {});
      //   const sortedIngredients = Object.keys(ingredientCounts).sort((a, b) => ingredientCounts[b] - ingredientCounts[a]);
      //   return sortedIngredients.slice(0, 5);
      // }
      ingredientsNeed() {
        const searchTerms = this.$parent.query.toLowerCase().split(',');
        const ingredientsArray = this.post.ingredients.split(',');
        const filteredIngredients = ingredientsArray.map(ingredient => ingredient.trim()).filter(ingredient => !this.isIngredientMatch(ingredient, searchTerms));
        const ingredientCounts = filteredIngredients.reduce((acc, ingredient) => {
          acc[ingredient] = (acc[ingredient] || 0) + 1;
          return acc;
        }, {});
        const sortedIngredients = Object.keys(ingredientCounts).sort((a, b) => ingredientCounts[b] - ingredientCounts[a]);
        return sortedIngredients.slice(0, 5);
      },
    },
    methods: {
      // isIngredientMatch(ingredient) {
      //   return this.$parent.query && ingredient.toLowerCase().includes(this.$parent.query.toLowerCase());
      // }, 
      isIngredientMatch(ingredient, searchTerms) {
        return searchTerms.some(term => ingredient.toLowerCase().includes(term.trim()));
      }
    }
  };
  </script>
  
  <style>
  </style>
  