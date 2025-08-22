import pandas as pd


routine = pd.read_csv('cleanedRoutine.csv')


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
