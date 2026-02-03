from fastapi import FastAPI, HTTPException
from datetime import date
from typing import List, Dict
from pydantic import BaseModel
import db_helper

app = FastAPI(title="Expense Tracking API")

# =========================
# MODELS
# =========================

class Expense(BaseModel):
    amount: float
    category: str
    notes: str


class DateRange(BaseModel):
    start_date: date
    end_date: date


class AnalyticsItem(BaseModel):
    total: float
    percentage: float


# =========================
# EXPENSE APIs
# =========================

@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date: date):
    """
    Get all expenses for a given date
    """
    try:
        return db_helper.fetch_expenses_for_date(expense_date)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/expenses/{expense_date}")
def add_or_update_expenses(expense_date: date, expenses: List[Expense]):
    """
    Add or update expenses for a given date
    """
    try:
        # Remove old expenses for that date
        db_helper.delete_expenses_for_date(expense_date)

        # Insert new expenses
        for exp in expenses:
            db_helper.insert_expense(
                expense_date,
                exp.amount,
                exp.category,
                exp.notes
            )

        return {"message": "Expenses updated successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# =========================
# ANALYTICS API
# =========================

@app.post("/analytics/", response_model=Dict[str, AnalyticsItem])
def get_analytics(date_range: DateRange):
    """
    Get expense summary between two dates
    """
    data = db_helper.fetch_expense_summary(
        date_range.start_date,
        date_range.end_date
    )

    if not data:
        return {}

    total_amount = sum(row["total"] for row in data)

    breakdown: Dict[str, AnalyticsItem] = {}

    for row in data:
        percentage = (
            (row["total"] / total_amount) * 100
            if total_amount != 0
            else 0
        )

        breakdown[row["category"]] = {
            "total": row["total"],
            "percentage": percentage
        }

    return breakdown
