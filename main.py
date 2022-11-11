from tkinter import *
from PIL import Image, ImageTk
import json
from tkinter import messagebox
import math
# Done by Engr_max
# WARNING: PLEASE HANDLE WITH CARE
# ------------------------------------------ FUOYE CGPA CALCULATOR ---------------------------------------------------

# ---------------------------------------------------SEARCH------------------------------------------------------------

# def search():
#     name_input = name_entry.get()
#     with open("data.json", "r"):



# ------------------------------------------ SAVE RESULT -------------------------------------------------------------


def save():
    """This save the details for the individual"""
    gpa_1 = gpa_value_label.cget("text")
    print(gpa_1)
    gpa_2 = gpa_2_value_label.cget("text")
    name = name_entry.get()
    level = level_entry.get()
    dept = dept_entry.get()

    # first_semester_course_code
    first_semester_course_1 = course_1_entry.get()
    first_semester_course_2 = course_2_entry.get()
    first_semester_course_3 = course_3_entry.get()
    first_semester_course_4 = course_4_entry.get()
    first_semester_course_5 = course_5_entry.get()
    first_semester_course_6 = course_6_entry.get()
    first_semester_course_7 = course_7_entry.get()
    first_semester_course_8 = course_8_entry.get()
    first_semester_course_9 = course_9_entry.get()
    first_semester_course_10 = course_10_entry.get()
    first_semester_course_11 = course_11_entry.get()

    # grade
    first_semester_grade_1 = grade_1.get()
    first_semester_grade_2 = grade_2.get()
    first_semester_grade_3 = grade_3.get()
    first_semester_grade_4 = grade_4.get()
    first_semester_grade_5 = grade_5.get()
    first_semester_grade_6 = grade_6.get()
    first_semester_grade_7 = grade_7.get()
    first_semester_grade_8 = grade_8.get()
    first_semester_grade_9 = grade_9.get()
    first_semester_grade_10 = grade_10.get()
    first_semester_grade_11 = grade_11.get()

    # second_semester_course_code
    second_semester_course_1 = second_semester_course_1_entry.get()
    second_semester_course_2 = second_semester_course_2_entry.get()
    second_semester_course_3 = second_semester_course_3_entry.get()
    second_semester_course_4 = second_semester_course_4_entry.get()
    second_semester_course_5 = second_semester_course_5_entry.get()
    second_semester_course_6 = second_semester_course_6_entry.get()
    second_semester_course_7 = second_semester_course_7_entry.get()
    second_semester_course_8 = second_semester_course_8_entry.get()
    second_semester_course_9 = second_semester_course_9_entry.get()
    second_semester_course_10 = second_semester_course_10_entry.get()

    # grade
    second_semester_grade_1_ = second_semester_grade_1.get()
    second_semester_grade_2_ = second_semester_grade_2.get()
    second_semester_grade_3_ = second_semester_grade_3.get()
    second_semester_grade_4_ = second_semester_grade_4.get()
    second_semester_grade_5_ = second_semester_grade_5.get()
    second_semester_grade_6_ = second_semester_grade_6.get()
    second_semester_grade_7_ = second_semester_grade_7.get()
    second_semester_grade_8_ = second_semester_grade_8.get()
    second_semester_grade_9_ = second_semester_grade_9.get()
    second_semester_grade_10_ = second_semester_grade_10.get()

    new_data = {
        name:
            {"Semester": "First_Semester",
             "LEVEL": level,
             "DEPT": dept,
             first_semester_course_1: first_semester_grade_1,
             first_semester_course_2: first_semester_grade_2,
             first_semester_course_3: first_semester_grade_3,
             first_semester_course_4: first_semester_grade_4,
             first_semester_course_5: first_semester_grade_5,
             first_semester_course_6: first_semester_grade_6,
             first_semester_course_7: first_semester_grade_7,
             first_semester_course_8: first_semester_grade_8,
             first_semester_course_9: first_semester_grade_9,
             first_semester_course_10: first_semester_grade_10,
             first_semester_course_11: first_semester_grade_11,
             "First_semester_GPA": gpa_1
             },

        #   second_semester
        "name":
            {"Semester": "Second_Semester",
             "LEVEL": level,
             "DEPT": dept,
             second_semester_course_1: second_semester_grade_1_,
             second_semester_course_2: second_semester_grade_2_,
             second_semester_course_3: second_semester_grade_3_,
             second_semester_course_4: second_semester_grade_4_,
             second_semester_course_5: second_semester_grade_5_,
             second_semester_course_6: second_semester_grade_6_,
             second_semester_course_7: second_semester_grade_7_,
             second_semester_course_8: second_semester_grade_8_,
             second_semester_course_9: second_semester_grade_9_,
             second_semester_course_10: second_semester_grade_10_,
             "Second_semester_GPA": gpa_2
             },

    }

    try:
        with open("result_data.json", "r") as result_file:
            data = json.load(result_file)
            data.update(new_data)
    except FileNotFoundError:
        with open("result_data.json", "w") as result_file:
            json.dump(new_data, result_file, indent=4)

    else:
        data.update(new_data)
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
    finally:
        messagebox.showinfo(title="Message", message="Are you sure, you want to save this?, if 'yes' click "
                                                     "on 'ok' to save,if 'no' click cancel")
        name_entry.delete(0, END)
        dept_entry.delete(0, END)
        level_entry.delete(0, END)
        matric_num_entry.delete(0, END)

        course_1_entry.delete(0, END)
        course_2_entry.delete(0, END)
        course_3_entry.delete(0, END)
        course_4_entry.delete(0, END)
        course_5_entry.delete(0, END)
        course_6_entry.delete(0, END)
        course_7_entry.delete(0, END)
        course_8_entry.delete(0, END)
        course_9_entry.delete(0, END)
        course_10_entry.delete(0, END)
        course_11_entry.delete(0, END)
        grade_1.delete(0, END)
        grade_2.delete(0, END)
        grade_3.delete(0, END)
        grade_4.delete(0, END)
        grade_5.delete(0, END)
        grade_6.delete(0, END)
        grade_7.delete(0, END)
        grade_8.delete(0, END)
        grade_9.delete(0, END)
        grade_10.delete(0, END)
        grade_11.delete(0, END)

        unit_1.delete(0, END)
        unit_2.delete(0, END)
        unit_3.delete(0, END)
        unit_4.delete(0, END)
        unit_5.delete(0, END)
        unit_6.delete(0, END)
        unit_7.delete(0, END)
        unit_8.delete(0, END)
        unit_9.delete(0, END)
        unit_10.delete(0, END)
        unit_11.delete(0, END)

        second_semester_grade_1.delete(0, END)
        second_semester_grade_2.delete(0, END)
        second_semester_grade_3.delete(0, END)
        second_semester_grade_4.delete(0, END)
        second_semester_grade_5.delete(0, END)
        second_semester_grade_6.delete(0, END)
        second_semester_grade_7.delete(0, END)
        second_semester_grade_8.delete(0, END)
        second_semester_grade_9.delete(0, END)
        second_semester_grade_10.delete(0, END)
        second_semester_course_1_entry.delete(0, END)
        second_semester_course_2_entry.delete(0, END)
        second_semester_course_3_entry.delete(0, END)
        second_semester_course_4_entry.delete(0, END)
        second_semester_course_5_entry.delete(0, END)
        second_semester_course_6_entry.delete(0, END)
        second_semester_course_7_entry.delete(0, END)
        second_semester_course_8_entry.delete(0, END)
        second_semester_course_9_entry.delete(0, END)
        second_semester_course_10_entry.delete(0, END)

        second_semester_unit_1_entry.delete(0,END)
        second_semester_unit_2_entry.delete(0, END)
        second_semester_unit_3_entry.delete(0, END)
        second_semester_unit_4_entry.delete(0, END)
        second_semester_unit_5_entry.delete(0, END)
        second_semester_unit_6_entry.delete(0, END)
        second_semester_unit_7_entry.delete(0, END)
        second_semester_unit_8_entry.delete(0, END)
        second_semester_unit_9_entry.delete(0, END)
        second_semester_unit_10_entry.delete(0, END)
        name_entry.focus()


