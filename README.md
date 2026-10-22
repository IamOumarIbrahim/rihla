# Rihla

A simple desktop app for a travel company. The frontend is an Electron window. The backend is a Python (Flask) server with a SQLite database.

## Features

- Pages: Home, Experiences, Book now, Contact us
- Bookings are saved in a SQLite database
- Capacity limit for each experience
- Admin login with Refund and Delete buttons for bookings

## Tech stack

- Electron
- Node.js and npm
- Python 3 and Flask
- SQLite

## Requirements

- Node.js (nodejs.org)
- Python 3 (python.org). Tick "Add python.exe to PATH" during setup.

## Setup

    npm install
    pip install -r backend/requirements.txt

## Run

    npm start

Electron starts the Flask server in the background and opens the app window. When you close the window, the server stops.

## Admin login (dummy values)

- Email: admin@hotmail.com
- Password: admin1234

Change these before you put the app online. You can set the environment variables ADMIN_EMAIL, ADMIN_PASSWORD and SECRET_KEY.

## Project structure

    my-electron-app/
    ├── backend/
    │   ├── app.py
    │   ├── requirements.txt
    │   ├── static/
    │   └── templates/
    ├── index.html
    ├── main.js
    ├── package.json
    └── preload.js

## Notes

- The database file backend/rihla.db is created automatically and is not stored in Git.
- Refund only changes the booking status. No real payment is sent back.
- All text, prices and contact details are dummy data.