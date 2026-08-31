# Django REST Framework API

A Django REST Framework API implementing user authentication with JWT, user profiles, and announcements.

## Features

* User registration
* JWT authentication
* JWT token refresh
* User profile
* Update profile
* Announcements
* Authentication and permission handling
* PostgreSQL database
* Environment-based configuration

## Requirements

* Python 3.12+
* Django
* Django REST Framework
* PostgreSQL
* `uv`

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd <project-directory>
```

### 2. Create a virtual environment

```bash
uv venv
```

Activate it:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
uv sync
```

## Environment Variables

The project uses environment variables for sensitive configuration such as the Django secret key and database credentials.

A `.env.example` file is included as a template.

Create your local `.env` file:

```bash
cp .env.example .env
```

Then update `.env` with your own values.

## Database Setup

Make sure PostgreSQL is running and that the database specified in `.env` exists.

Run migrations:

```bash
uv run python manage.py migrate
```

## Run the Server

Start the development server:

```bash
uv run python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

## API Endpoints

### Authentication

#### Register

```http
POST /api/register/
```

Example request:

```json
{
    "username": "username",
    "email": "user@example.com",
    "password": "your-password",
    "password2": "your-password"
}
```

#### Login

```http
POST /api/login/
```

Returns an access token and refresh token.

Example request:

```json
{
    "username": "username",
    "password": "your-password"
}
```

#### Refresh Token

```http
POST /api/token/refresh/
```

Example:

```json
{
    "refresh": "your-refresh-token"
}
```

### Profile

Authentication is required for profile endpoints.

#### Get Profile

```http
GET /api/profile/
```

Include the access token:

```http
Authorization: Bearer <access-token>
```

#### Update Profile

```http
PATCH /api/profile/
```

Example:

```json
{
    "bio": "My bio",
    "avatar_url": "https://example.com/avatar.jpg"
}
```

### Announcements

Authentication is required.

#### List Announcements

```http
GET /api/announcements/
```

#### Create Announcement

```http
POST /api/announcements/
```

Example:

```json
{
    "title": "Announcement title",
    "content": "Announcement content"
}
```

The authenticated user is automatically assigned as the author.

## JWT Authentication

The API uses JSON Web Tokens for authentication.

After logging in, use the returned access token in authenticated requests:

```http
Authorization: Bearer <access-token>
```

The access token should be used for requests to protected endpoints such as:

```text
/api/profile/
/api/announcements/
```

## Testing the API

You can test the endpoints using tools such as:

* Postman
* Insomnia
* `curl`

Example:

```bash
curl -X GET http://127.0.0.1:8000/api/profile/ \
  -H "Authorization: Bearer <access-token>"
```