# ------------------------------------------ CALCULATOR --------------------------------------------------------------
#     Grading_system_1: 70-100 = A Grading_system_2: A=5 points
#                       60-69 = B                    B=4 points
#                       50-59 = C                    C=3 points
#                       45-49 = D                    D=2 points
#                       40-44 = E                    E=1 point
#                       0-39  = F                    F=0 point


def calculator_1():
    """This calculates the gpa for the current session_2"""
    Grade_1 = grade_1.get()
    Grade_2 = grade_2.get()
    Grade_3 = grade_3.get()
    Grade_4 = grade_4.get()
    Grade_5 = grade_5.get()
    Grade_6 = grade_6.get()
    Grade_7 = grade_7.get()
    Grade_8 = grade_8.get()
    Grade_9 = grade_9.get()
    Grade_10 = grade_10.get()
    Grade_11 = grade_11.get()

    Unit_1 = unit_1.get()
    Unit_2 = unit_2.get()
    Unit_3 = unit_3.get()
    Unit_4 = unit_4.get()
    Unit_5 = unit_5.get()
    Unit_6 = unit_6.get()
    Unit_7 = unit_7.get()
    Unit_8 = unit_8.get()
    Unit_9 = unit_9.get()
    Unit_10 = unit_10.get()
    Unit_11 = unit_11.get()

    Total_grade_point_value = total_credit_point_value_label
    TLU = total_load_unit_value_label
    GPA = gpa_value_label

    if Grade_1 == "A":
        grade_1_point = 5
    elif Grade_1 == "B":
        grade_1_point = 4
    elif Grade_1 == "C":
        grade_1_point = 3
    elif Grade_1 == "D":
        grade_1_point = 2
    elif Grade_1 == "E":
        grade_1_point = 1
    else:
        grade_1_point = 0

    if Grade_2 == "A":
        grade_2_point = 5
    elif Grade_2 == "B":
        grade_2_point = 4
    elif Grade_2 == "C":
        grade_2_point = 3
    elif Grade_2 == "D":
        grade_2_point = 2
    elif Grade_2 == "E":
        grade_2_point = 1
    else:
        grade_2_point = 0

    if Grade_3 == "A":
        grade_3_point = 5
    elif Grade_3 == "B":
        grade_3_point = 4
    elif Grade_3 == "C":
        grade_3_point = 3
    elif Grade_3 == "D":
        grade_3_point = 2
    elif Grade_3 == "E":
        grade_3_point = 1
    else:
        grade_3_point = 0

    if Grade_4 == "A":
        grade_4_point = 5
    elif Grade_4 == "B":
        grade_4_point = 4
    elif Grade_4 == "C":
        grade_4_point = 3
    elif Grade_4 == "D":
        grade_4_point = 2
    elif Grade_4 == "E":
        grade_4_point = 1
    else:
        grade_4_point = 0

    if Grade_5 == "A":
        grade_5_point = 5
    elif Grade_5 == "B":
        grade_5_point = 4
    elif Grade_5 == "C":
        grade_5_point = 3
    elif Grade_5 == "D":
        grade_5_point = 2
    elif Grade_5 == "E":
        grade_5_point = 1
    else:
        grade_5_point = 0

    if Grade_6 == "A":
        grade_6_point = 5
    elif Grade_6 == "B":
        grade_6_point = 4
    elif Grade_6 == "C":
        grade_6_point = 3
    elif Grade_6 == "D":
        grade_6_point = 2
    elif Grade_6 == "E":
        grade_6_point = 1
    else:
        grade_6_point = 0

    if Grade_7 == "A":
        grade_7_point = 5
    elif Grade_7 == "B":
        grade_7_point = 4
    elif Grade_7 == "C":
        grade_7_point = 3
    elif Grade_7 == "D":
        grade_7_point = 2
    elif Grade_7 == "E":
        grade_7_point = 1
    else:
        grade_7_point = 0

    if Grade_8 == "A":
        grade_8_point = 5
    elif Grade_8 == "B":
        grade_8_point = 4
    elif Grade_8 == "C":
        grade_8_point = 3
    elif Grade_8 == "D":
        grade_8_point = 2
    elif Grade_8 == "E":
        grade_8_point = 1
    else:
        grade_8_point = 0

    if Grade_9 == "A":
        grade_9_point = 5
    elif Grade_9 == "B":
        grade_9_point = 4
    elif Grade_9 == "C":
        grade_9_point = 3
    elif Grade_9 == "D":
        grade_9_point = 2
    elif Grade_9 == "E":
        grade_9_point = 1
    else:
        grade_9_point = 0

    if Grade_10 == "A":
        grade_10_point = 5
    elif Grade_10 == "B":
        grade_10_point = 4
    elif Grade_10 == "C":
        grade_10_point = 3
    elif Grade_10 == "D":
        grade_10_point = 2
    elif Grade_10 == "E":
        grade_10_point = 1
    else:
        grade_10_point = 0

    if Grade_11 == "A":
        grade_11_point = 5
    elif Grade_11 == "B":
        grade_11_point = 4
    elif Grade_11 == "C":
        grade_11_point = 3
    elif Grade_11 == "D":
        grade_11_point = 2
    elif Grade_11 == "E":
        grade_11_point = 1
    else:
        grade_11_point = 0

    first_cp_1 = grade_1_point * (int(Unit_1))
    first_cp_2 = grade_2_point * (int(Unit_2))
    first_cp_3 = grade_3_point * (int(Unit_3))
    first_cp_4 = grade_4_point * (int(Unit_4))
    first_cp_5 = grade_5_point * (int(Unit_5))
    first_cp_6 = grade_6_point * (int(Unit_6))
    first_cp_7 = grade_7_point * (int(Unit_7))
    first_cp_8 = grade_8_point * (int(Unit_8))
    first_cp_9 = grade_9_point * (int(Unit_9))
    first_cp_10 = grade_10_point * (int(Unit_10))
    first_cp_11 = grade_11_point * (int(Unit_11))

    total_grade_point = (
            grade_1_point * (int(Unit_1)) + grade_2_point * (int(Unit_2)) + grade_3_point * (int(Unit_3)) +
            grade_4_point * (int(Unit_4))
            + grade_5_point * (int(Unit_5)) + grade_6_point * (int(Unit_6)) +
            grade_7_point * (int(Unit_7)) + grade_8_point * (int(Unit_8)) + grade_9_point * (int(Unit_9))
            + grade_10_point * (int(Unit_10))
            + grade_11_point * (int(Unit_11)))

    total_load_unit = int(Unit_1) + int(Unit_2) + int(Unit_3) + int(Unit_4) + int(Unit_5) + int(Unit_6) + int(Unit_7) \
                      + int(Unit_8) + int(Unit_9) + int(Unit_10) + int(Unit_11)
    gpa = float(total_grade_point/total_load_unit)
    approximated_gpa_1 = round(gpa,2)
    Total_grade_point_value.config(text=total_grade_point)
    TLU.config(text=total_load_unit)
    GPA.config(text=approximated_gpa_1)
    credit_point_1_label.config(text=first_cp_1)
    credit_point_2_label.config(text=first_cp_2)
    credit_point_3_label.config(text=first_cp_3)
    credit_point_4_label.config(text=first_cp_4)
    credit_point_5_label.config(text=first_cp_5)
    credit_point_6_label.config(text=first_cp_6)
    credit_point_7_label.config(text=first_cp_7)
    credit_point_8_label.config(text=first_cp_8)
    credit_point_9_label.config(text=first_cp_9)
    credit_point_10_label.config(text=first_cp_10)
    credit_point_11_label.config(text=first_cp_11)


