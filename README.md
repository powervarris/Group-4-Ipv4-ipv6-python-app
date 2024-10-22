# IP Information App

## Description
This Flask-based web application allows users to look up and visualize information about public IPv4 and IPv6 addresses. It provides both automatic retrieval of the user's public IP and manual input for specific IP addresses.

## Features
- Automatic retrieval of the user's public IPv4 and IPv6 addresses.
- Manual IP address input for user lookups.
- Displays detailed information about the IP address.
- User-friendly interface with a web map visualization.

## Installation Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/powervarris/Group-4-Ipv4-ipv6-python-app.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd Group-4-Ipv4-ipv6-python-app
   ```
3. **Install the required packages:**
   ```bash
   pip install flask requests
   ```

## Usage Instructions
1. **API Key Setup:**
   - Replace `d7deef0eeb5540a2c60b2bcf04e4fdb1` in `iprequest.py` with your actual API key from ipstack.
   
2. **Run the application:**
   ```bash
   python iprequest.py
   ```

3. **Access the application:**
   - Open your browser and go to `http://127.0.0.1:5000/`.


## API Keys
- You will need an API key from [ipstack](https://ipstack.com/) to retrieve IP information. Ensure you replace the placeholder in the code with your actual API key.

## Contributing
1. **Fork the repository.**
2. **Create a new branch for your feature.**
3. **Submit a pull request with your changes.**

## License
This project is licensed under the MIT License.
