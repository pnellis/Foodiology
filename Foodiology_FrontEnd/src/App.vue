<template>
  <nav class="py-10 px-8 border-b border-gray-200">
    <div class="nav-container flex flex-row md:flex-row justify-between items-center max-w-7xl mx-auto">
      <div class="menu-left flex-shrink-0">
        <RouterLink to="/" class="icon-container">
          <a href="#" class="text-xl" style="display: flex; align-items: center;">
            <img src="/public/assets/logocat.png" class="logo-cat">
            <img src="/public/assets/foodiology.png" alt="Foodiology Logo" class="logo-image">
          </a>
        </RouterLink>
      </div>

      <div class="menu-center flex-grow justify-center flex space-x-12">
        <RouterLink to="/" class="icon-container">
          <div class="tooltip">Home</div>
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
            class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round"
              d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
          </svg>
        </RouterLink>

        <RouterLink to="/search" class="icon-container">
          <div class="tooltip">Search Recipes</div>
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
            class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round"
              d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"></path>
          </svg>
        </RouterLink>

        <template v-if="userStore.user.isAuthenticated">
          <RouterLink to="/find" class="icon-container">
            <div class="tooltip">Find Friends</div>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
              stroke="currentColor" class="w-6 h-6">
              <path stroke-linecap="round" stroke-linejoin="round"
                d="M15 19.128a9.38 9.38 0 0 0 2.625.372 9.337 9.337 0 0 0 4.121-.952 4.125 4.125 0 0 0-7.533-2.493M15 19.128v-.003c0-1.113-.285-2.16-.786-3.07M15 19.128v.106A12.318 12.318 0 0 1 8.624 21c-2.331 0-4.512-.645-6.374-1.766l-.001-.109a6.375 6.375 0 0 1 11.964-3.07M12 6.375a3.375 3.375 0 1 1-6.75 0 3.375 3.375 0 0 1 6.75 0Zm8.25 2.25a2.625 2.625 0 1 1-5.25 0 2.625 2.625 0 0 1 5.25 0Z" />
            </svg>
          </RouterLink>

          <RouterLink to="/feed" class="icon-container">
            <div class="tooltip">Feed</div>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
              stroke="currentColor" class="w-6 h-6">
              <path stroke-linecap="round" stroke-linejoin="round"
                d="M8.625 9.75a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0H8.25m4.125 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0H12m4.125 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0h-.375m-13.5 3.01c0 1.6 1.123 2.994 2.707 3.227 1.087.16 2.185.283 3.293.369V21l4.184-4.183a1.14 1.14 0 01.778-.332 48.294 48.294 0 005.83-.498c1.585-.233 2.708-1.626 2.708-3.228V6.741c0-1.602-1.123-2.995-2.707-3.228A48.394 48.394 0 0012 3c-2.392 0-4.744.175-7.043.513C3.373 3.746 2.25 5.14 2.25 6.741v6.018z">
              </path>
            </svg>
          </RouterLink>
        </template>

        <RouterLink to="/about" class="icon-container">
          <div class="tooltip">About</div>
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
            class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round"
              d="M14.857 17.082a23.848 23.848 0 005.454-1.31A8.967 8.967 0 0118 9.75v-.7V9A6 6 0 006 9v.75a8.967 8.967 0 01-2.312 6.022c1.733.64 3.56 1.085 5.455 1.31m5.714 0a24.255 24.255 0 01-5.714 0m5.714 0a3 3 0 11-5.714 0">
            </path>
          </svg>
        </RouterLink>
      </div>

      <div class="menu-right flex-shrink-0">
        <template v-if="userStore.user.isAuthenticated">
          <RouterLink :to="{ name: 'profile', params: { 'id': userStore.user.id } }">
	  <img :src="avatarSrc" class="w-12 rounded-full" alt='User Avatart'>
          </RouterLink>
        </template>

        <template v-else>
          <RouterLink to="/login" class="py-2 px-4 bg-gray-600 text-white rounded-md">Log in</RouterLink>
          <RouterLink to="/signup" class="ml-2 py-2 px-4 bg-pink-600 text-white rounded-md">Sign up</RouterLink>
        </template>
      </div>
    </div>
  </nav>

  <div id="app">
    <main :class="mainClass">
      <RouterView />
    </main>
  </div>
  <Toast />