def calculator_2():
    """This calculates the gpa for the current session_2"""
    Total_grade_point_value_2 = total_credit_point_value_2_label
    TLU_2 = total_load_unit_value_2_label
    GPA_2 = gpa_2_value_label
    second_semester_Grade_1 = second_semester_grade_1.get()
    second_semester_Grade_2 = second_semester_grade_2.get()
    second_semester_Grade_3 = second_semester_grade_3.get()
    second_semester_Grade_4 = second_semester_grade_4.get()
    second_semester_Grade_5 = second_semester_grade_5.get()
    second_semester_Grade_6 = second_semester_grade_6.get()
    second_semester_Grade_7 = second_semester_grade_7.get()
    second_semester_Grade_8 = second_semester_grade_8.get()
    second_semester_Grade_9 = second_semester_grade_9.get()
    second_semester_Grade_10 = second_semester_grade_10.get()

    second_Unit_1 = second_semester_unit_1_entry.get()
    second_Unit_2 = second_semester_unit_2_entry.get()
    second_Unit_3 = second_semester_unit_3_entry.get()
    second_Unit_4 = second_semester_unit_4_entry.get()
    second_Unit_5 = second_semester_unit_5_entry.get()
    second_Unit_6 = second_semester_unit_6_entry.get()
    second_Unit_7 = second_semester_unit_7_entry.get()
    second_Unit_8 = second_semester_unit_8_entry.get()
    second_Unit_9 = second_semester_unit_9_entry.get()
    second_Unit_10 = second_semester_unit_10_entry.get()

    if second_semester_Grade_1 == "A":
        second_semester_grade_1_point = 5
    elif second_semester_Grade_1 == "B":
        second_semester_grade_1_point = 4
    elif second_semester_Grade_1 == "C":
        second_semester_grade_1_point = 3
    elif second_semester_Grade_1 == "D":
        second_semester_grade_1_point = 2
    elif second_semester_Grade_1 == "E":
        second_semester_grade_1_point = 1
    else:
        second_semester_grade_1_point = 0

    if second_semester_Grade_2 == "A":
        second_semester_grade_2_point = 5
    elif second_semester_Grade_2 == "B":
        second_semester_grade_2_point = 4
    elif second_semester_Grade_2 == "C":
        second_semester_grade_2_point = 3
    elif second_semester_Grade_2 == "D":
        second_semester_grade_2_point = 2
    elif second_semester_Grade_2 == "E":
        second_semester_grade_2_point = 1
    else:
        second_semester_grade_2_point = 0

    if second_semester_Grade_3 == "A":
        second_semester_grade_3_point = 5
    elif second_semester_Grade_3 == "B":
        second_semester_grade_3_point = 4
    elif second_semester_Grade_3 == "C":
        second_semester_grade_3_point = 3
    elif second_semester_Grade_3 == "D":
        second_semester_grade_3_point = 2
    elif second_semester_Grade_3 == "E":
        second_semester_grade_3_point = 1
    else:
        second_semester_grade_3_point = 0

    if second_semester_Grade_4 == "A":
        second_semester_grade_4_point = 5
    elif second_semester_Grade_4 == "B":
        second_semester_grade_4_point = 4
    elif second_semester_Grade_4 == "C":
        second_semester_grade_4_point = 3
    elif second_semester_Grade_4 == "D":
        second_semester_grade_4_point = 2
    elif second_semester_Grade_4 == "E":
        second_semester_grade_4_point = 1
    else:
        second_semester_grade_4_point = 0

    if second_semester_Grade_5 == "A":
        second_semester_grade_5_point = 5
    elif second_semester_Grade_5 == "B":
        second_semester_grade_5_point = 4
    elif second_semester_Grade_5 == "C":
        second_semester_grade_5_point = 3
    elif second_semester_Grade_5 == "D":
        second_semester_grade_5_point = 2
    elif second_semester_Grade_5 == "E":
        second_semester_grade_5_point = 1
    else:
        second_semester_grade_5_point = 0

    if second_semester_Grade_6 == "A":
        second_semester_grade_6_point = 5
    elif second_semester_Grade_6 == "B":
        second_semester_grade_6_point = 4
    elif second_semester_Grade_6 == "C":
        second_semester_grade_6_point = 3
    elif second_semester_Grade_6 == "D":
        second_semester_grade_6_point = 2
    elif second_semester_Grade_6 == "E":
        second_semester_grade_6_point = 1
    else:
        second_semester_grade_6_point = 0

    if second_semester_Grade_7 == "A":
        second_semester_grade_7_point = 5
    elif second_semester_Grade_7 == "B":
        second_semester_grade_7_point = 4
    elif second_semester_Grade_7 == "C":
        second_semester_grade_7_point = 3
    elif second_semester_Grade_7 == "D":
        second_semester_grade_7_point = 2
    elif second_semester_Grade_7 == "E":
        second_semester_grade_7_point = 1
    else:
        second_semester_grade_7_point = 0

    if second_semester_Grade_8 == "A":
        second_semester_grade_8_point = 5
    elif second_semester_Grade_8 == "B":
        second_semester_grade_8_point = 4
    elif second_semester_Grade_8 == "C":
        second_semester_grade_8_point = 3
    elif second_semester_Grade_8 == "D":
        second_semester_grade_8_point = 2
    elif second_semester_Grade_8 == "E":
        second_semester_grade_8_point = 1
    else:
        second_semester_grade_8_point = 0

    if second_semester_Grade_9 == "A":
        second_semester_grade_9_point = 5
    elif second_semester_Grade_9 == "B":
        second_semester_grade_9_point = 4
    elif second_semester_Grade_9 == "C":
        second_semester_grade_9_point = 3
    elif second_semester_Grade_9 == "D":
        second_semester_grade_9_point = 2
    elif second_semester_Grade_9 == "E":
        second_semester_grade_9_point = 1
    else:
        second_semester_grade_9_point = 0

    if second_semester_Grade_10 == "A":
        second_semester_grade_10_point = 5
    elif second_semester_Grade_10 == "B":
        second_semester_grade_10_point = 4
    elif second_semester_Grade_10 == "C":
        second_semester_grade_10_point = 3
    elif second_semester_Grade_10 == "D":
        second_semester_grade_10_point = 2
    elif second_semester_Grade_10 == "E":
        second_semester_grade_10_point = 1
    else:
        second_semester_grade_10_point = 0

    cp_1 = second_semester_grade_1_point * (int(second_Unit_1))
    cp_2 = second_semester_grade_2_point * (int(second_Unit_2))
    cp_3 = second_semester_grade_3_point * (int(second_Unit_3))
    cp_4 = second_semester_grade_4_point * (int(second_Unit_4))
    cp_5 = second_semester_grade_5_point * (int(second_Unit_5))
    cp_6 = second_semester_grade_6_point * (int(second_Unit_6))
    cp_7 = second_semester_grade_7_point * (int(second_Unit_7))
    cp_8 = second_semester_grade_8_point * (int(second_Unit_8))
    cp_9 = second_semester_grade_9_point * (int(second_Unit_9))
    cp_10 = second_semester_grade_10_point * (int(second_Unit_10))

    total_grade_point_2 = (second_semester_grade_1_point * (int(second_Unit_1)) + second_semester_grade_2_point
                           * (int(second_Unit_2))
                           + second_semester_grade_3_point * (int(second_Unit_3)) + second_semester_grade_4_point *
                           (int(second_Unit_4))
                           + second_semester_grade_5_point * (int(second_Unit_5)) + second_semester_grade_6_point *
                           (int(second_Unit_6)) +
                           second_semester_grade_7_point * (int(second_Unit_7)) + second_semester_grade_8_point *
                           (int(second_Unit_8))
                           + second_semester_grade_9_point * (int(second_Unit_9)) + second_semester_grade_10_point *
                           (int(second_Unit_10)))
    total_load_unit_2 = int(second_Unit_1) + int(second_Unit_2) + int(second_Unit_3) + int(second_Unit_4) +\
                        int(second_Unit_5) + int(second_Unit_6) + int(second_Unit_7) \
                      + int(second_Unit_8) + int(second_Unit_9) + int(second_Unit_10)

    gpa_2 = float(total_grade_point_2/total_load_unit_2)
    approximated_gpa_2 = round(gpa_2, 2)
    Total_grade_point_value_2.config(text=total_grade_point_2)
    TLU_2.config(text=total_load_unit_2)
    GPA_2.config(text=approximated_gpa_2)
    second_credit_point_1_label.config(text=cp_1)
    second_credit_point_2_label.config(text=cp_2)
    second_credit_point_3_label.config(text=cp_3)
    second_credit_point_4_label.config(text=cp_4)
    second_credit_point_5_label.config(text=cp_5)
    second_credit_point_6_label.config(text=cp_6)
    second_credit_point_7_label.config(text=cp_7)
    second_credit_point_8_label.config(text=cp_8)
    second_credit_point_9_label.config(text=cp_9)
    second_credit_point_10_label.config(text=cp_10)


