<template>
    <div class="relative flex flex-col mt-6 text-gray-700 bg-white shadow-md bg-clip-border rounded-xl w-70">
      <div class="relative mx-4 mt-4 overflow-hidden text-gray-700 bg-white shadow-lg bg-clip-border rounded-xl h-52">
        <img :src="post.image_url" alt="recipe-image" class="w-full h-full object-cover">
      </div>
      <div class="p-6">
        <h5 class="block mb-2 font-sans text-xl antialiased font-semibold leading-snug tracking-normal text-blue-gray-900">
          {{ post.title }}
        </h5>
        <div class="block font-sans text-base antialiased font-light leading-relaxed text-inherit">
          <h6 class="font-semibold">Ingredients:</h6>
          <ul>
            <li v-for="(ingredient, index) in post.ingredients" :key="index">{{ ingredient.name }}</li>
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
      post: Object
    }
  };
  </script>
  
  <style>
  /* Add your card styles here */
  </style>
  