</template>

<script>
import axios from 'axios'
import RecommendedRecipes from '@/components/RecommendedRecipes.vue'
import TrendingRecipes from '@/components/TrendingRecipes.vue'
import FeedItem from '@/components/FeedItem.vue'
import PantryComponent from '@/components/PantryComponent.vue';
import { useUserStore } from '@/stores/user'
import { useToastStore } from '@/stores/toast'
import Toast from '@/components/Toast.vue'

export default {
  name: 'FeedView',
  setup() {
    const userStore = useUserStore()

    return {
      userStore
    }
  },

  components: {
    Toast,
    FeedItem
  },


  // mounted() {
  //   this.getFeed()
  // },

  data() {
    return {
      posts: [],
      user: {
        id: null
      },
      can_send_friendship_request: null,
      body: '',
    }
  },

  watch: {
    '$route.params.id': {
      handler: function (newId) {
        if (newId != null) {
          this.getFeed()
        }
      },
      immediate: true
    }
  },

  methods: {
    getFeed() {
      axios
        .get(`/api/posts/profile/${this.$route.params.id}/`)
        .then(response => {
          console.log('data', response.data)

          this.posts = response.data.posts
          this.user = response.data.user
          this.can_send_friendship_request = response.data.can_send_friendship_request

        })
        .catch(error => {
          console.log('error', error)
        })
    },

    sendFriendshipRequest() {
      axios
        .post(`/api/friends/${this.$route.params.id}/request/`)
        .then(response => {
          console.log('data', response.data)

          this.can_send_friendship_request = false

          if (response.data.message == 'request already sent') {
            this.toastStore.showToast(5000, 'The request has already been sent!', 'bg-red-300')
          } else {
            this.toastStore.showToast(5000, 'The request was sent!', 'bg-emerald-300')
          }
        })
        .catch(error => {
          console.log('error', error)
        })
    },

    submitForm() {
      console.log('submitForm', this.body)

      axios
        .post('/api/posts/create/', {
          'body': this.body
        })
        .then(response => {
          console.log('data', response.data)

          this.posts.unshift(response.data)
          this.body = ''
          this.user.posts_count += 1
        })
        .catch(error => {
          console.log('error', error)
        })
    },

    logout() {
      console.log('Log out')

      this.userStore.removeToken()

      this.$router.push('/login')
    }
  },

  beforeCreate() {
    this.userStore.initStore()

    const token = this.userStore.user.access

    if (token) {
      axios.defaults.headers.common["Authorization"] = "Bearer " + token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },
  computed: {
    mainClass() {
      // Define the routes that should have the specific style
      const styledRoutes = ['/', '/about', '/login'];
      // Check if the current route is one of the styled routes /friends/${this.$route.params.id}/request/`
      if (styledRoutes.includes(this.$route.path)) {
        return ' '; // Apply no style
      }
      return 'px-8 py-6 bg-gray-100'; // Default style
    },
    avatarSrc() {
	return (this.userStore.user.avatar === null || this.userStore.user.avatar === "null") ? '/assets/logocat.png' : this.userStore.user.avatar;
    }
  }
}

</script>

<style>
.menu-center .icon-container {
  position: relative;
  display: flex;
}


.menu-center .icon-container:hover .tooltip {
  display: block;
}

.menu-center .icon-container .tooltip {
  display: none;
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  background-color: pink;
  padding: 8px;
  border-radius: 4px;
  color: white;
  z-index: 1;
}

.menu-center .icon-container:hover .icon {
  color: pink;
}

.nav-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  /* flex-wrap: wrap; */
  /* Allow items to wrap onto multiple lines */
}

.logo-cat {
  width: 10vw;
  /* Make logo scalable */
  max-width: 80px;
  /* Set max width for logo */
  height: auto;
  /* Maintain aspect ratio */
  margin-right: 8px;
}

.logo-image {
  width: 20vw;
  /* Make logo scalable */
  max-width: 250px;
  /* Set max width for logo */
  height: auto;
  /* Maintain aspect ratio */
  margin-right: 8px;
}

/* Add styles for icon links and user authentication links as needed */
</style>
