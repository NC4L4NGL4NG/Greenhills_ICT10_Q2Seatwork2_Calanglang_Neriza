from pyscript import document

UNIT_SCIENCE = 5.0
UNIT_ENGLISH = 3.0
UNIT_ICT = 2.0
UNIT_MATH = 5.0
UNIT_FILIPINO = 3.0

def compute_gwa():
    grade_science = float(document.getElementById("science").value)
    grade_english = float(document.getElementById("english").value)
    grade_ict = float(document.getElementById("ict").value)
    grade_math = float(document.getElementById("math").value)
    grade_filipino = float(document.getElementById("filipino").value)

    total_quality_points = (grade_science * UNIT_SCIENCE) + \
                           (grade_english * UNIT_ENGLISH) + \
                           (grade_ict * UNIT_ICT) + \
                           (grade_math * UNIT_MATH) + \
                           (grade_filipino * UNIT_FILIPINO)
  
    total_units = UNIT_SCIENCE + UNIT_ENGLISH + UNIT_ICT + UNIT_MATH + UNIT_FILIPINO
    

    gwa = total_quality_points / total_units

    output = document.getElementById("result")
    output.textContent = f"Your GWA is: {gwa:.2f}"
