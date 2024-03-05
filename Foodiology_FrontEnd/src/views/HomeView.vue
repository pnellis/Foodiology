<template>
  <main class="main-background">
    <div class="welcome-container welcome-background">
      <!-- <img src="@/assets/HomePhoto.jpg" alt="Delicious food" class="home-photo"> -->
      <h1>Welcome to Foodiology!</h1>
      <p>Transforming kitchen confusion into delicious discoveries.</p>
          <p>Discover delicious recipes based on your ingredients and preferences!</p>
      <RouterLink to="/search" class="search-button">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-6 h-6">
          <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"></path>
        </svg>
        Search Recipes
      </RouterLink>
    </div>
  </main>
</template>
<style scoped>


main {
  display: flex;
  justify-content: center;
  
  height: 50vh;
}
.welcome-container {
  text-align: center;
  max-width: 800px;
  max-height: 300px;
}

.welcome-background {
  background-color: #f792ac; /* Set the background color to #f792ac */
  padding: 10px; /* Optional: Add padding for better visual appearance */
}

h1 {
  font-size: 3rem;
  margin-bottom: 16px;
  color: #464040;
  font-weight: bold;
}

p {
  font-size: 1.5rem;
  margin-bottom: 24px;
  color: #464040;
  font-weight: bold;
}

.search-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 12px 24px;
  font-size: 1.25rem;
  background-color: rgb(134, 212, 208);
  color: white;
  text-decoration: none;
  border-radius: 8px;
  transition: background-color 0.3s ease;
}

.search-button:hover {
  background-color: rgb(52, 136, 131);
}

main.main-background {
  background-image: url("@/assets/HomePhoto.jpg");
  background-size: contain;
  
  background-repeat: no-repeat;
  height: 200vh; /* Adjust the height as needed */
  margin: 0;
  padding: 0;
}

</style>