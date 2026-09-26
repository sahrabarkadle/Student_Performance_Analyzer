# Name: Sahra Azhar Keid Barkadle
# Period: AM - AI Engineering
# Student Performance Analyzer

# Program Introduction

print("========================================")
print("STUDENT PERFORMANCE ANALYZER")
print("========================================")
print("Enter the student's information below.")
print()

# Asking user to input student information
student_name = input("What is the student's name?: ") # Student's name
grade_level = int(input("What grade level is the student in?: ")) # Student's grade level
assignment_avg = float(input("What is the student's assignment average?: ")) # Student's assginment average
quiz_avg = float(input("What is the student's quiz average?: ")) # Student's quiz average
test_avg = float(input("What is the student's test average?: ")) # Student's test average
attendance_perc = float(input("What is the student's attendance percentage: ")) # Student's attendace percentage
missing_assignments = int(input("How many missing assignments does the student have?: ")) # Student's amount of missing assginments
print()



# Calculating student's overall grade
def calculate_grade (assignment_average, quiz_average, test_average):
  assignment_portion = assignment_average * 0.30
  quiz_portion = quiz_average * 0.30
  test_portion = test_average * 0.40

  overall_grade = assignment_portion + quiz_portion + test_portion

  return overall_grade


overall_grade = calculate_grade(assignment_avg, quiz_avg, test_avg)

# Determining student's letter grade
def letter_grade(overall_grade):
  if overall_grade >= 90:
     return "Letter Grade: A"
  elif overall_grade >= 80:
     return "Letter Grade: B"
  elif overall_grade >= 70:
     return "Letter Grade: C"
  elif overall_grade >= 60:
     return "Letter Grade: D"
  else:
     return "Letter Grade: F"


let_grade = letter_grade(overall_grade)
 

# Determining student's attendance status
def attendance_status(attendance):
  if attendance >= 95:
     return "Attendance Status: Excellent Attendance"
  elif attendance >= 90:
     return "Attendance Status: Good Attendance"
  elif attendance >= 80:
     return "Attendance Status: Attendance Warning"
  else:
     return "Attendance Status: Poor Attendance"


attend_stat = attendance_status(attendance_perc)

# Determining student's assignment status
def assignment_status(missing_assignments):
  if missing_assignments == 0:
     return "Missing Assignment Status: Excellent"
  elif missing_assignments <= 2:
     return "Missing Assignment Status: Good"
  elif missing_assignments <= 4:
     return "Missing Assignment Status: Warning"
  else:
     return "Missing Assignment Status: Critical"


assign_stat = assignment_status(missing_assignments)

# Checking student's eligibilty
def check_eligibility(overall_grade, attendance, missing_assignments):
   if overall_grade >= 70:
       if attendance >= 90:
           if missing_assignments <= 2:
              return("Academic Eligibility: ELIGIBLE")
              return("Student passed all three requirments.")
           else:
               return("Academic Eligibility: NOT ELIGIBLE")
               return("Reason: Too many missing assignments.")
       else:
           return("Academic Eligibility: NOT ELIGIBLE")
           return("Reason: Attendance is too low.")
   else:
      return("Academic Eligibility: NOT ELIGIBLE")
      return("Reason: Overall grade is too low.")


eligibility = check_eligibility(overall_grade,attendance_perc,missing_assignments)

# Checking if student has high honors
def check_high_honors(overall_grade, attendance, missing_assignments):
  if overall_grade >= 90:
     if attendance >= 95:
        if missing_assignments == 0:
           return("High Honors: YES")
        else:
           return("High Honors: NO")
           return("Reason: Student has missing assignments.")
     else:
        return("High Honors: NO")
        return("Reason: Attendance requirement not met.")
  else:
     return("High Honors: NO")
     return("Reason: Grade requirement not met.")


high_honors = check_high_honors(overall_grade, attendance_perc, missing_assignments)

# Checking if student has good standing
def check_good_standing(overall_grade, attendance):
  if overall_grade >= 70 and attendance >= 90:
     return("Good Standing: YES")
  else:
     return("Good Standing: NO")


good_standing = check_good_standing(overall_grade, attendance_perc)

# Checking if support needed for student
def check_support(overall_grade, attendance):
  if overall_grade < 70 or attendance < 80:
     return("Additional Support: RECOMMENDED")
  else:
     return("Additional Support: NOT NEEDED")


support = check_support(overall_grade, attendance_perc)


# Student Login
username = input("Enter username: ")
pin = int(input("Enter PIN: "))

# Checking the login
def check_login(username,pin):
  if username == "student":
     if pin == 1234:
        return("Login Successful!")
     else:
        return("Login Failed: Incorrect PIN")
  else:
     return("Login Failed: Incorrect username")

login = check_login(username,pin)


# Grade-Level Message
def grade_level_message(grade_level):
  if grade_level == 9:
     return("Welcome to your freshman year!")
  elif grade_level == 10:
     return("Keep building your skills!")
  elif grade_level == 11:
     return("Keep pushing!")
  elif grade_level == 12:
     return("Finish strong!")
  else:
     return("Invalid grade level")


year = grade_level_message(grade_level)


# Strongest Academic Category
def strongest_category(assignment_average, quiz_average, test_average):
  if assignment_average > quiz_average and assignment_average > test_average:
     return("Strongest Category: Assignments")
  elif quiz_average > assignment_average and quiz_average > test_average:
     return("Strongest Category: Quizzes")
  elif test_average > assignment_average and test_average > quiz_average:
     return("Strongest Category: Tests")


category = strongest_category(assignment_avg, quiz_avg,test_avg)

# Checking student's advanced status
def check_advanced_status(overall_grade, attendance, missing_assignments):
  if (overall_grade >= 90 and attendance >= 95) or (overall_grade >= 85 and missing_assignments == 0):
     return ("OUTSTANDING STUDENT")
  else:
      return("STANDARD STUDENT STATUS")


advanced_status = check_advanced_status(overall_grade, attendance_perc,missing_assignments)
# Student Summary


print("============ Student Summary ============")
print()


print("Student: ",student_name)
print("Grade Level: ", grade_level)
print()


print("Assignment Average: ",assignment_avg)
print("Quiz Average: ",quiz_avg)
print("Test Average: ",test_avg)
print()


print("Overall Grade: ",overall_grade)
print("Attendance: ", attendance_perc)
print("Missing Assignments: ", missing_assignments)
print("Advanced Status: ",advanced_status)
print()

print("============THANK YOU============")