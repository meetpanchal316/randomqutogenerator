# Random Quote Generator

A full-stack random quote generator app.

## Structure
- `frontend/`: Express server serving HTML/JS frontend (port 3000)
- `backend/`: Flask API fetching quotes from quotable.io (port 5000, CORS restricted to frontend)

## Running
1. Backend: `cd backend && pip install -r requirements.txt && python app.py`
2. Frontend: `cd frontend && npm install && npm start`

Open http://localhost:3000 to use the app.