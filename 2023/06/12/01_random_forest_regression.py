import datetime
import locale
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib

# Set locale ke bahasa Indonesia
locale.setlocale(locale.LC_TIME, "id_ID")

# Baca dataset
dataset = pd.read_csv("2023/06/12/togel.csv")

# Ambil kolom tanggal dan angka HK
tanggal_hk = dataset["tanggal"].values.tolist()
angka_hk = dataset["keluaran"].values.tolist()

# Mengubah tanggal menjadi fitur numerik
numerical_dates = np.arange(len(tanggal_hk)).reshape(-1, 1)

# Inisialisasi dan latih model Random Forest Regression
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(numerical_dates, angka_hk)

# Ambil tanggal terakhir dari dataset
last_date = tanggal_hk[-1]

# Hitung tanggal berikutnya berdasarkan tanggal terakhir
last_date_datetime = datetime.datetime.strptime(last_date, "%A, %d %B %Y")
next_date_datetime = last_date_datetime + datetime.timedelta(days=1)
next_date = next_date_datetime.strftime("%A, %d %B %Y")

# Mengubah tanggal prediksi menjadi fitur numerik
next_numerical_date = len(tanggal_hk)

# Prediksi angka berikutnya
prediction = model.predict([[next_numerical_date]])

# Tampilkan hasil prediksi
print(f"{next_date}\t{int(prediction)}")


# Validasi input
def validate_input(tanggal_hk, angka_hk):
    if len(tanggal_hk) != len(angka_hk):
        raise ValueError("Jumlah tanggal dan angka HK tidak sama")
    for tanggal in tanggal_hk:
        try:
            datetime.datetime.strptime(tanggal, "%A, %d %B %Y")
        except ValueError:
            raise ValueError("Format tanggal salah: " + tanggal)
    for angka in angka_hk:
        if not isinstance(angka, int):
            try:
                angka = int(angka)
            except ValueError:
                raise ValueError("Format angka HK salah: " + str(angka))
    return True


validate_input(tanggal_hk, angka_hk)


# Unit test untuk model
def test_model(model, numerical_dates, angka_hk):
    predictions = model.predict(numerical_dates)
    mae = mean_absolute_error(angka_hk, predictions)
    rmse = np.sqrt(mean_squared_error(angka_hk, predictions))
    print(f"MAE: {mae:.2f}")
    print(f"RMSE: {rmse:.2f}")


test_model(model, numerical_dates, angka_hk)


# Fitur untuk menampilkan plot
def plot_prediction(tanggal_hk, angka_hk, prediction):
    numerical_dates = np.arange(len(tanggal_hk)).reshape(-1, 1)
    next_numerical_date = len(tanggal_hk)
    fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
    ax.plot(numerical_dates, angka_hk, label="Angka HK")
    ax.plot([next_numerical_date], [int(prediction)], "ro", label="Prediksi")
    ax.axhline(y=np.mean(angka_hk), color="gray", linestyle="--", label="Rata-rata")
    ax.axvline(
        x=next_numerical_date, color="gray", linestyle="--", label="Tanggal Prediksi"
    )
    ax.set_xlabel("Tanggal")
    ax.set_ylabel("Angka HK")
    ax.set_title("Prediksi Angka HK")
    ax.grid(True)
    ax.legend()
    plt.savefig("plot.png")
    plt.show()


plot_prediction(tanggal_hk, angka_hk, prediction)

# Simpan model ke dalam file
joblib.dump(model, "model.joblib")

# Output:
# Senin, 12 Juni 2023     3227
# MAE: 1162.72
# RMSE: 1308.59
