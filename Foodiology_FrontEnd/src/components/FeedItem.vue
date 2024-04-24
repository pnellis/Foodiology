<template>
    <div class="mb-6 flex items-center justify-between">
        <div class="flex items-center space-x-6">
            <img :src="post.created_by.get_avatar || '/src/assets/logocat.png'" class="w-[40px] rounded-full">
            <p>
                <strong>
                    <RouterLink :to="{ name: 'profile', params: { 'id': post.created_by.id } }">{{ post.created_by.name }}
                    </RouterLink>
                </strong>
            </p>
        </div>
        <p class="text-gray-600">{{ post.created_at_formatted }}</p>
    </div>

    <!-- Displaying the recipe details -->
    <div class="recipe-details">
        <h2 class="font-bold text-xl">{{ post.title }}</h2>
        <div class="my-4"></div>
        <div>
            <img v-if="!post.image_url" v-for="image in post.attachments" :key="image.id" :src="image.get_image"
                class="responsive-image rounded-lg">

            <img v-else :src="post.image_url" alt="Recipe Image" class="responsive-image rounded-lg">
        </div>
        <div class="my-4"></div>
        <div>
            <h3 class="font-semibold">Ingredients:</h3>
            <!-- <p>{{ post.ingredients }}</p > -->
            <ul>
                <li v-for="ingredient in post.ingredients.split(',')" :key="ingredient">- {{ ingredient.trim() }}</li>
            </ul>
        </div>
        <div class="my-4"></div>
        <div>
            <h3 class="font-semibold">Steps:</h3>
            <!-- <p>{{ post.instructions }}</p > -->
            <ul>
                <li v-for="step in post.instructions.split('.')" :key="step">- {{ step.trim() }}.</li>
            </ul>
        </div>
        <div class="my-4"></div>
        <div>
            <h3 class="font-semibold">Total Time:</h3>
            <p>{{ post.total_time }}</p>
        </div>
        <div class="my-4"></div>
        <div>
            <h3 class="font-semibold">Yields:</h3>
            <p>{{ post.yields }}</p>
        </div>
        <div class="my-4"></div>
        <div>
            <h3 class="font-semibold">Meal Type:</h3>
            <p>{{ post.meal_type }}</p>
        </div>
        <div class="my-4"></div>
        <div>
            <h3 class="font-semibold">Cuisine Type:</h3>
            <p>{{ post.cuisine_type }}</p>
        </div>
        <div class="my-4"></div>
        <div>
            <h3 class="font-semibold">Nutrient:</h3>
            <!-- <p>{{ post.nutirents }}</p > -->
            <ul>
                <li v-for="nutrient in post.nutirents.split(',')" :key="nutrient">{{ nutrient.trim() }}</li>
            </ul>
        </div>
    </div>

    <div class="my-6 flex justify-between">
        <div class="flex space-x-6">
            <div class="flex items-center space-x-2" @click="likePost(post.id)">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                    stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round"
                        d="M17.593 3.322c1.1.128 1.907 1.077 1.907 2.185V21L12 17.25 4.5 21V5.507c0-1.108.806-2.057 1.907-2.185a48.507 48.507 0 0 1 11.186 0Z" />
                </svg>

                <span class="text-gray-500 text-xs"> {{ post.likes_count }} likes </span>
            </div>

            <div class="flex items-center space-x-2">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                    stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round"
                        d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 01-.923 1.785A5.969 5.969 0 006 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337z">
                    </path>
                </svg>

                <RouterLink :to="{ name: 'postview', params: { id: post.id } }" class="text-gray-500 text-xs">{{
                    post.comments_count }} comments</RouterLink>
            </div>
        </div>

        <div>
            <div @click="toggleExtraModal">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                    stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round"
                        d="M12 6.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 12.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 18.75a.75.75 0 110-1.5.75.75 0 010 1.5z">
                    </path>
                </svg>
            </div>
        </div>
    </div>

    <div v-if="showExtraModal">
        <div class="flex space-x-6 items-center">
            <div class="flex items-center space-x-2" @click="deletePost" v-if="userStore.user.id == post.created_by.id">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                    stroke="currentColor" class="w-6 h-6 text-red-500">
                    <path stroke-linecap="round" stroke-linejoin="round"
                        d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0" />
                </svg>

                <span class="text-red-500 text-xs">Delete post</span>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    props: {
        post: Object
    },

    emits: ['deletePost'],

    data() {
        return {
            showExtraModal: false
        }
    },

    methods: {
        // formatDate(datetime) {
        //     const options = { year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric' };
        //     return new Date(datetime).toLocaleDateString('en-US', options);
        // },
        formatDate(datetime) {
            const options = { year: 'numeric', month: 'short', day: 'numeric', hour: 'numeric', minute: 'numeric', second: 'numeric', hour12: true };
            return new Date(datetime).toLocaleDateString('en-US', options);
        },
        likePost(id) {
            axios
                .post(`/api/posts/${id}/like/`)
                .then(response => {
                    if (response.data.message == 'like created') {
                        this.post.likes_count += 1
                    }
                })
                .catch(error => {
                    console.log('error', error)
                })
        },
        deletePost() {
            this.$emit('deletePost', this.post.id)

            axios
                .delete(`/api/posts/${this.post.id}/delete/`)
                .then(response => {
                    console.log(response.data)

                    this.toastStore.showToast(5000, 'The post was deleted', 'bg-emerald-500')
                })
                .catch(error => {
                    console.log("error", error);
                })
        },
        toggleExtraModal() {
            console.log('toggleExtraModal')

            this.showExtraModal = !this.showExtraModal
        }
    }
}
</script>

<style scoped>
.avatar {
    width: 40px;
    height: 40px;
    /* Maintain the aspect ratio */
}

.responsive-image {
    max-width: 100%;
    height: auto;
    border-radius: 10px;
}
</style>