from django.shortcuts import render
import requests

def home(request):
    weather = None
    city = request.GET.get('city', None)
    
    if city:
        api_key = '15643983db3e48558ae165542242607'  # Your WeatherAPI key
        url = f'http://api.weatherapi.com/v1/current.json?q={city}&key={api_key}'
        
        try:
            response = requests.get(url)
            data = response.json()
            #print("API Response Data:", data)  # Print for debugging

            if response.status_code == 200 and 'current' in data:
                weather = {
                    'city': data.get('location', {}).get('name'),
                    'temperature': data.get('current', {}).get('temp_c'),
                    'description': data.get('current', {}).get('condition', {}).get('text'),
                    'humidity': data.get('current', {}).get('humidity'),
                    'wind_speed': data.get('current', {}).get('wind_kph')
                }
            else:
                print("API Error Code:", data.get('error', {}).get('code'))
                print("Error Message:", data.get('error', {}).get('message', 'Unknown error'))
                weather = None
        except requests.exceptions.RequestException as e:
            print(f"RequestException: {e}")
            weather = None

    return render(request, 'home.html', {'weather': weather})
