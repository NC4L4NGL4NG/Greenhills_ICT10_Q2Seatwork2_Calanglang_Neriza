from pyscript import document

def compute_gwa():
    grades = [
        float(document.getElementById("science").value),
        float(document.getElementById("english").value),
        float(document.getElementById("ict").value),
        float(document.getElementById("math").value),
        float(document.getElementById("filipino").value)
    ]

    total = sum(grades)
    gwa = total / 5

    output = document.getElementById("result")
    output.textContent = f"Your GWA is: {gwa}"
