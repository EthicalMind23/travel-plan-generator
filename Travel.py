import pandas as pd
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

# Load dataset
def load_data(file_path):
    """Load dataset from CSV file."""
    return pd.read_csv(file_path)

# Function to get travel plan
def get_travel_plan(df, place_name, num_days):
    """Fetch travel plan for the selected place."""
    place_data = df[df["Place Name"].str.lower() == place_name.lower()]
    if place_data.empty:
        return "Place not found in the dataset."
    
    place_info = place_data.iloc[0]
    travel_plan = (
        f"\n🌍 Destination: {place_info['Place Name']}\n"
        f"📍 State: {place_info['State/Region']}\n"
        f"🗓 Best Time to Visit: {place_info['Best Time to Visit']}\n"
        f"🏛 Attractions: {place_info['Popular Attractions']}\n"
        f"⏳ Recommended Duration: {place_info['Recommended Duration']} days\n"
        f"💰 Budget Estimate: {place_info['Ideal Budget Range']}\n"
        f"🎯 Suitable for: {place_info['Suitable for']}\n"
        f"📝 Suggested Itinerary: {place_info['Sample Itinerary']}\n"
    )
    return travel_plan

# Display travel plan
def show_travel_plan():
    place_name = place_dropdown.get()
    try:
        num_days = int(days_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number of days.")
        return
    
    if not place_name or place_name == "Select a place":
        messagebox.showerror("Input Error", "Please select a place.")
        return
    
    travel_plan = get_travel_plan(df, place_name, num_days)
    result_text.config(state="normal")
    result_text.delete("1.0", "end")
    result_text.insert("end", travel_plan)
    result_text.config(state="disabled")

# Load Data
file_path = "india_tourist_places_large.csv"
df = load_data(file_path)
places_list = sorted(df["Place Name"].unique().tolist())

# Create Modern GUI
root = ttk.Window(themename="superhero")
root.title("Travel Plan Generator ✈️")
root.geometry("800x600")

# Header Label
header = ttk.Label(root, text="🌍 Travel Plan Generator", font=("Arial", 18, "bold"), bootstyle="primary")
header.pack(pady=10)

# Frame for Inputs
input_frame = ttk.Frame(root, padding=20)
input_frame.pack(pady=10, fill="x")

# Place Dropdown
ttk.Label(input_frame, text="Select Destination:", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5, sticky="w")
place_dropdown = ttk.Combobox(input_frame, values=places_list, width=40, font=("Arial", 10))
place_dropdown.grid(row=0, column=1, padx=5, pady=5)
place_dropdown.set("Select a place")

# Number of Days Entry
ttk.Label(input_frame, text="Enter Days:", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5, sticky="w")
days_entry = ttk.Entry(input_frame, width=10)
days_entry.grid(row=1, column=1, padx=5, pady=5)

# Fetch Travel Plan Button
ttk.Button(input_frame, text="Get Travel Plan", command=show_travel_plan, bootstyle="success").grid(row=2, columnspan=2, pady=10)

# Travel Plan Display
result_frame = ttk.Frame(root, padding=10)
result_frame.pack(fill="both", expand=True)

ttk.Label(result_frame, text="📜 Travel Plan (Per Person):", font=("Arial", 14, "bold")).pack(anchor="w")
result_text = ttk.Text(result_frame, wrap="word", font=("Arial", 10), height=10, width=70, state="disabled")
result_text.pack(pady=5, padx=10, fill="both", expand=True)

# Run Application
root.mainloop()
