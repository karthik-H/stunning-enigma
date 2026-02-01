# JSONPlaceholder User Fetcher

## Overview
This application retrieves user information from the JSONPlaceholder API using a clean, layered architecture (controller → service → domain → repository). It is production-ready, modular, and follows Python best practices.

## Folder Structure
```
├── src/
│   ├── config/
│   │   └── config.py
│   ├── controller/
│   │   └── user_controller.py
│   ├── domain/
│   │   └── user.py
│   ├── repository/
│   │   └── user_repository.py
│   ├── service/
│   │   └── user_service.py
│   └── main.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository**
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure environment variables**
   - Edit `.env` if you need to change the API URL (default is set for JSONPlaceholder)
4. **Run the application**
   ```bash
   python src/main.py
   ```

## Configuration
- All environment variables are managed in `.env` and loaded via `python-dotenv`.
- The API URL is set in `.env` as `JSONPLACEHOLDER_API_URL`.

## Logging & Error Handling
- Errors and connectivity issues are logged using Python's `logging` module.
- The application will print a user-friendly message if it fails to retrieve users.

## Extensibility
- The codebase is modular and can be extended for additional endpoints or business logic.

## Notes
- Only GET operations are implemented as per requirements.
- No authentication is required for the JSONPlaceholder API.
