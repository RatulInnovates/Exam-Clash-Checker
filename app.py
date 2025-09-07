import streamlit as st
import pandas as pd
from script import checkClashByDay, clashByTime, routine, showRoutine
import logging
logging.basicConfig(
    filename="app.log",
    filemode="w",
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    force=True
)

# Load courses
uiu_courses = pd.read_csv('uiu_courses.csv')

# Keep only rows where 'course code' exists in routine.columns
uiu_courses = uiu_courses[uiu_courses['course code'].isin(routine.columns)]

# Fix typo in course code
uiu_courses['course code'] = uiu_courses['course code'].replace(
    'SOC 4101', 'SOC 2101')

# Create mapping: code -> title
code_to_title = pd.Series(uiu_courses.title.values,
                          index=uiu_courses['course code']).to_dict()

# Create display options as "code - title" for search/autocomplete
display_options = [f"{code} - {title}" for code,
                   title in code_to_title.items()]


def showDetails(course):
    time = {
        'T1': '9:00 AM - 11:00 AM',
        'T2': '11:30 AM - 1:30 PM',
        'T3': '2:00 PM - 4:00 PM'
    }
    dict = {course: [routine[course].iloc[0], time[routine[course].iloc[1]]]}
    st.write(pd.DataFrame(dict, index=["Day", "Time"]))


st.title("UIU Exam Time Clash Checker")

# Mode selection
modes = ["", "Check Clash By Day", "Check Clash By Time"]
mode = st.selectbox("Select Mode", modes)

if mode:
    # Multiselect with autocomplete
    selected_display = st.multiselect(
        "Select Courses",
        options=display_options,
        max_selections=15
    )

    # Extract course codes from selections
    chosen_courses = [s.split(" - ")[0].strip() for s in selected_display]
    logging.debug(chosen_courses)

    if chosen_courses:
        if mode == "Check Clash By Day":
            clash = checkClashByDay(*chosen_courses)
            if clash:
                st.warning("Day Clash Found!!!")
                for course, day in clash.items():
                    # st.write(f"{course} clashes on day {day}")
                    # st.write(routine[str(course)])
                    showDetails(course)
            else:
                st.success("No Day Clash!")
                showRoutine(*chosen_courses)
        elif mode == "Check Clash By Time":
            clash = clashByTime(*chosen_courses)
            if clash:
                st.warning("Time Clash Found!!!")
                for course, day in clash.items():
                    # st.write(f"{course} clashes on day {day}")
                    # st.write(routine[str(course)])
                    showDetails(course)
            else:
                st.success("No Time Clash!")
                showRoutine(*chosen_courses)