def cgpa_cal():
    """This calculates the cgpa(cumulative grade point average) for the individual"""
    CGPA = cgpa_value_label
    first_semester_credit_point = total_credit_point_value_label.cget("text")
    second_semester_credit_point = total_credit_point_value_2_label.cget("text")
    first_semester_load_unit = total_load_unit_value_label.cget("text")
    second_semester_load_unit = total_load_unit_value_2_label.cget("text")
    TCP = first_semester_credit_point + second_semester_credit_point
    TLU = first_semester_load_unit + second_semester_load_unit
    cgpa = float(TCP / TLU)
    approximated_cgpa = round(cgpa,2)
    CGPA.config(text=approximated_cgpa)

# ------------------------------------------ CONSTANTS ---------------------------------------------------------------
FONT_NAME = "Courier"
# ------------------------------------------- UI SET_UP --------------------------------------------------------------
# window
win = Tk()

win.title("FUOYE SCREENING APPLICATION")
win.attributes("-fullscreen", True)
win.config(padx=10, pady=10)

# img
image = ImageTk.PhotoImage(Image.open("Desktop - 2 (3).png"))
image_label = Label(image=image)
image_label.grid(column=0, row=0)

image_2 = ImageTk.PhotoImage(Image.open("Frame 2 (1).png"))
image_2_label = Label(image=image_2)
image_2_label.place(x=0, y=200)

