## You will require authentication token for all put/patch, post, delete  methods, get method is public api hence you wont need any token.

1. login (POST) 
- endpoint - http://127.0.0.1:8000/api/login/
- payload:
{
    "username": "test",
    "passord": "test@123"
}

2. Get users (GET)
- endpoint - http://127.0.0.1:8000/api/users/

3. Create user (POST)
- endpoint - http://127.0.0.1:8000/api/users/
- payload:
{
    "username": "temp",
    "email": "temp@gmail.com",
    "password": "temp@123"
}

4. Update user (PATCH/PUT)
- endpoint - http://127.0.0.1:8000/api/users/1/
- payload:
{
    "username": "updated temp",
    "email": "temp@gmail.com",
    "password": "temp@123"
}

5. Delete user (DELETE)
- endpoint - http://127.0.0.1:8000/api/users/1/

6. Get posts (GET)
- endpoint - http://127.0.0.1:8000/api/posts/

7. Create post (POST)
- endpoint - http://127.0.0.1:8000/api/posts/
- payload:
{
    "title": "My First Blog Post",
    "description": "This is a test blog post.",
    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "is_public": true"
}

8. Update post (PATCH/PUT)
- endpoint - http://127.0.0.1:8000/api/posts/1/
- payload:
{
    "title": "My First updated Blog Post",
    "description": "This is a test blog post.",
    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "is_public": true"
}

9. Delete post (DELETE)
- endpoint - http://127.0.0.1:8000/api/posts/1/

10. Like post (POST)
- endpoint - http://127.0.0.1:8000/api/posts/1/like/

11. Dislike post (DELETE)
- endpoint - http://127.0.0.1:8000/api/posts/1/unlike/