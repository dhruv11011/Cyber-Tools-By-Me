import sys
import requests
import re

def get_response(url):
    response = requests.get(url)
    return response.text

def crlf_check(response):
    crlf_regex = re.compile(r'(?<!\S)\r\n|\r\n(?!\S)')
    if crlf_regex.search(response):
        return True
    else:
        return False

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python crlf_scanner.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    response = get_response(url)
    if crlf_check(response):
        print(f"CRLF injection vulnerability found in {url}")
    else:
        print(f"CRLF injection vulnerability not found in {url}")