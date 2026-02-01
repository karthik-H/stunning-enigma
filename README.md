# JSONPlaceholder User Fetcher

## Overview
This application retrieves user information from the JSONPlaceholder API using a clean, layered architecture (controller → service → domain → repository). It is production-ready, modular, and follows Python best practices. The application also saves all retrieved user records to a CSV file for future access and analysis.

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
│   │   ├── user_repository.py
│   │   └── user_csv_repository.py
│   ├── service/
│   │   └── user_service.py
│   └── main.py
├── .env
├── .gitignore
├── requirements.txt
├── README.md
```

## Setup Instructions

1. **Clone the repository**
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure environment variables**
   - Edit `.env` if you need to change the API URL or CSV file path (defaults are set for JSONPlaceholder and `data/users.csv`)
4. **Run the application**
   ```bash
   python src/main.py
   ```

## Configuration
- All environment variables are managed in `.env` and loaded via `python-dotenv`.
- The API URL is set in `.env` as `JSONPLACEHOLDER_API_URL`.
- The CSV file path is set in `.env` as `USER_CSV_PATH` (default: `data/users.csv`).

## Output
- After running, all user records are saved to the CSV file specified by `USER_CSV_PATH`.
- The CSV contains columns for: id, name, username, email, phone, website, address, company.
- Address and company fields are serialized as JSON strings for compatibility with spreadsheet tools.

## Logging & Error Handling
- Errors and connectivity issues are logged using Python's `logging` module.
- The application will print a user-friendly message if it fails to retrieve users or save to CSV.

## Extensibility
- The codebase is modular and can be extended for additional endpoints or business logic.

## Notes
- Only GET operations are implemented as per requirements.
- No authentication is required for the JSONPlaceholder API.
