# Exam Time Clash Checker

A Streamlit web app to check for exam schedule clashes by day and time for UIU courses.
  🚀 **[Live Demo](https://uiu-exam-clash-checker.streamlit.app/)**

## Features

- **Check Clash By Day:** Detects if selected courses have exams scheduled on the same day.
- **Check Clash By Time:** Detects if selected courses have exams scheduled at the same time slot on the same day.
- **Autocomplete Course Selection:** Easily search and select courses by code and title.

## How It Works

- The app loads course codes, exam days, and time slots from `cleanedRoutine.csv`.
- Users select courses from a searchable list.
- The app checks for scheduling conflicts and displays results.

## File Structure

- `app.py` — Streamlit app UI and logic.
- `script.py` — Clash detection functions.
- `cleanedRoutine.csv` — Exam schedule data (course codes, days, times).
- `uiu_courses.csv` — Course code and title mapping.

## Setup

1. **Install dependencies:**

   ```
   pip install streamlit pandas
   ```

2. **Run the app:**

   ```
   streamlit run app.py
   ```

3. **Select courses and check for clashes.**

## Data Format

- `cleanedRoutine.csv`:

  - Row 1: Course codes
  - Row 2: Exam days (e.g., 1, 2, ...)
  - Row 3: Time slots (e.g., T1, T2, ...)

- `uiu_courses.csv`:
  - Columns: `course code`, `title`

## Logging

- App logs are saved to `app.log` for debugging.

## License

MIT License
