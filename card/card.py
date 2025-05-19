from reportlab.lib.pagesizes import inch
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader

# === User-editable variables ===
logo_path = "/Users/franrota/Documents/P.IVA/logo.png"          # Path to your logo file
output_pdf = "/Users/franrota/Documents/P.IVA/calling_card.pdf" # Output PDF file name

# Card dimensions (3.5" x 2")
width, height = 3.5 * inch, 2 * inch

# Create the PDF canvas
c = canvas.Canvas(output_pdf, pagesize=(width, height))

# --- Front Page (English) ---

# Draw the logo
logo = ImageReader(logo_path)
logo_size = 0.5 * inch
c.drawImage(logo, x=0.01 * inch, y=height - 0.01 * inch - logo_size,
            width=logo_size, height=logo_size, mask='auto')

# Header: Name
c.setFont("Helvetica-Bold", 12)
c.setFillColor(colors.HexColor("#2E8B57"))  # Forest Green
c.drawString(0.5 * inch, height - 0.4 * inch, "Francesco Rota, PhD")

# Subheader: Roles
c.setFont("Helvetica", 9)
c.setFillColor(colors.HexColor("#4F4F4F"))  # Charcoal Grey
c.drawString(0.5 * inch, height - 0.6 * inch,
             "Agrotechnician • Botanist • GIS • Data Scientist")

# Tagline
c.setFont("Helvetica-Oblique", 8)
c.drawString(0.5 * inch, height - 0.75 * inch,
             "Sustainable land use and ecosystem protection.")

# Contact details
contacts = [
    "Email: rotafran@outlook.com",
    "Phone: +39 334 36 12 133",
    "Web: https://francescorota93.github.io/franrota-website/",
    "LinkedIn: linkedin.com/in/francescorota93"
]
y_pos = height - 1.0 * inch
c.setFont("Helvetica", 7)
for line in contacts:
    c.drawString(0.1 * inch, y_pos, line)
    y_pos -= 0.12 * inch

# Bottom tagline
c.setFont("Helvetica-Oblique", 8)
c.drawString(0.7 * inch, height - 1.8 * inch,
             "Rooted in nature, powered by data")

# Finish front page
c.showPage()

# --- Back Page (Italian) ---

# Draw the logo (as watermark or top-left)
c.drawImage(logo, x=0.01 * inch, y=height - 0.01 * inch - logo_size,
            width=logo_size, height=logo_size, mask='auto')

# Header: Name
c.setFont("Helvetica-Bold", 12)
c.setFillColor(colors.HexColor("#2E8B57"))
c.drawString(0.5 * inch, height - 0.4 * inch, "Francesco Rota, PhD")

# Subheader: Ruoli
c.setFont("Helvetica", 9)
c.setFillColor(colors.HexColor("#4F4F4F"))
c.drawString(0.5 * inch, height - 0.6 * inch,
             "Agrotecnico • Botanico • GIS • Data Scientist")

# Tagline in Italian
c.setFont("Helvetica-Oblique", 8)
c.drawString(0.5 * inch, height - 0.75 * inch,
             "Uso sostenibile del territorio e protezione degli ecosistemi.")

# Contact details (Italian)
y_pos = height - 1.0 * inch
c.setFont("Helvetica", 7)
for line in contacts:
    c.drawString(0.1 * inch, y_pos, line)
    y_pos -= 0.12 * inch

# Bottom tagline in Italian
c.setFont("Helvetica-Oblique", 8)
c.drawString(0.7 * inch, height - 1.8 * inch,
             "Ricerca e ripristino della biodiversità.")

# Finish back page and save
c.showPage()
c.save()

print(f"Two-sided calling card saved as: {output_pdf}")
