from pyscript import document

def compute_gwa(e):
    try:
        g1 = float(document.getElementById('science').value)
        g2 = float(document.getElementById('english').value)
        g3 = float(document.getElementById('ict').value)
        g4 = float(document.getElementById('math').value)
        g5 = float(document.getElementById('filipino').value)

        gwa = (g1 + g2 + g3 + g4 + g5) / 5

        result = document.getElementById("result")
        result.textContent = f"Your GWA is: {gwa:.2f}"

    except:
        result = document.getElementById("result")
        result.textContent = "Please enter valid numbers in all fields."

