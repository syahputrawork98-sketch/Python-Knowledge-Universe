"""
LAB PRACTICAL: Mocking External API
Standard: PPM V4 - Gold Standard

Tujuan: Mengisolasi unit test dari dependensi pihak ketiga.
Guna: Mendebug alur logika aplikasi tanpa membutuhkan koneksi internet nyata.
"""

import unittest
from unittest.mock import patch

# 1. THE SYSTEM UNDER TEST (SUT)
# Fungsi yang bergantung pada data dari API luar
def get_weather_report(city):
    # Bayangkan ini memanggil 'requests.get("https://api.weather.com/...")'
    # Di laboratorium ini, kita hanya mensimulasikan pemanggilannya.
    return f"Weather in {city} is sunny."

def process_city_weather(city):
    report = get_weather_report(city)
    if "sunny" in report:
        return f"☀️ Recommendation: Wear sunglasses in {city}!"
    return "☁️ Recommendation: Stay indoors."

# 2. THE TEST CLASS
class TestWeatherLogic(unittest.TestCase):
    
    # Menerapkan Mock pada fungsi get_weather_report
    # Kita menggunakan jalur absolut ke fungsi di dalam modul ini (__main__)
    @patch("__main__.get_weather_report")
    def test_process_sunny_weather(self, mock_get_weather):
        print("\n[TEST] Testing sunny weather recommendation...")
        
        # Skenario: Kita paksa fungsi tersebut mengembalikan nilai 'sunny'
        mock_get_weather.return_value = "Weather in Jakarta is sunny."
        
        result = process_city_weather("Jakarta")
        
        # Verifikasi logika
        self.assertIn("sunglasses", result)
        # Verifikasi interaksi: Apakah pemanggilan dilakukan dengan benar?
        mock_get_weather.assert_called_with("Jakarta")

    @patch("__main__.get_weather_report")
    def test_process_cloudy_weather(self, mock_get_weather):
        print("[TEST] Testing cloudy weather recommendation...")
        
        # Skenario: Kita paksa fungsi tersebut mengembalikan nilai 'cloudy'
        mock_get_weather.return_value = "Weather in Jakarta is cloudy."
        
        result = process_city_weather("Jakarta")
        
        self.assertIn("Stay indoors", result)

if __name__ == "__main__":
    print("=" * 60)
    print("🧪 API MOCKING LAB SUITE")
    print("=" * 60)
    unittest.main()
