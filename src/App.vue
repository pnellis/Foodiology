<template>
  <div>
    <h1 class="mb-4">Foodiology</h1>
    <div class="container">
      <div class="btn-group">
        <button class="btn btn-primary dropdown-toggle" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          Select Ingredients
        </button>
        <div class="dropdown-menu">
          <a class="dropdown-item" href="#">Ingredient 1</a>
          <a class="dropdown-item" href="#">Ingredient 2</a>
          <a class="dropdown-item" href="#">Ingredient 3</a>
          <!-- Add more items as needed -->
        </div>
      </div>

      <div class="form-check mt-3" v-if="checked">
        <input class="form-check-input" type="checkbox" value="" id="checkbox1">
        <label class="form-check-label" for="checkbox1">
          Recipe Option 1
        </label>
      </div>
      <div class="form-check" v-if="checked">
        <input class="form-check-input" type="checkbox" value="" id="checkbox2">
        <label class="form-check-label" for="checkbox2">
          Recipe Option 2
        </label>
      </div>

      <button class="btn btn-primary mt-3" @click="showInput">Search for Recipes</button>
      <input v-if="checked" type="text" class="form-control mt-3" placeholder="Search for recipes...">
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const checked = ref(false)

const showInput = () => {
  checked.value = !checked.value
}
</script>
