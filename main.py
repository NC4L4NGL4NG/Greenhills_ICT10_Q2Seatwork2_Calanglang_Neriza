from pyscript import document

def compute_gwa(e):
    try:
        g1 = float(document.getElementById('Science').value)
        g2 = float(document.getElementById('English').value)
        g3 = float(document.getElementById('ICT').value)
        g4 = float(document.getElementById('Math').value)
        g5 = float(document.getElementById('Filipino').value)

        gwa = (g1 + g2 + g3 + g4 + g5) / 5
        display(f'Your GWA is {gwa:.2f}', target="output")
    except Exception:
        display(" Please enter valid numbers in all fields.", target="output")


    output = document.getElementById("result")
    output.textContent = f"Your GWA is: {gwa:.2f}"

