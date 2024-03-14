<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-1">
            <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
                <img src="@/assets/logocat.png" class="mb-6 rounded-full">
                
                <p><strong>Your Name</strong></p>

                <div class="mt-6 flex space-x-8 justify-around">
                    <p class="text-xs text-gray-500">82 saves</p>
                    <p class="text-xs text-gray-500">2 recipes</p>
                </div>
            </div>
        </div>

        <div class="main-center col-span-2 space-y-4">
            <div class="bg-white border border-gray-200 rounded-lg">
                <!-- <div class="p-4">  
                    <textarea class="p-4 w-full bg-gray-100 rounded-lg" placeholder="Input your own recipe"></textarea>
                </div>

                <div class="p-4 border-t border-gray-100 flex justify-between">
                    <a href="#" class="inline-block py-4 px-6 bg-gray-600 text-white rounded-lg">Attach image</a>

                    <a href="#" class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg">Post</a>
                </div> -->
                <div class="p-8">  
                    <form @submit.prevent="postRecipe" class="space-y-4">
                      <div>
                        <label for="recipeName" class="block text-sm font-medium text-gray-700">Recipe Name:</label>
                        <input v-model="recipeName" id="recipeName" class="input-field" placeholder="Enter recipe name" />
                      </div>
              
                      <div>
                        <label for="recipeDescription" class="block text-sm font-medium text-gray-700">Recipe Description:</label>
                        <textarea v-model="recipeDescription" id="recipeDescription" class="input-field" placeholder="Enter recipe description"></textarea>
                      </div>
              
                      <div>
                        <label for="ingredients" class="block text-sm font-medium text-gray-700">Ingredients:</label>
                        <textarea v-model="ingredients" id="ingredients" class="input-field" placeholder="Enter ingredients with quantities"></textarea>
                      </div>
              
                      <div>
                        <label for="recipeSteps" class="block text-sm font-medium text-gray-700">Recipe Steps:</label>
                        <textarea v-model="recipeSteps" id="recipeSteps" class="input-field" placeholder="Enter recipe steps"></textarea>
                      </div>
              
                      <div class="flex justify-between">
                        <a href="#" class="inline-block py-4 px-6 bg-gray-600 text-white rounded-lg">Attach image</a>
                        <button type="submit" class="inline-block py-4 px-6 bg-pink-600 text-white rounded-lg">Post</button>
                      </div>
                    </form>
                  </div>
            </div>

            <div class="p-4 bg-white border border-gray-200 rounded-lg">
                <div class="mb-6 flex items-center justify-between">
                    <div class="flex items-center space-x-6">
                        <img src="@/assets/logocat.png" class="w-[40px] rounded-full">
                        
                        <p><strong>Your name</strong></p>
                        <p>My recipe 1</p>
                    </div>

                    <p class="text-gray-600">18 minutes ago</p>
                </div>

                <img src="@/assets/logocat.png" class="w-full rounded-lg">

                <div class="my-6 flex justify-between">
                    <div class="flex space-x-6">
                        <div class="flex items-center space-x-2">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z"></path>
                            </svg>  
                            
                            <span class="text-gray-500 text-xs"> 82 saves</span>
                        </div>
                        
                        <div class="flex items-center space-x-2">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 01-.923 1.785A5.969 5.969 0 006 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337z"></path>
                            </svg> 

                            <span class="text-gray-500 text-xs">0 reviews</span>
                        </div>
                    </div>
                    
                    <div>
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 12.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 18.75a.75.75 0 110-1.5.75.75 0 010 1.5z"></path>
                        </svg>   
                    </div>   
                </div>  
            </div>

            <div class="p-4 bg-white border border-gray-200 rounded-lg">
                <div class="mb-6 flex items-center justify-between">
                    <div class="flex items-center space-x-6">
                        <img src="@/assets/logocat.png" class="w-[40px] rounded-full">
                        
                        <p><strong>Your Name</strong></p>
                        
                    </div>

                    <p class="text-gray-600">18 minutes ago</p>
                </div>

                <p>Your Review on Recipe 1
                
                </p>

                <div class="my-6 flex justify-between">
                    <div class="flex space-x-6">
                        <div class="flex items-center space-x-2">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z"></path>
                            </svg>  
                            
                            <span class="text-gray-500 text-xs">82 likes</span>
                        </div>
                        
                        <div class="flex items-center space-x-2">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 01-.923 1.785A5.969 5.969 0 006 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337z"></path>
                            </svg> 

                            <span class="text-gray-500 text-xs">0 comments</span>
                        </div>
                    </div>
                    
                    <div>
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 12.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 18.75a.75.75 0 110-1.5.75.75 0 010 1.5z"></path>
                        </svg>   
                    </div>   
                </div>  
            </div>
        </div>



        <div class="main-right col-span-1 space-y-4">
            <RecommendedRecipes/>
            <TrendingRecipes/>
            
                
        </div>
    </div>
</template>

<script>
import RecommendedRecipes from '../components/RecommendedRecipes.vue'
import TrendingRecipes from '../components/TrendingRecipes.vue';

export default {
    name: 'FeedView',
    components: {
        RecommendedRecipes,
        TrendingRecipes,
    }
}
</script>