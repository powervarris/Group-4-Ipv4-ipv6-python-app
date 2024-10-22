import requests
from flask import Flask, render_template, request

# Create a Flask application instance
app = Flask(__name__)

def get_ip_info(ip, api_key):
    """
    Retrieves detailed information about the provided IP address using the ipstack API.

    Parameters:
    - ip (str): The IP address to look up.
    - api_key (str): The API key for ipstack.

    Returns:
    - dict: Parsed JSON response containing IP information if the request is successful; None otherwise.
    """
    url = f'http://api.ipstack.com/{ip}?access_key={api_key}'
    response = requests.get(url)  # Make the API request
    if response.status_code == 200:
        return response.json()  # Return parsed JSON data
    else:
        return None  # Return None if the API request failed

def get_current_ip():
    """
    Fetches the current public IPv4 and IPv6 addresses using ipify API.

    Returns:
    - tuple: A tuple containing the IPv4 and IPv6 addresses.
    """
    ipv4_response = requests.get('https://api.ipify.org?format=json')
    ipv6_response = requests.get('https://api64.ipify.org?format=json')

    ipv4 = None
    ipv6 = None

    # Check if IPv4 address retrieval was successful
    if ipv4_response.status_code == 200:
        ipv4_data = ipv4_response.json()
        print("IPv4 Response JSON:", ipv4_data)  # Log the JSON response for debugging
        ipv4 = ipv4_data.get('ip')  # Extract the IP address
    else:
        print("Failed to retrieve IPv4 address.")

    # Check if IPv6 address retrieval was successful
    if ipv6_response.status_code == 200:
        ipv6_data = ipv6_response.json()
        print("IPv6 Response JSON:", ipv6_data)  # Log the JSON response for debugging
        ipv6 = ipv6_data.get('ip')  # Extract the IP address
    else:
        print("Failed to retrieve IPv6 address.")

    # Output both addresses
    print(f"IPv4 Address: {ipv4 if ipv4 else 'Not available'}")
    print(f"IPv6 Address: {ipv6 if ipv6 else 'Not available'}")

    return ipv4, ipv6  # Return both addresses

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Handles the main application route. Processes GET and POST requests
    for IP address lookup and returns the rendered HTML page with IP info.

    Returns:
    - str: Rendered HTML page with IPv4 and IPv6 information or an error message.
    """
    api_key = 'd7deef0eeb5540a2c60b2bcf04e4fdb1'  # API key for ipstack
    ipv4, ipv6 = get_current_ip()  # Get current IP addresses
    ipv4_info = {}  # Initialize IPv4 information dictionary
    ipv6_info = {}  # Initialize IPv6 information dictionary

    # Handle form submission
    if request.method == 'POST':
        ip = request.form['ip_address']  # Get the IP address from the form
        if ':' in ip:
            ipv6 = ip  # If the input is IPv6
        else:
            ipv4 = ip  # Otherwise, it's IPv4

    # Fetch information for the provided IP addresses
    if ipv4:
        ipv4_info = get_ip_info(ipv4, api_key)
    if ipv6:
        ipv6_info = get_ip_info(ipv6, api_key)

    # Render the HTML template with the IP information
    if ipv4_info or ipv6_info:
        return render_template('index.html', ipv4_info=ipv4_info, ipv6_info=ipv6_info)
    else:
        return "Failed to retrieve IP information", 500  # Return an error if no data is found

if __name__ == "__main__":
    app.run(debug=True)  # Start the Flask application in debug mode
