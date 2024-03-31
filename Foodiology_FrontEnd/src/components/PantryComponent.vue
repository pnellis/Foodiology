<template>
    <div class="add-ingredients">
        <h1>Add Your Ingredients</h1>
        <form @submit.prevent="addIngredient">
            <input type="text" v-model="newIngredient.name" placeholder="Enter ingredient" />
            <input type="text" v-model="newIngredient.amount" placeholder="Enter amount" />
            <button type="submit">Add</button>
        </form>
        <ul>
            <li v-for="(ingredient, index) in ingredients" :key="index">
                {{ ingredient.name }} - {{ ingredient.amount }}
                <button @click="deleteIngredient(index)">Delete</button>
            </li>
        </ul>
    </div>
</template>
  
<script>
export default {
    data() {
        return {
            newIngredient: { name: '', amount: '' },
            ingredients: [],
        };
    },
    methods: {
        addIngredient() {
            if (this.newIngredient.name.trim() && this.newIngredient.amount.trim()) {
                this.ingredients.push({
                    name: this.newIngredient.name.trim(),
                    amount: this.newIngredient.amount.trim()
                });
                this.newIngredient = { name: '', amount: '' };
                localStorage.setItem('ingredients', JSON.stringify(this.ingredients));
            }
        },
        deleteIngredient(index) {
            this.ingredients.splice(index, 1);
            localStorage.setItem('ingredients', JSON.stringify(this.ingredients));
        },
    },
    created() {
        const storedIngredients = localStorage.getItem('ingredients');
        if (storedIngredients) {
            this.ingredients = JSON.parse(storedIngredients);
        }
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
  
  