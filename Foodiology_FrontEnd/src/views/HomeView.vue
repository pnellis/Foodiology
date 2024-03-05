<template>
  <main>
    
    <div class="welcome-container">
      <h1>Welcome to Foodiology!</h1>
      <p>Discover, Share, and Enjoy Amazing Recipes.</p>
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
  align-items: center;
  height: 100vh;
}
.welcome-container {
  /* text-align: center;
  max-width: 600px; */
  position: relative;
  width: 100%;
  height: 100vh; /* Adjust the height as needed */
  background-image: url('@/assets/HomePhoto.jpg');
  background-size: cover;
  background-position: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
}
h1 {
  font-size: 3rem;
  margin-bottom: 16px;
  color: #ffffff;
}

p {
  font-size: 1.5rem;
  margin-bottom: 24px;
  color: #ffffff;
}

.search-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 12px 24px;
  font-size: 1.25rem;
  background-color: #D53F8C;
  color: white;
  text-decoration: none;
  border-radius: 8px;
  transition: background-color 0.3s ease;
}

.search-button:hover {
  background-color: #4c51bf;
}

.home-background {
  background-image: url("@/assets/HomePhoto.jpg");
  background-size: contain;
  background-position: center;
  background-repeat: no-repeat;
  height: 200vh; /* Adjust the height as needed */
  margin: 0;
  padding: 0;
}

</style>