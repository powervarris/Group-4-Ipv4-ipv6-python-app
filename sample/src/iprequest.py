import requests
from flask import Flask, render_template, request

app = Flask(__name__)

def get_ip_info(ip, api_key):
    url = f'http://api.ipstack.com/{ip}?access_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_current_ip():
    ipv4_response = requests.get('https://api.ipify.org?format=json')
    ipv6_response = requests.get('https://api64.ipify.org?format=json')

    ipv4 = None
    ipv6 = None

    if ipv4_response.status_code == 200:
        ipv4_data = ipv4_response.json()
        print("IPv4 Response JSON:", ipv4_data)
        ipv4 = ipv4_data.get('ip')
    else:
        print("Failed to retrieve IPv4 address.")

    if ipv6_response.status_code == 200:
        ipv6_data = ipv6_response.json()
        print("IPv6 Response JSON:", ipv6_data)
        ipv6 = ipv6_data.get('ip')
    else:
        print("Failed to retrieve IPv6 address.")

    # Outputting both addresses
    print(f"IPv4 Address: {ipv4 if ipv4 else 'Not available'}")
    print(f"IPv6 Address: {ipv6 if ipv6 else 'Not available'}")

    return ipv4, ipv6

@app.route('/', methods=['GET', 'POST'])
def index():
    api_key = 'd7deef0eeb5540a2c60b2bcf04e4fdb1'
    api_key = 'c6076bd31b09ddc1ea539dc9c1f6d1e4'
    ipv4, ipv6 = get_current_ip()
    ipv4_info = {}
    ipv6_info = {}
    if request.method == 'POST':
        ip = request.form['ip_address']
        if ':' in ip:
            ipv6 = ip
        else:
            ipv4 = ip
    if ipv4:
        ipv4_info = get_ip_info(ipv4, api_key)
    if ipv6:
        ipv6_info = get_ip_info(ipv6, api_key)
    if ipv4_info or ipv6_info:
        return render_template('index.html', ipv4_info=ipv4_info, ipv6_info=ipv6_info)
    else:
        return "Failed to retrieve IP information", 500

if __name__ == "__main__":
    app.run(debug=True)