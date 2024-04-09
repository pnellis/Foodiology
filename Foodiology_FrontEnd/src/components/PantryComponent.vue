<template>
    <div class="add-ingredients">
        <h1>Add Your Ingredients</h1>
        <form @submit.prevent="addIngredient">
            <input type="text" v-model="newIngredient.ingredient_name" placeholder="Enter ingredient" />
            <input type="text" v-model="newIngredient.ingredient_quantity" placeholder="Enter amount" />
            <button type="submit">Add</button>
        </form>
        <ul>
            <li v-for="(ingredient, index) in ingredients" :key="index">
                {{ ingredient.ingredient_name }} - {{ ingredient.ingredient_quantity }}
                <button @click="deleteIngredient(ingredient.id)">Delete</button>
            </li>
        </ul>
    </div>
</template>
  
<script>
import axios from 'axios';

export default {
    name: 'PantryComponent',
    data() {
        return {
            newIngredient: { ingredient_name: '', ingredient_quantity: '' },
            ingredients: [],
        };
    },
    mounted() {
        this.getIngredients();
    },
    methods: {
        getIngredients() {
            axios
                .get('/api/pantry/')
                .then(response => {
                    this.ingredients = response.data;
                })
                .catch(error => {
                    console.error('Failed to fetch ingredients:', error);
                });
        },
        addIngredient() {
            const ingredientData = {
                ingredient_name: this.newIngredient.ingredient_name.trim(),
                ingredient_quantity: this.newIngredient.ingredient_quantity
            };
            const existingIngredient = this.ingredients.find(ingredient => ingredient.ingredient_name.toLowerCase() === ingredientData.ingredient_name.toLowerCase());

            if (existingIngredient) {
                // Alert the user or handle the duplication as needed
                alert('This ingredient already exists in your pantry.');
                return; // Prevent adding the duplicate ingredient
            }
            axios
                .post('/api/pantry/', ingredientData)
                .then(response => {
                    this.ingredients.push(response.data);
                    this.newIngredient = { ingredient_name: '', ingredient_quantity: '' };
                })
                .catch(error => {
                    console.error('Failed to add ingredient:', error);
                });
        },
        deleteIngredient(id) {
            axios
                .delete(`/api/pantry/${id}/`)
                .then(() => {
                    this.ingredients = this.ingredients.filter(ingredient => ingredient.id !== id);
                })
                .catch(error => {
                    console.error('Failed to delete ingredient:', error);
                });
        },
    },
};
</script>
  
  
<style scoped>
.add-ingredients {
    max-width: 600px;
    margin: 0 auto;
    /* Center align the box */
    background-color: white;
    border: 1px solid #ccc;
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.add-ingredients h1 {
    text-align: center;
    font-size: 1.5em;
    font-weight: bold;
}

.add-ingredients form {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
}

.add-ingredients input[type="text"] {
    width: 70%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

.add-ingredients button {
    width: 25%;
    padding: 10px;
    background-color: rgb(134, 212, 208);
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.add-ingredients button:hover {
    background-color: rgb(52, 136, 131);
}

.add-ingredients ul {
    list-style-type: none;
    padding: 0;
}

.add-ingredients li {
    margin-bottom: 10px;
    background-color: #f9f9f9;
    padding: 10px;
    border-radius: 4px;
}
</style>