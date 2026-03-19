# Notes App (Demo README)

A full-stack notes application built with **Django REST Framework** and **Next.js**.

The app supports authentication, category-based organization, and CRUD note management with a clean dashboard UI.

## 1) Technologies Used

### Frontend
- **Next.js 16** (App Router)
- **React 19**
- **Tailwind CSS v4**
- **Axios** (API client + auth interceptor)

### Backend
- **Python 3 / Django 4**
- **Django REST Framework**
- **SimpleJWT** (access + refresh tokens)
- **django-cors-headers**

### Database
- **PostgreSQL 16** (Docker environment)
- **SQLite** (local fallback when `DATABASE_URL` is not set)

### DevOps / Runtime
- **Docker / Docker Compose**
- Separate containers for frontend, backend, and database

## 2) Project Features

- Signup, login, logout
- JWT authentication with automatic token refresh
- Notes CRUD (create, read, update, delete)
- Category filtering and note counts
- Protected routes on frontend middleware
- User-level data isolation (users only see their own notes)

## 3) Architecture Overview

### Frontend flow
- UI calls backend through `NEXT_PUBLIC_API_URL`
- Access token is attached on each request
- On `401`, frontend tries refresh token once, retries request, otherwise logs out

### Backend flow
- `POST /api/auth/signup/` creates user and returns JWT tokens
- `POST /api/auth/login/` returns JWT tokens
- Notes endpoints require authentication
- Custom ownership permission enforces per-user access

## 4) Setup & Run

## Option A: Docker (recommended for demo)

From project root:

```bash
docker compose up --build
```

Services:
- Frontend: `http://localhost:3000`
- Backend: `http://localhost:8000`
- DB: PostgreSQL container (`db` service, persisted in `postgres_data` volume)

Stop:

```bash
docker compose down
```

Full reset (including DB data):

```bash
docker compose down -v
```

## Option B: Local run (without Docker)

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:3000`.

## 5) Demo Script (Suggested)

1. Open signup page and create a user.
2. Show redirect to dashboard after successful auth.
3. Create a note and assign a category.
4. Filter notes by category from sidebar.
5. Edit and delete a note.
6. Log out and log back in.
7. (Optional) Show API endpoints in browser network tab.

## 6) README Requirement: Summary of Process

I built this project in iterative stages:

1. Set up backend API modules (accounts, categories, notes).
2. Added JWT auth and signup/login flow.
3. Implemented user-scoped note CRUD with category filtering.
4. Built frontend auth forms and protected dashboard routes.
5. Added Axios interceptors for token attach/refresh.
6. Debugged integration issues (CORS, validation errors, native frontend dependency issues).
7. Added complete Docker workflow and PostgreSQL service for reproducible demo setup.

## 7) README Requirement: Key Design & Technical Decisions

- **JWT-based auth** for stateless API interaction.
- **Refresh-token retry** in frontend interceptor to improve UX on token expiry.
- **Per-user query scoping + object-level permission** for notes security.
- **Read-only categories** seeded and managed by backend to keep taxonomy consistent.
- **Dockerized Postgres** for realistic demo environment.
- **SQLite fallback** preserved for lightweight local development.

## 8) README Requirement: AI Tools Used and How

AI-assisted development was used as a coding copilot and debugger.

- **OpenAI Codex / ChatGPT-style assistant**:
  - Generated and refactored implementation code.
  - Helped debug integration issues (frontend build error, CORS mismatch, validation handling).
  - Produced Dockerization artifacts (`Dockerfile`, `docker-compose.yml`) and setup docs.
  - Helped improve developer UX by surfacing backend validation messages in frontend.

How it was used in practice:
- Iterative prompt -> code update -> run/test -> inspect logs/network -> refine.
- AI outputs were validated manually through local execution, API responses, and browser checks.

## 9) Known Limitations / Next Improvements

- Current backend uses Django dev server (fine for demo, replace with Gunicorn for production).
- Authentication token is stored in localStorage (can migrate to httpOnly cookies for stronger security).
- Additional automated tests can be added for API and UI flows.

## 10) Key Files

- Backend settings: `backend/config/settings.py`
- Auth API: `backend/apps/accounts/`
- Notes API: `backend/apps/notes/`
- Frontend API client: `frontend/lib/api.js`
- Docker orchestration: `docker-compose.yml`
