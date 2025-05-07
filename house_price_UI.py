import tkinter as tk
from tkinter import ttk
import joblib

# Load the trained model
model = joblib.load("house_price_model.pkl")

# Custom popup for prediction result
def show_custom_popup(price):
    popup = tk.Toplevel(root)
    popup.title("Prediction Result")
    popup.configure(bg="#D6EAF8")
    popup.geometry("400x200")
    popup.resizable(False, False)

    label = tk.Label(
        popup,
        text=f"🏷 Estimated Price:\n₹{price:,.2f}",
        font=("Segoe UI", 18, "bold"),
        bg="#D6EAF8",
        fg="#154360",
        pady=40
    )
    label.pack()

    close_button = ttk.Button(popup, text="Close", command=popup.destroy)
    close_button.pack(pady=10)

# Predict function
def predict_price():
    try:
        inputs = [
            int(entry_bedrooms.get()), float(entry_bathrooms.get()),
            float(entry_living_area.get()), float(entry_lot_area.get()),
            float(entry_floors.get()), int(entry_waterfront.get()),
            int(entry_condition.get()), int(entry_grade.get()),
            float(entry_area_excl_basement.get()), float(entry_area_basement.get()),
            int(entry_built_year.get()), int(entry_renov_year.get()),
            float(entry_living_area_renov.get()), float(entry_lot_area_renov.get()),
            int(entry_schools_nearby.get()), float(entry_distance_airport.get())
        ]
        price = model.predict([inputs])[0]
        show_custom_popup(price)
    except Exception as e:
        show_custom_popup(f"Error!\n{str(e)}")

# Main window
root = tk.Tk()
root.title("🏡 House Price Predictor")
root.geometry("620x750")
root.configure(bg="#D6EAF8")  # Light blue background

style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#D6EAF8", font=("Segoe UI", 11))
style.configure("TEntry", font=("Segoe UI", 11))
style.configure("TButton", font=("Segoe UI", 11, "bold"))

# Title
tk.Label(
    root,
    text="House Price Predictor",
    font=("Segoe UI", 18, "bold"),
    bg="#D6EAF8",
    fg="#1A5276"
).pack(pady=20)

# Form frame
frame = tk.Frame(root, bg="#D6EAF8")
frame.pack()

labels = [
    "Bedrooms", "Bathrooms", "Living Area (sq ft)", "Lot Area (sq ft)",
    "Floors", "Waterfront (0/1)", "Condition (1–5)", "Grade (1–13)",
    "Area excl. Basement", "Basement Area", "Built Year", "Renovation Year",
    "Living Area (Renov)", "Lot Area (Renov)", "Schools Nearby", "Distance to Airport"
]

entries = []
for i, text in enumerate(labels):
    ttk.Label(frame, text=text).grid(row=i, column=0, sticky="e", padx=15, pady=6)
    entry = ttk.Entry(frame, width=30)
    entry.grid(row=i, column=1, padx=15, pady=6)
    entries.append(entry)

(
    entry_bedrooms, entry_bathrooms, entry_living_area, entry_lot_area,
    entry_floors, entry_waterfront, entry_condition, entry_grade,
    entry_area_excl_basement, entry_area_basement, entry_built_year,
    entry_renov_year, entry_living_area_renov, entry_lot_area_renov,
    entry_schools_nearby, entry_distance_airport
) = entries

# Predict Button
ttk.Button(
    root,
    text="💰 Predict Price",
    command=predict_price
).pack(pady=30)

root.mainloop()
