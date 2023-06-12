"""
Prediksi HK
"""

import numpy as np
from sklearn.ensemble import RandomForestRegressor

# Data yang diberikan
dates = [
    "Minggu, 11 Juni 2023",
    "Sabtu, 10 Juni 2023",
    "Jumat, 09 Juni 2023",
    "Kamis, 08 Juni 2023",
    "Rabu, 07 Juni 2023",
    "Selasa, 06 Juni 2023",
    "Senin, 05 Juni 2023",
    "Minggu, 04 Juni 2023",
    "Sabtu, 03 Juni 2023",
    "Jumat, 02 Juni 2023",
    "Kamis, 01 Juni 2023",
    "Rabu, 31 Mei 2023",
    "Selasa, 30 Mei 2023",
    "Senin, 29 Mei 2023",
    "Minggu, 28 Mei 2023",
]
values = [
    2185,
    3591,
    8949,
    1337,
    4611,
    7752,
    4178,
    1964,
    7089,
    "0626",
    6409,
    5124,
    "0492",
    9545,
    1356,
]

# Mengubah tanggal menjadi fitur numerik
formatted_dates = np.arange(len(dates)).reshape(-1, 1)

# Inisialisasi dan latih model Random Forest Regression
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(formatted_dates, values)

# Prediksi angka berikutnya
next_date = "Senin, 12 Juni 2023"
next_formatted_date = len(dates)
prediction = model.predict([[next_formatted_date]])

# Tampilkan hasil prediksi
print(f"{next_date}\t{int(prediction)}")

"""
Output:
Senin, 12 Juni 2023	    4262
"""
