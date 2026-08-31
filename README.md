# A. Sheik Farith — Portfolio

A production-oriented full stack developer portfolio with a React/Vite frontend and FastAPI/SQLAlchemy backend. It showcases practical Python, REST API, LangChain/RAG and full-stack experience, and includes a functional contact-message API.

## Features

- Responsive dark portfolio with accessible navigation, motion, and loading/error states
- API-powered skills, projects, and experience sections
- Validated contact form that stores messages through FastAPI
- MySQL-ready SQLAlchemy models and seed data
- Clean component and router structure

## Tech stack

**Frontend:** React, Vite, JavaScript, CSS, Lucide icons  
**Backend:** FastAPI, SQLAlchemy, Pydantic  
**Database:** MySQL via PyMySQL

## Folder structure

```
src/                 React components, service, and styles
backend/app/         FastAPI routes, models, schemas, and seed service
backend/requirements.txt
```

## Run locally

1. Copy `.env.example` to `backend/.env` and set `DATABASE_URL` for MySQL.
2. Create a MySQL database: `CREATE DATABASE portfolio_db CHARACTER SET utf8mb4;`
3. Start the API:

   ```powershell
   cd backend
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```

4. In another terminal, install and start the frontend:

   ```powershell
   npm install
   npm run dev
   ```

The frontend runs at `http://localhost:5173`; documentation is at `http://localhost:8000/docs`.

## Environment variables

`DATABASE_URL` takes precedence. Or use `DB_HOST`, `DB_USER`, `DB_PASSWORD`, and `DB_NAME` to build a MySQL URL. Configure `CORS_ORIGINS` as a comma-separated list.

## API endpoints

| Method | Endpoint | Purpose |
| --- | --- | --- |
| GET | `/api/projects` | Portfolio projects |
| GET | `/api/skills` | Skills grouped by category |
| GET | `/api/experience` | Professional experience |
| POST | `/api/contact` | Validate and store a contact message |

## Deployment (Railway)

The included `Dockerfile` builds the React site and serves it through FastAPI from one Railway domain.

1. Create a Railway project and add a **MySQL** service.
2. Add a new service from this project’s source and deploy it. Railway detects the root `Dockerfile`.
3. In the web service **Variables** tab, add the following (use Railway reference variables from the MySQL service):

   ```env
   DATABASE_URL=mysql+pymysql://${{MySQL.MYSQLUSER}}:${{MySQL.MYSQLPASSWORD}}@${{MySQL.MYSQLHOST}}:${{MySQL.MYSQLPORT}}/${{MySQL.MYSQLDATABASE}}
   CORS_ORIGINS=https://${{RAILWAY_PUBLIC_DOMAIN}}
   ```

4. In **Settings → Networking**, generate a public domain. Open `/health` to verify the service; opening the root domain displays the portfolio.

Railway’s deployed MySQL database is separate from local XAMPP/phpMyAdmin. The API creates its portfolio tables and seeds its portfolio data on first startup.
