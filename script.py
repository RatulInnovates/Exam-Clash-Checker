import pandas as pd
from functools import cmp_to_key
import streamlit as st


routine = pd.read_csv('cleanedRoutine.csv')


def showDetails(course):
    time = {
        'T1': '9:00 AM - 11:00 AM',
        'T2': '11:30 AM - 1:30 PM',
        'T3': '2:00 PM - 4:00 PM'
    }
    dict = {course: [routine[course].iloc[0], time[routine[course].iloc[1]]]}
    st.write(pd.DataFrame(dict, index=["Day", "Time"]))


def comparator(course1, course2):
    return routine[course1].iloc[0] > routine[course2].iloc[0]


def showRoutine(*courses):
    """
    Show routine of selected courses.
    Sorted by date 
    *When no clash exists*

    """

    st.badge("Routine:", color="green")
    srted = sorted(courses, key=cmp_to_key(comparator))
    for c in srted:
        showDetails(c)


def checkClashByDay(*courses):
    """
    Checks for time clashes on the same day among given courses.
    Returns a dictionary: {course_code: (day, time)} for all clashes.

    Parameters:
        courses (list): List of course codes to check.
        routine (DataFrame): DataFrame with days as index and course codes as columns.
                             Each cell contains the time slot of the course.

    Returns:
        dict: {course_code: (day, time)} for all clashes.
    """
    days = []
    day_map = {}
    clashes = {}
    for course in courses:
        day = routine[course].iloc[0]
        if day in days:
            clashes[course] = day
            clashes[day_map[day]] = day
        else:
            days.append(day)
            day_map[day] = course
    return clashes


def clashByTime(*courses):
    """
    Checks for time clashes on the same day among given courses.
    Returns a dictionary: {course_code: (day, time)} for all clashes.
    """
    # maps day -> {time -> course}
    time_map = {}
    clashes = {}

    for course in courses:
        # Assuming routine[course] is a Series with 'Day' and 'Time'
        day = routine[course].iloc[0]
        time = routine[course].iloc[1]

        if day not in time_map:
            time_map[day] = {}

        if time in time_map[day]:
            # Clash found
            other_course = time_map[day][time]
            clashes[course] = (day, time)
            clashes[other_course] = (day, time)
        else:
            # No clash, store this course
            time_map[day][time] = course

    return clashes


if __name__ == "__main__":
    checkClashByDay("ENG 1013", "ENG 1011")
