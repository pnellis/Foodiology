<script setup>
import { ref } from 'vue'
const checked = ref(false)
const showInput = () => {
  checked.value = !checked.value
}
</script>



<template>
  <div>
    <h1>Foodiology</h1>
    <div class="container">
      <button class="btn btn-primary" @click="showInput">Input Ingredients</button>
      <input v-if="checked" type="text" class="form-control mt-3" placeholder="Search for recipes...">
    </div>
  </div>

</template>