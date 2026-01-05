from pyscript import document

def compute_gwa(e):
    result_box = document.getElementById("result")
    
    try:
        g1 = float(document.getElementById('science').value)
        g2 = float(document.getElementById('english').value)
        g3 = float(document.getElementById('ict').value)
        g4 = float(document.getElementById('math').value)
        g5 = float(document.getElementById('filipino').value)

        gwa_total = (g1 + g2 + g3 + g4 + g5) / 5

        if gwa_total > 74:
            status = "PASSED"
        else:
            status = "FAILED"

        result_box.textContent = f"Your GWA is: {gwa_total:.2f} ({status})"

    except ValueError:
        result_box.textContent = "Please enter valid numbers in all fields."
