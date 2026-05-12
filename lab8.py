import tkinter as tk
from tkinter import ttk

FONT = ("Arial", 11)
FONT_B = ("Arial", 11, "bold")
FONT_H = ("Arial", 13, "bold")

BG = "#eaf0fb"
WHITE = "#ffffff"
BLUE = "#3a6fd8"
BLUE_ACT = "#5a8aec"
GREEN = "#217a3c"

root = tk.Tk()
root.title("Калькулятор здоровья")
root.geometry("500x750")
root.resizable(False, True)
root.configure(bg=BG)

IMAGE = tk.PhotoImage(file="health.png").subsample(20,20)

bmi_frame = tk.Frame(root, bg=WHITE, bd=1, relief="solid", padx=14, pady=12)
bmi_frame.pack(fill="x", padx=14, pady=(14, 6))

tk.Label(bmi_frame, text="Индекс массы тела", font=FONT_H, bg=WHITE, fg=BLUE).grid(row=0, column=0, columnspan=4, sticky="w", pady=(0, 8))

tk.Label(bmi_frame, text="Рост (см):", font=FONT, bg=WHITE).grid(row=1, column=0, sticky="w")
height_var = tk.StringVar(value=None)
tk.Entry(bmi_frame, textvariable=height_var, width=7, font=FONT, bg="#f0f4ff").grid(row=1, column=1, sticky="w", padx=(5, 16))

tk.Label(bmi_frame, text="Вес (кг):", font=FONT, bg=WHITE).grid(row=1, column=2, sticky="w")
weight_var = tk.StringVar(value=None)
tk.Entry(bmi_frame, textvariable=weight_var, width=7, font=FONT, bg="#f0f4ff").grid(row=1, column=3, sticky="w", padx=(5, 0))

tk.Label(bmi_frame, text="Пол:", font=FONT, bg=WHITE).grid(row=2, column=0, sticky="w", pady=(8, 0))
gender_var = tk.StringVar(value=None)
ttk.Combobox(bmi_frame, textvariable=gender_var, values=["Мужской", "Женский"], width=12, state="readonly", font=FONT).grid(row=2, column=1, columnspan=2, sticky="w", padx=(5, 0), pady=(8, 0))

bmi_result_var = tk.StringVar()
tk.Label(bmi_frame, textvariable=bmi_result_var, font=FONT, bg=WHITE, fg=GREEN, wraplength=440, justify="left").grid(row=4, column=0, columnspan=4, sticky="w", pady=(8, 0))

def calculate_bmi():
    try:
        h = float(height_var.get()) / 100
        w = float(weight_var.get())
        bmi = w / h ** 2
        categories = [
            (16,   "Выраженный дефицит"),
            (18.5, "Недостаточный вес"),
            (25,   "Норма"),
            (30,   "Избыточный вес"),
            (35,   "Ожирение I"),
            (40,   "Ожирение II"),
        ]
        category = "Ожирение III"
        for threshold, name in categories:
            if bmi < threshold:
                category = name
                break
        ideal_min = round(18.5 * h ** 2, 1)
        ideal_max = round(24.9 * h ** 2, 1)
        bmi_result_var.set(
            f"ИМТ = {bmi:.1f}  —  {category}\n"
            f"Идеальный вес: {ideal_min} – {ideal_max} кг"
        )
    except:
        bmi_result_var.set("Введите корректные числа")

tk.Button(bmi_frame, text="Рассчитать ИМТ", command=calculate_bmi,
          bg=BLUE, fg="white", font=FONT_B, relief="flat",
          padx=10, pady=5, cursor="hand2",
          activebackground=BLUE_ACT, activeforeground="white", image=IMAGE, compound=tk.LEFT).grid(
    row=3, column=0, columnspan=2, sticky="w", pady=(10, 0))



cal_frame = tk.Frame(root, bg=WHITE, bd=1, relief="solid", padx=14, pady=12)
cal_frame.pack(fill="x", padx=14, pady=6)

tk.Label(cal_frame, text="Суточная норма калорий", font=FONT_H, bg=WHITE, fg=BLUE).grid(row=0, column=0, columnspan=4, sticky="w", pady=(0, 8))

tk.Label(cal_frame, text="Возраст:", font=FONT, bg=WHITE).grid(row=1, column=0, sticky="w")
age_var = tk.StringVar(value=None)
tk.Entry(cal_frame, textvariable=age_var, width=7, font=FONT, bg="#f0f4ff").grid(
    row=1, column=1, sticky="w", padx=(5, 16))

tk.Label(cal_frame, text="Цель:", font=FONT, bg=WHITE).grid(row=1, column=2, sticky="w")
goal_var = tk.StringVar(value=None)
ttk.Combobox(cal_frame, textvariable=goal_var, values=["Похудение", "Поддержание", "Набор массы"], width=13, state="readonly", font=FONT).grid(row=1, column=3, sticky="w", padx=(5, 0))

tk.Label(cal_frame, text="Активность:", font=FONT, bg=WHITE).grid(row=2, column=0, sticky="w", pady=(8, 0))
activity_labels = ["Сидячий", "Лёгкая", "Умеренная", "Высокая", "Очень высокая"]
activity_coeffs = [1.2, 1.375, 1.55, 1.725, 1.9]
activity_var = tk.StringVar(value=None)
ttk.Combobox(cal_frame, textvariable=activity_var, values=activity_labels,
             width=16, state="readonly", font=FONT).grid(
    row=2, column=1, columnspan=3, sticky="w", padx=(5, 0), pady=(8, 0))

tk.Label(cal_frame, text="Показать:", font=FONT, bg=WHITE).grid(row=3, column=0, sticky="w", pady=(8, 0))
show_protein_var = tk.BooleanVar(value=True)
show_fat_var = tk.BooleanVar(value=True)
show_carb_var = tk.BooleanVar(value=True)

