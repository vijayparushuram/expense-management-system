
# Expense Management System 💰

A full-stack web application for tracking and analyzing personal expenses built with FastAPI backend and Streamlit frontend.

## 📋 Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Contributing](#contributing)

## ✨ Features

- **Add/Update Expenses**: Record daily expenses with amount, category, and notes
- **Multiple Categories**: Organize expenses into categories (Rent, Food, Shopping, Entertainment, Other)
- **Date-based Management**: View and edit expenses for specific dates
- **Analytics Dashboard**: Visualize expense breakdown by category
- **Date Range Analysis**: Analyze expenses over custom date ranges
- **Percentage Breakdown**: See spending distribution across categories
- **REST API**: Backend API for expense management operations
- **MySQL Database**: Persistent data storage

## 🛠️ Tech Stack

### Backend
- **FastAPI** (0.128.0) - Modern web framework for building APIs
- **Uvicorn** (0.40.0) - ASGI server
- **MySQL Connector** (9.5.0) - Database connectivity
- **Pydantic** (2.12.5) - Data validation

### Frontend
- **Streamlit** (1.53.1) - Interactive web application framework
- **Pandas** (2.3.3) - Data manipulation and analysis
- **Requests** (2.32.5) - HTTP library for API calls

### Testing
- **Pytest** (9.0.2) - Testing framework

## 📁 Project Structure

```
Project-expense-tracking/
│
├── Backend/
│   ├── server.py           # FastAPI application
│   ├── db_helper.py        # Database operations
│   ├── logging_setup.py    # Logging configuration
│   └── __pycache__/
│
├── Fronted/
│   ├── app.py              # Main Streamlit application
│   ├── add_update_ui.py    # Add/Update expenses interface
│   ├── analytics_ui.py     # Analytics dashboard
│   └── __pycache__/
│
├── tests/
│   ├── backend/
│   │   └── test_db_helper.py
│   ├── frontend/
│   └── conftest.py
│
├── .venv/                  # Virtual environment
├── requirements.txt        # Project dependencies
└── README.md              # Project documentation
```

## 📋 Prerequisites

- Python 3.8 or higher
- MySQL Server
- pip (Python package manager)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Project-expense-tracking
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   
   **Windows:**
   ```powershell
   .venv\Scripts\activate
   ```
   
   **macOS/Linux:**
   ```bash
   source .venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuration

### Database Setup

1. **Create MySQL Database**
   ```sql
   CREATE DATABASE expense_management;
   ```

2. **Update Database Configuration**
   
   Edit `Backend/db_helper.py` with your MySQL credentials:
   ```python
   connection = mysql.connector.connect(
       host="localhost",
       user="your_username",
       password="your_password",
       database="expense_management"
   )
   ```

3. **Create Tables**
   
   The application will automatically create necessary tables on first run, or you can run the schema manually:
   ```sql
   CREATE TABLE expenses (
       id INT AUTO_INCREMENT PRIMARY KEY,
       date DATE NOT NULL,
       amount DECIMAL(10, 2) NOT NULL,
       category VARCHAR(50) NOT NULL,
       notes TEXT,
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   ```

## 🏃 Running the Application

You need to run both backend and frontend servers simultaneously.

### Terminal 1: Start Backend API

```bash
cd Backend
uvicorn server:app --reload --port 8000
```

The API will be available at `http://localhost:8000`

### Terminal 2: Start Frontend

Open a **new terminal** and run:

```bash
cd Fronted
streamlit run app.py
```

The Streamlit app will open automatically in your browser at `http://localhost:8501`

## 📖 Usage

### Adding Expenses

1. Navigate to the **"➕ Add / Update"** tab
2. Select a date using the date picker
3. Enter up to 5 expenses with:
   - Amount
   - Category (Rent, Food, Shopping, Entertainment, Other)
   - Optional notes
4. Click **"Save Expenses"** to store the data

### Viewing Analytics

1. Navigate to the **"📊 Analytics"** tab
2. Select a date range (Start Date and End Date)
3. Click **"Get Analytics"** to view:
   - Bar chart showing expense breakdown by category
   - Detailed table with totals and percentages

## 🔌 API Endpoints

### Base URL: `http://localhost:8000`

#### Get Expenses for a Date
```http
GET /expenses/{date}
```
- **Parameters**: `date` (YYYY-MM-DD format)
- **Response**: List of expenses for the specified date

#### Add/Update Expenses
```http
POST /expenses/{date}
```
- **Parameters**: `date` (YYYY-MM-DD format)
- **Body**: JSON array of expense objects
  ```json
  [
    {
      "amount": 50.00,
      "category": "Food",
      "notes": "Grocery shopping"
    }
  ]
  ```

#### Get Analytics
```http
POST /analytics/
```
- **Body**: JSON object with date range
  ```json
  {
    "start_date": "2024-08-01",
    "end_date": "2024-08-31"
  }
  ```
- **Response**: Category-wise breakdown with totals and percentages

## 🧪 Testing

Run the test suite:

```bash
pytest tests/
```

Run specific test file:

```bash
pytest tests/backend/test_db_helper.py
```

Run with coverage:

```bash
pytest --cov=Backend tests/
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Development Notes

- The backend uses logging configured in `logging_setup.py` - check `server.log` for debugging
- Frontend components are modular - `add_update_ui.py` and `analytics_ui.py` can be modified independently
- Database helper functions are centralized in `db_helper.py`
- The application uses date-based expense tracking (expenses grouped by date)

## 🐛 Troubleshooting

### Common Issues

**Backend won't start:**
- Check if MySQL server is running
- Verify database credentials in `db_helper.py`
- Ensure port 8000 is not already in use

**Frontend can't connect to API:**
- Verify backend is running on `http://localhost:8000`
- Check API_URL in `add_update_ui.py` and `analytics_ui.py`

**Database connection errors:**
- Confirm MySQL service is active
- Check database name and user permissions
- Verify network/firewall settings

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👥 Authors

- Your Name - Initial work

## 🙏 Acknowledgments

- FastAPI documentation
- Streamlit community
- MySQL documentation
