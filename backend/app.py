import hmac
import os
import sqlite3
from datetime import datetime
from functools import wraps
from pathlib import Path

from flask import (
    Flask, flash, g, redirect, render_template, request, session, url_for,
)

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-change-me")
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"

COMPANY = "Rihla"
DB_PATH = Path(__file__).parent / "rihla.db"

# Dummy admin login, change before going online
ADMIN_EMAIL = os.environ.get("ADMIN_EMAIL", "admin@hotmail.com")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "admin1234")

# Dummy data, replace later. "capacity" = max guests in total.
EXPERIENCES = [
    {"name": "Desert Sunset Safari", "description": "Dune driving, camel rides and a sunset dinner.", "price": "$120", "capacity": 20},
    {"name": "Old Town Walking Tour", "description": "Discover local history, markets and hidden cafes.", "price": "$45", "capacity": 15},
    {"name": "Coastal Boat Trip", "description": "Half day on the water with snorkelling and lunch.", "price": "$85", "capacity": 12},
]


# ---------- Database ----------

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(error):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    db = sqlite3.connect(DB_PATH)
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            experience TEXT NOT NULL,
            date TEXT NOT NULL,
            guests INTEGER NOT NULL,
            created_at TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'confirmed'
        )
        """
    )
    # Upgrade an older database that has no "status" column yet
    columns = [row[1] for row in db.execute("PRAGMA table_info(bookings)")]
    if "status" not in columns:
        db.execute("ALTER TABLE bookings ADD COLUMN status TEXT NOT NULL DEFAULT 'confirmed'")
    db.commit()
    db.close()


def get_experiences():
    """Experiences with live capacity. Only confirmed bookings use spots."""
    rows = get_db().execute(
        "SELECT experience, COALESCE(SUM(guests), 0) AS booked "
        "FROM bookings WHERE status = 'confirmed' GROUP BY experience"
    ).fetchall()
    booked_by_name = {r["experience"]: r["booked"] for r in rows}

    result = []
    for e in EXPERIENCES:
        booked = booked_by_name.get(e["name"], 0)
        result.append({**e, "booked": booked, "remaining": max(e["capacity"] - booked, 0)})
    return result


# ---------- Admin login ----------

def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not session.get("admin"):
            return redirect(url_for("admin_login"))
        return view(*args, **kwargs)
    return wrapped


@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if session.get("admin"):
        return redirect(url_for("admin_bookings"))

    error = None
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        email_ok = hmac.compare_digest(email.encode(), ADMIN_EMAIL.lower().encode())
        pass_ok = hmac.compare_digest(password.encode(), ADMIN_PASSWORD.encode())

        if email_ok and pass_ok:
            session.clear()
            session["admin"] = True
            return redirect(url_for("admin_bookings"))
        error = "Wrong email or password."

    return render_template("admin_login.html", active="", error=error)


@app.route("/admin/logout", methods=["POST"])
def admin_logout():
    session.clear()
    return redirect(url_for("home"))


# ---------- Public pages ----------

@app.context_processor
def inject_globals():
    return {"company": COMPANY}


@app.route("/")
def home():
    return render_template("home.html", active="home")


@app.route("/experiences")
def experiences():
    return render_template("experiences.html", active="experiences", experiences=get_experiences())


@app.route("/book", methods=["GET", "POST"])
def book():
    error = None

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        experience = request.form.get("experience", "").strip()
        date = request.form.get("date", "").strip()
        try:
            guests = int(request.form.get("guests", "1"))
        except ValueError:
            guests = 0

        valid_names = [e["name"] for e in EXPERIENCES]

        if not name or not email or not date or guests < 1 or experience not in valid_names:
            error = "Please fill in all fields correctly."
        else:
            db = get_db()
            # Lock the database so two people cannot take the last spots at the same time
            db.execute("BEGIN IMMEDIATE")
            chosen = next(e for e in get_experiences() if e["name"] == experience)

            if guests > chosen["remaining"]:
                db.rollback()
                error = f"Sorry, only {chosen['remaining']} spots are left for {experience}."
            else:
                db.execute(
                    "INSERT INTO bookings (name, email, experience, date, guests, created_at, status) "
                    "VALUES (?, ?, ?, ?, ?, ?, 'confirmed')",
                    (name, email, experience, date, guests, datetime.now().isoformat(timespec="seconds")),
                )
                db.commit()
                # Redirect so a page refresh does not send the form twice
                return redirect(url_for("book", sent=1))

    message = None
    if request.args.get("sent"):
        message = "Thank you! Your booking request was saved. We will contact you soon."

    return render_template("book.html", active="book", experiences=get_experiences(), message=message, error=error)


@app.route("/contact")
def contact():
    return render_template("contact.html", active="contact")


# ---------- Admin pages ----------

@app.route("/admin/bookings")
@login_required
def admin_bookings():
    rows = get_db().execute("SELECT * FROM bookings ORDER BY id DESC").fetchall()
    return render_template("admin_bookings.html", active="", bookings=rows, experiences=get_experiences())


@app.route("/admin/bookings/<int:booking_id>/refund", methods=["POST"])
@login_required
def refund_booking(booking_id):
    db = get_db()
    cur = db.execute(
        "UPDATE bookings SET status = 'refunded' WHERE id = ? AND status = 'confirmed'",
        (booking_id,),
    )
    db.commit()
    if cur.rowcount:
        flash(f"Booking {booking_id} was refunded. Its spots are free again.")
    else:
        flash(f"Booking {booking_id} could not be refunded (not found or already refunded).")
    return redirect(url_for("admin_bookings"))


@app.route("/admin/bookings/<int:booking_id>/delete", methods=["POST"])
@login_required
def delete_booking(booking_id):
    db = get_db()
    cur = db.execute("DELETE FROM bookings WHERE id = ?", (booking_id,))
    db.commit()
    if cur.rowcount:
        flash(f"Booking {booking_id} was deleted.")
    else:
        flash(f"Booking {booking_id} was not found.")
    return redirect(url_for("admin_bookings"))


if __name__ == "__main__":
    init_db()
    app.run(host="127.0.0.1", port=5000)