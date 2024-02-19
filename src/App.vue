<template>
  <div id="app">
    <header>
      <h1>Foodiology</h1>
      <nav>
        <router-link to="/">Home</router-link>
        <router-link to="/login">Login</router-link>
        <!-- Add more navigation links as needed -->
      </nav>
    </header>

    <main>
      <router-view></router-view>
    </main>

    <footer>
      <!-- Add footer content if needed -->
    </footer>
  </div>
</template>

<style>
#app {
  font-family: 'Arial', sans-serif;
  text-align: center;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

header {
  background-color: #fabbe0;
  color: white;
  padding: 20px;
}

nav {
  display: flex;
  justify-content: space-around;
  margin-top: 10px;
}

nav a {
  text-decoration: none;
  color: white;
  font-weight: bold;
}

main {
  margin-top: 20px;
}

footer {
  margin-top: 20px;
  padding: 10px;
  background-color: #f1f1f1;
}
</style>
