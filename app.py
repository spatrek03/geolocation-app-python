from flask import Flask, request
import requests

app = Flask(__name__)

def get_location_from_ip(ip):
    url = f"http://api.ipapi.com/{ip}?access_key=ba956c7f3a1b45db7723db76783438ef"
    response = requests.get(url)
    data = response.json()
    location = f"{data['city']}, {data['region_name']}, {data['country_name']}"
    return location

@app.route('/')
def get_location():
    ip = request.remote_addr
    location = get_location_from_ip(ip)
    return f'A felhasználó helyzete: {location}'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