image_3 = ImageTk.PhotoImage(Image.open("Frame 2 (1).png"))
image_3_label = Label(image=image_3)
image_3_label.place(x=700, y=200)

# Label
student_details_label = Label(text="Student Details:", fg="black", font=(FONT_NAME, 10, "bold"))
student_details_label.place(x=0, y=130)
name_label = Label(text="Name:")
name_label.place(x=0, y=148)
matric_no_label = Label(text="Matric Number:")
matric_no_label.place(x=170, y=148)
dept_label = Label(text="Department:")
dept_label.place(x=390, y=148)
level_label = Label(text="Level:")
level_label.place(x=610, y=148)
gpa_label = Label(text="GPA:")
gpa_label.place(x=0, y=660)
gpa_value_label = Label(text="0.00", fg="black", font=(FONT_NAME,10, "bold"))
gpa_value_label.place(x=30, y=660)
total_credit_point_label = Label(text="Total Credit Unit:", fg="black", font=(FONT_NAME,10, "bold"))
total_credit_point_label.place(x=0, y=620)
total_credit_point_value_label = Label(text="000", fg="black", font=(FONT_NAME,10, "bold"))
total_credit_point_value_label.place(x=148, y=620)
total_load_unit_label = Label(text="Total Load Unit:", fg="black", font=(FONT_NAME,10, "bold"))
total_load_unit_label.place(x=0, y=640)
total_load_unit_value_label = Label(text="00", fg="black", font=(FONT_NAME,10, "bold"))
total_load_unit_value_label.place(x=130, y=640)

