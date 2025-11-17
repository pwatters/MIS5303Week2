import random
import string
import requests

BASE_URL = "http://127.0.0.1:5000"

def random_string(length=10):
    return ''.join(random.choice(string.printable) for _ in range(length))

def fuzz_add_endpoint(iterations=50):
    for i in range(iterations):
        name = random_string(random.randint(1, 30))
        try:
            resp = requests.get(f"{BASE_URL}/add", params={"name": name})
            print(f"[{i}] Sent name={name!r}, got status {resp.status_code}")
        except Exception as e:
            print(f"[{i}] Error with input {name!r}: {e}")

def fuzz_show_endpoint(iterations=10):
    for i in range(iterations):
        try:
            resp = requests.get(f"{BASE_URL}/show")
            print(f"[{i}] /show returned {len(resp.text)} chars")
        except Exception as e:
            print(f"[{i}] Error calling /show: {e}")

if __name__ == "__main__":
    fuzz_add_endpoint()
    fuzz_show_endpoint()

