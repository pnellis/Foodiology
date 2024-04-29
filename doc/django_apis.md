## API Overview
Foodiology's back-end is run through a Django project with multiple Django Apps.

## Account

Account is used to store and retrieve user information and user interactions with other users. The following API functions can be found in the Account app:

1. **me**: Returns a user's unique id in the Foodiology database, the user's name, the user's email address, and the user's avatar (if provided)
2. **signup**: Creates a user account. Requires a user to input their name, email address, and set a password (typed in twice for conformation). The account will require the user to verify their email before being activated.
3. **friends**: Returns a user and other users that they have are Foodiology friends with.
4. **editprofile**: Updates a user's email address or name. If the new email that a user provides is already in our database a user will be unable to update their email.
5. **editpassword**: Updates a user's password.
6. **send_friendship_request**: Creates a friendship request from one user to another. Prevents duplicate requests.
7. **handle_request**: Allows the user to accept or reject a friendship request. If accepted, both users are added as friends of one another.

## Find
1. **find**: Allows a user to search for and find other user accounts.

## Post

Post allows users to create their own recipes, as well as comment on and like other recipes. The following API functions can be found in the Post app:

1. **post_list**: Retrieves posts made by a user's friends.
2. **post_detail**: Retrieves the contents of a specified post.
3. **post_list_profile**: Retrieves a different user's profile information, including their public profile information, the option to send a friendship request (if the two users are not already friends), and their posted recipes.
4. **post_create**: 
5. **post_like**: Allows a user to like a recipe.
6. **post_create_comment**: Allows a user to post a comment on a recipe.
7. **post_delete**: Delete's a user's post.
8: **post_report**: Allows a user to report another user's post (posts that may contain offensive content).

## Search

Search allows users to search recipes by ingredients, as well as time, yield, meal type, cuisine, and nutrient information. This app contains 1 API function:

1. **find**: Allows users to search recipes by input parameters (primarily ingredient). Returns recipes that match input parameters.

## Pantry

Pantry allows users to store a list of the ingredients that they currently have available.

1. **pantry_list**: Allows a user to initially input an ingredient into their pantry, then subsequently displays the ingredient.
2. **pantry_detail**: Allows a user to edit their pantry ingredients.
