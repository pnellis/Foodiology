<template>
    <div class="mb-6 flex items-center justify-between">
        <div class="flex items-center space-x-6">
            <img :src="post.created_by.get_avatar" class="w-[40px] rounded-full">
            <p>
                <strong>
                    <RouterLink :to="{name: 'profile', params:{'id': post.created_by.id}}">{{ post.created_by.name }}</RouterLink>
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
            <h3 class="font-semibold">Ingredients:</h3>
            <p>{{ post.ingredients }}</p >
        </div>
        <div class="my-4"></div>
        <div>
            <h3 class="font-semibold">Steps:</h3>
            <p>{{ post.instructions }}</p >
        </div>
        <div v-if="post.image">
            < img: src="post.image" alt="Recipe Image" class="max-w-full h-auto rounded-lg">
        </div>
    </div>
    
    <div class="my-6 flex justify-between">
        <div class="flex space-x-6">
            <div class="flex items-center space-x-2" @click="likePost(post.id)">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M17.593 3.322c1.1.128 1.907 1.077 1.907 2.185V21L12 17.25 4.5 21V5.507c0-1.108.806-2.057 1.907-2.185a48.507 48.507 0 0 1 11.186 0Z" />
                  </svg>                   
                
                <span class="text-gray-500 text-xs"> {{ post.likes_count }} likes </span>
            </div>
            
            <div class="flex items-center space-x-2">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 01-.923 1.785A5.969 5.969 0 006 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337z"></path>
                </svg> 
    
                <RouterLink :to="{name: 'postview', params: {id: post.id}}" class="text-gray-500 text-xs">{{ post.comments_count }} comments</RouterLink>
            </div>
        </div>
        
        <div>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 12.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 18.75a.75.75 0 110-1.5.75.75 0 010 1.5z"></path>
            </svg>   
        </div>   
    </div>
</template>

<script>
import axios from 'axios'

export default {
props: {
    post: Object
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
    }
}
}
</script>