gpa_2_label = Label(text="GPA:")
gpa_2_label.place(x=730, y=660)
gpa_2_value_label = Label(text="0.00", fg="black", font=(FONT_NAME,10, "bold"))
gpa_2_value_label.place(x=760, y=660)
total_credit_point_2_label = Label(text="Total Credit Unit:", fg="black", font=(FONT_NAME,10, "bold"))
total_credit_point_2_label.place(x=730, y=620)
total_credit_point_value_2_label = Label(text="000", fg="black", font=(FONT_NAME,10, "bold"))
total_credit_point_value_2_label.place(x=878, y=620)
total_load_unit_2_label = Label(text="Total Load Unit:", fg="black", font=(FONT_NAME,10, "bold"))
total_load_unit_2_label.place(x=730, y=640)
total_load_unit_value_2_label = Label(text="00", fg="black", font=(FONT_NAME,10, "bold"))
total_load_unit_value_2_label.place(x=860, y=640)


cgpa_label = Label(text="CGPA:")
cgpa_label.place(x=600, y=700)
cgpa_value_label = Label(text="0.00", fg="black", font=(FONT_NAME,10, "bold"))
cgpa_value_label.place(x=640, y=700)

# semester_label
first_semester_label =Label(text="First Semester:", fg="black", font=(FONT_NAME,10, "bold"))
first_semester_label.place(x=0, y=180)
second_semester_label =Label(text="Second Semester:", fg="black", font=(FONT_NAME,10, "bold"))
second_semester_label.place(x=700, y=180)


# Entry
name_entry = Entry(width=18)
name_entry.place(x=40, y=150)
matric_num_entry = Entry(width=18)
matric_num_entry.place(x=260, y=148)
dept_entry = Entry(width=22)
dept_entry.place(x=460, y=148)
level_entry = Entry(width=10)
level_entry.place(x=650, y=148)

