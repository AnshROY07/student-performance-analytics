def calculate_grade(average):

    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def check_result(row):

    if row["Average"] >= 40 and row["Attendance"] >= 75:
        return "Pass"
    else:
        return "Fail"


def get_top_students(df, number=5):

    return df.sort_values(
        by="Average",
        ascending=False
    ).head(number)