tk.Checkbutton(cal_frame, text="Белки", variable=show_protein_var, bg=WHITE, font=FONT, activebackground=WHITE).grid(row=3, column=1, sticky="w", pady=(8, 0))
tk.Checkbutton(cal_frame, text="Жиры", variable=show_fat_var, bg=WHITE, font=FONT, activebackground=WHITE).grid(row=3, column=2, sticky="w", pady=(8, 0))
tk.Checkbutton(cal_frame, text="Углеводы", variable=show_carb_var, bg=WHITE, font=FONT, activebackground=WHITE).grid(row=3, column=3, sticky="w", pady=(8, 0))

cal_result_var = tk.StringVar()
tk.Label(cal_frame, textvariable=cal_result_var, font=FONT, bg=WHITE, fg=GREEN, justify="left").grid(row=5, column=0, columnspan=4, sticky="w", pady=(8, 0))

def calculate_calories():
    try:
        h = float(height_var.get())
        w = float(weight_var.get())
        age = float(age_var.get())

        if gender_var.get() == "Мужской":
            bmr = 10 * w + 6.25 * h - 5 * age + 5
        else:
            bmr = 10 * w + 6.25 * h - 5 * age - 161

        coeff = activity_coeffs[activity_labels.index(activity_var.get())]
        tdee = bmr * coeff

        if goal_var.get() == "Похудение":
            tdee -= 500
        elif goal_var.get() == "Набор массы":
            tdee += 300

        lines = [f"Калории: {tdee:.0f} ккал/день"]
        if show_protein_var.get():
            lines.append(f"Белки: {tdee * 0.30 / 4:.0f} г")
        if show_fat_var.get():
            lines.append(f"Жиры: {tdee * 0.25 / 9:.0f} г")
        if show_carb_var.get():
            lines.append(f"Углеводы: {tdee * 0.45 / 4:.0f} г")

        cal_result_var.set("\n".join(lines))
    except:
        cal_result_var.set("Заполните рост, вес, возраст")

tk.Button(cal_frame, text="Рассчитать калории", command=calculate_calories,
          bg=BLUE, fg="white", font=FONT_B, relief="flat",
          padx=10, pady=5, cursor="hand2",
          activebackground=BLUE_ACT, activeforeground="white", image=IMAGE, compound=tk.LEFT).grid(
    row=4, column=0, columnspan=2, sticky="w", pady=(10, 0))


water_frame = tk.Frame(root, bg=WHITE, bd=1, relief="solid", padx=14, pady=12)
water_frame.pack(fill="x", padx=14, pady=(6, 14))

tk.Label(water_frame, text="Норма воды в день", font=FONT_H, bg=WHITE, fg=BLUE).grid(row=0, column=0, columnspan=4, sticky="w", pady=(0, 8))

tk.Label(water_frame, text="Климат:", font=FONT, bg=WHITE).grid(row=1, column=0, sticky="w")
climate_var = tk.StringVar(value=None)
ttk.Combobox(water_frame, textvariable=climate_var,
             values=["Холодный", "Умеренный", "Жаркий"],
             width=11, state="readonly", font=FONT).grid(
    row=1, column=1, sticky="w", padx=(5, 16))

tk.Label(water_frame, text="Тренировки:", font=FONT, bg=WHITE).grid(row=1, column=2, sticky="w")
workout_var = tk.StringVar(value=None)
ttk.Combobox(water_frame, textvariable=workout_var,
             values=["Нет", "Лёгкие", "Интенсивные"],
             width=11, state="readonly", font=FONT).grid(
    row=1, column=3, sticky="w", padx=(5, 0))

tk.Label(water_frame, text="Вес (кг):", font=FONT, bg=WHITE).grid(row=2, column=0, sticky="w", pady=(8, 2))
slider_weight_var = tk.IntVar(value="70")
slider_label = tk.Label(water_frame, text="70 кг", font=FONT, bg=WHITE, fg=BLUE)
slider_label.grid(row=2, column=1, sticky="w", padx=(5, 0), pady=(8, 2))

tk.Scale(water_frame, from_=30, to=200, orient="horizontal",
         variable=slider_weight_var, length=350, bg=WHITE,
         highlightthickness=0, font=FONT,
         command=lambda value: slider_label.config(text=f"{value} кг")).grid(row=3, column=0, columnspan=4, sticky="w")

water_result_var = tk.StringVar()
tk.Label(water_frame, textvariable=water_result_var, font=FONT, bg=WHITE, fg=GREEN, justify="left").grid(row=5, column=0, columnspan=4, sticky="w", pady=(8, 0))

def calculate_water():
    try:
        weight = float(slider_weight_var.get())
        base_water = weight * 35

        climate_bonus = {
            "Холодный": 0,
            "Умеренный": 200,
            "Жаркий": 500
        }

        workout_bonus = {
            "Нет": 0,
            "Лёгкие": 350,
            "Интенсивные": 700
        }

        total_water = base_water + climate_bonus[climate_var.get()] + workout_bonus[workout_var.get()]

        water_result_var.set(
            f"Норма воды: {total_water / 1000:.1f} л/день\n"
            f"Примерно {total_water / 250:.0f} стаканов по 250 мл"
        )
    except:
        water_result_var.set("Ошибка расчёта")

tk.Button(water_frame, text="Рассчитать норму воды", command=calculate_water,
          bg=BLUE, fg="white", font=FONT_B, relief="flat",
          padx=10, pady=5, cursor="hand2",
          activebackground=BLUE_ACT, activeforeground="white", image=IMAGE, compound=tk.LEFT).grid(row=4, column=0, columnspan=2, sticky="w", pady=(10, 0))

root.mainloop()