# first_semester
course_1_entry = Entry(width=20)
course_1_entry.place(x=30, y=290)
course_2_entry = Entry(width=20)
course_2_entry.place(x=30, y=320)
course_3_entry = Entry(width=20)
course_3_entry.place(x=30, y=350)
course_4_entry = Entry(width=20)
course_4_entry.place(x=30, y=380)
course_5_entry = Entry(width=20)
course_5_entry.place(x=30, y=410)
course_6_entry = Entry(width=20)
course_6_entry.place(x=30, y=440)
course_7_entry = Entry(width=20)
course_7_entry.place(x=30, y=470)
course_8_entry = Entry(width=20)
course_8_entry.place(x=30, y=500)
course_9_entry = Entry(width=20)
course_9_entry.place(x=30, y=530)
course_10_entry = Entry(width=20)
course_10_entry.place(x=30, y=560)
course_11_entry = Entry(width=20)
course_11_entry.place(x=30, y=590)

# unit_entry
unit_1 = Entry(width=5)
unit_1.place(x=240, y=290)
unit_2 = Entry(width=5)
unit_2.place(x=240, y=320)
unit_3 = Entry(width=5)
unit_3.place(x=240, y=350)
unit_4 = Entry(width=5)
unit_4.place(x=240, y=380)
unit_5 = Entry(width=5)
unit_5.place(x=240, y=410)
unit_6 = Entry(width=5)
unit_6.place(x=240, y=440)
unit_7 = Entry(width=5)
unit_7.place(x=240, y=470)
unit_8 = Entry(width=5)
unit_8.place(x=240, y=500)
unit_9 = Entry(width=5)
unit_9.place(x=240, y=530)
unit_10 = Entry(width=5)
unit_10.place(x=240, y=560)
unit_11 = Entry(width=5)
unit_11.place(x=240, y=590)
# grade
grade_1 = Entry(width=5)
grade_1.place(x=352, y=290)
grade_2 = Entry(width=5)
grade_2.place(x=352, y=320)
grade_3 = Entry(width=5)
grade_3.place(x=352, y=350)
grade_4 = Entry(width=5)
grade_4.place(x=352, y=380)
grade_5 = Entry(width=5)
grade_5.place(x=352, y=410)
grade_6 = Entry(width=5)
grade_6.place(x=352, y=440)
grade_7 = Entry(width=5)
grade_7.place(x=352, y=470)
grade_8 = Entry(width=5)
grade_8.place(x=352, y=500)
grade_9 = Entry(width=5)
grade_9.place(x=352, y=530)
grade_10 = Entry(width=5)
grade_10.place(x=352, y=560)
grade_11 = Entry(width=5)
grade_11.place(x=352, y=590)

# credit_point
credit_point_1_label = Label(text= "0", fg="black", font=(FONT_NAME,10, "bold"))
credit_point_1_label.place(x=490, y=290)
credit_point_2_label = Label(text= "0", fg="black", font=(FONT_NAME,10, "bold"))
credit_point_2_label.place(x=490, y=320)
credit_point_3_label = Label(text= "0", fg="black", font=(FONT_NAME,10, "bold"))
credit_point_3_label.place(x=490, y=350)
credit_point_4_label = Label(text= "0", fg="black", font=(FONT_NAME,10, "bold"))
credit_point_4_label.place(x=490, y=380)
credit_point_5_label = Label(text= "0", fg="black", font=(FONT_NAME,10, "bold"))
credit_point_5_label.place(x=490, y=410)
credit_point_6_label = Label(text= "0", fg="black", font=(FONT_NAME,10, "bold"))
credit_point_6_label.place(x=490, y=440)
credit_point_7_label = Label(text= "0", fg="black", font=(FONT_NAME,10, "bold"))
credit_point_7_label.place(x=490, y=470)
credit_point_8_label = Label(text= "0", fg="black", font=(FONT_NAME,10, "bold"))
credit_point_8_label.place(x=490, y=500)
credit_point_9_label = Label(text= "0", fg="black", font=(FONT_NAME,10, "bold"))
credit_point_9_label.place(x=490, y=530)
credit_point_10_label = Label(text= "0", fg="black", font=(FONT_NAME,10, "bold"))
credit_point_10_label.place(x=490, y=560)
credit_point_11_label = Label(text= "0", fg="black", font=(FONT_NAME,10, "bold"))
credit_point_11_label.place(x=490, y=590)

