import requests
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

API_KEY = "047c61cf7aa0b048243b8906c6aa049c"

# ---------------- WEATHER FUNCTION ----------------
def get_weather():
    city = city_entry.get().strip()

    if city == "":
        messagebox.showwarning("Input Error", "Enter city name")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={API_KEY}&units=metric"

    try:
        res = requests.get(url)
        data = res.json()

        if res.status_code == 200:
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            condition = data["weather"][0]["description"]
            wind = data["wind"]["speed"]

            now = datetime.now().strftime("%d %b %Y | %I:%M %p")

            # Smart Suggestion
            if "rain" in condition:
                suggestion = "🌧 Carry an umbrella"
            elif temp > 30:
                suggestion = "☀ Stay hydrated"
            elif temp < 15:
                suggestion = "🧥 Wear warm clothes"
            else:
                suggestion = "😊 Weather is pleasant"

            city_label.config(text=f"📍 {city}")
            time_label.config(text=now)
            temp_label.config(text=f"{temp}°C")
            details_label.config(
                text=f"{condition}\n💧 {humidity}% humidity\n🌬 {wind} m/s wind\n\n{suggestion}"
            )

        else:
            messagebox.showerror("Error", data.get("message", "City not found"))

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------- AUTO LOCATION ----------------
def detect_location():
    try:
        res = requests.get("http://ip-api.com/json/")
        data = res.json()
        city_entry.delete(0, tk.END)
        city_entry.insert(0, data["city"])
    except:
        messagebox.showerror("Error", "Location failed")


# ---------------- WEATHER WINDOW ----------------
def open_weather_app():
    global city_entry, city_label, temp_label, details_label, time_label

    app = tk.Tk()
    app.title("Smart Weather App")
    app.geometry("500x600")
    app.configure(bg="#0f172a")

    tk.Label(app, text="🌦 Smart Weather App", font=("Helvetica", 22, "bold"),
             fg="white", bg="#0f172a").pack(pady=10)

    frame = tk.Frame(app, bg="#0f172a")
    frame.pack(pady=10)

    city_entry = tk.Entry(frame, font=("Arial", 14), width=22, justify="center")
    city_entry.grid(row=0, column=0, padx=10)

    tk.Button(frame, text="Search", bg="#2563eb", fg="white",
              command=get_weather).grid(row=0, column=1)

    tk.Button(app, text="📍 Detect Location", bg="#16a34a",
              fg="white", command=detect_location).pack(pady=8)

    card = tk.Frame(app, bg="#1e293b", bd=3, relief="ridge")
    card.pack(pady=30, padx=20, fill="both")

    city_label = tk.Label(card, text="", font=("Arial", 18, "bold"),
                          fg="white", bg="#1e293b")
    city_label.pack(pady=10)

    time_label = tk.Label(card, text="", font=("Arial", 10),
                          fg="gray", bg="#1e293b")
    time_label.pack()

    temp_label = tk.Label(card, text="", font=("Arial", 50, "bold"),
                          fg="#38bdf8", bg="#1e293b")
    temp_label.pack()

    details_label = tk.Label(card, text="", font=("Arial", 12),
                             fg="white", bg="#1e293b", justify="center")
    details_label.pack(pady=10)

    tk.Button(app, text="🔄 Refresh", bg="#f59e0b",
              command=get_weather).pack(pady=10)

    tk.Label(app, text="Powered by OpenWeatherMap",
             fg="gray", bg="#0f172a").pack(side="bottom", pady=10)

    app.mainloop()


# ---------------- LOGIN ----------------
def login():
    if username.get() == "admin" and password.get() == "1234":
        login_win.destroy()
        open_weather_app()
    else:
        messagebox.showerror("Error", "Invalid login")


# ---------------- LOGIN UI ----------------
login_win = tk.Tk()
login_win.title("Login")
login_win.geometry("350x300")
login_win.configure(bg="#0f172a")

tk.Label(login_win, text="🔐 Login", font=("Helvetica", 20, "bold"),
         fg="white", bg="#0f172a").pack(pady=20)

username = tk.Entry(login_win, font=("Arial", 14), justify="center")
username.pack(pady=10)
username.insert(0, "admin")

password = tk.Entry(login_win, font=("Arial", 14), justify="center", show="*")
password.pack(pady=10)
password.insert(0, "1234")

tk.Button(login_win, text="Login", bg="#2563eb", fg="white",
          command=login).pack(pady=20)

login_win.mainloop()