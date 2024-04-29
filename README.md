# Foodiology_Test

This template should help get you started developing with Vue 3 in Vite.

## Introduction
FoodiologyRecipes.com is a web application to provide users with a community to share and search for recipes. To be able to like, post, and comment on recipes, and save ingredients to the pantry you must create an account. However, all users (with or without an account) are able to search for recipes based on ingredients they input directly into the search bar. 

## Purpose
Foodiologyrecipes.com is great for individuals who have a variety of ingredients, but don’t know what to cook using them. Our website provides a platform for people to input their ingredients, select a preferred cuisine type, time needed to prepare, servings yield, and meal type (breakfast, lunch, dinner, beverage, dessert). 

## Key Features

* **Search Recipes:** Search recipes based on ingredients you input, preferred cuisine type, time needed to prepare, servings yield, and meal type (breakfast, lunch, dinner, beverage, dessert).
* **Random Recipe of the Day:** A random recipe of the day will be shown from the databse.
* **Create an Account:** Create an account (email verification needed).
* **Edit Profile:** Users with accounts can change their name, change their email, and update their passowrd.
* **Comment on Posts:** Users with accounts and are logged in can comment on recipe posts.
* **Add Friends:** Users can go to "Find Friends" and search for other users to view their recipes and add them as friends.
* **Pantry:** Users with accounts can save ingredients to their pantry. After a user has saved 


## How to Run locally

To get started with our project on the local version, you must first create an environment to hold all relevant libraries and packages. To do this, open a terminal in the folder where you have cloned the repository type and the following:
  * Cd Foodiology_FrontEnd
  * npm install axios 
  * Python3 -m venv env
  * source env/bin/activate
  * pip3 install django 
  * pip3 install djangorestframework
  * pip3 install djangorestframework-simplejwt
  * pip3 install pillow
  * pip3 install django-cors-headers
  * pip3 install pymysql
To run the backend:
  * cd Foodiology_BackEnd
  * python manage.py runserver 
To run the front end:
  * cd Foodiology_FrontEnd
  * npm run dev

### See further documentation in the Foodiology wiki!