second_credit_point_1_label = Label(text= "0", fg="black", font=(FONT_NAME,10, "bold"))
second_credit_point_3_label = Label(text= "0", fg="black", font=(FONT_NAME,10, "bold"))
second_credit_point_3_label.place(x=1200, y=350)
second_credit_point_4_label = Label(text= "0", fg="black", font=(FONT_NAME,10, "bold"))
second_credit_point_1_label.place(x=1200, y=290)
second_credit_point_4_label.place(x=1200, y=380)
second_credit_point_5_label = Label(text= "0", fg="black", font=(FONT_NAME,10, "bold"))
second_credit_point_2_label = Label(text= "0", fg="black", font=(FONT_NAME,10, "bold"))
second_credit_point_2_label.place(x=1200, y=320)
second_credit_point_5_label.place(x=1200, y=410)
second_credit_point_6_label = Label(text= "0", fg="black", font=(FONT_NAME,10, "bold"))
second_credit_point_6_label.place(x=1200, y=440)
second_credit_point_7_label = Label(text= "0", fg="black", font=(FONT_NAME,10, "bold"))
second_credit_point_7_label.place(x=1200, y=470)
second_credit_point_8_label = Label(text= "0", fg="black", font=(FONT_NAME,10, "bold"))
second_credit_point_8_label.place(x=1200, y=500)
second_credit_point_9_label = Label(text= "0", fg="black", font=(FONT_NAME,10, "bold"))
second_credit_point_9_label.place(x=1200, y=530)
second_credit_point_10_label = Label(text= "0", fg="black", font=(FONT_NAME,10, "bold"))
second_credit_point_10_label.place(x=1200, y=560)

# second_semester
second_semester_course_1_entry = Entry(width=20)
second_semester_course_1_entry.place(x=730, y=290)
second_semester_course_2_entry = Entry(width=20)
second_semester_course_2_entry.place(x=730, y=320)
second_semester_course_3_entry = Entry(width=20)
second_semester_course_3_entry.place(x=730, y=350)
second_semester_course_4_entry = Entry(width=20)
second_semester_course_4_entry.place(x=730, y=380)
second_semester_course_5_entry = Entry(width=20)
second_semester_course_5_entry.place(x=730, y=410)
second_semester_course_6_entry = Entry(width=20)
second_semester_course_6_entry.place(x=730, y=440)
second_semester_course_7_entry = Entry(width=20)
second_semester_course_7_entry.place(x=730, y=470)
second_semester_course_8_entry = Entry(width=20)
second_semester_course_8_entry.place(x=730, y=500)
second_semester_course_9_entry = Entry(width=20)
second_semester_course_9_entry.place(x=730, y=530)
second_semester_course_10_entry = Entry(width=20)
second_semester_course_10_entry.place(x=730, y=560)
# unit
second_semester_unit_1_entry = Entry(width=5)
second_semester_unit_1_entry.place(x=940, y=290)
second_semester_unit_2_entry = Entry(width=5)
second_semester_unit_2_entry.place(x=940, y=320)
second_semester_unit_3_entry = Entry(width=5)
second_semester_unit_3_entry.place(x=940, y=350)
second_semester_unit_4_entry = Entry(width=5)
second_semester_unit_4_entry.place(x=940, y=380)
second_semester_unit_5_entry = Entry(width=5)
second_semester_unit_5_entry.place(x=940, y=410)
second_semester_unit_6_entry = Entry(width=5)
second_semester_unit_6_entry.place(x=940, y=440)
second_semester_unit_7_entry = Entry(width=5)
second_semester_unit_7_entry.place(x=940, y=470)
second_semester_unit_8_entry = Entry(width=5)
second_semester_unit_8_entry.place(x=940, y=500)
second_semester_unit_9_entry = Entry(width=5)
second_semester_unit_9_entry.place(x=940, y=530)
second_semester_unit_10_entry = Entry(width=5)
second_semester_unit_10_entry.place(x=940, y=560)
# grade
second_semester_grade_1 = Entry(width=5)
second_semester_grade_1.place(x=1060, y=290)
second_semester_grade_2 = Entry(width=5)
second_semester_grade_2.place(x=1060, y=320)
second_semester_grade_3 = Entry(width=5)
second_semester_grade_3.place(x=1060, y=350)
second_semester_grade_4 = Entry(width=5)
second_semester_grade_4.place(x=1060, y=380)
second_semester_grade_5 = Entry(width=5)
second_semester_grade_5.place(x=1060, y=410)
second_semester_grade_6 = Entry(width=5)
second_semester_grade_6.place(x=1060, y=440)
second_semester_grade_7 = Entry(width=5)
second_semester_grade_7.place(x=1060, y=470)
second_semester_grade_8 = Entry(width=5)
second_semester_grade_8.place(x=1060, y=500)
second_semester_grade_9 = Entry(width=5)
second_semester_grade_9.place(x=1060, y=530)
second_semester_grade_10 = Entry(width=5)
second_semester_grade_10.place(x=1060, y=560)
# button
gpa_button = Button(text= "Calculate GPA", command=calculator_1)
gpa_button.place(x=390, y=650)
gpa_button_2 = Button(text= "Calculate GPA_2", command=calculator_2)
gpa_button_2.place(x=1170, y=650)
cgpa_button = Button(text= "Calculate CGPA", command=cgpa_cal)
cgpa_button.place(x=600, y=720)
save_button = Button(text= "Save", command=save)
save_button.place(x=1200, y=720)
search_button = Button(text= "SEARCH RESULT")
search_button.place(x=1170, y=148)
# main_loop
win.mainloop()
# --------------------------------Please Handle My Project Source Code With Care----------------------------------------
#---------------------------------------------------THE END-------------------------------------------------------------
