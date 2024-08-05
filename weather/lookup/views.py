from django.shortcuts import render

# Create your views here.
def home(request):
    import os
    import requests

    zipcode: str = "89129"
    if request.method == "POST":
        zipcode = request.POST["zipcode"]

    error_message: str = ""
    response: dict = {}
    API_KEY = os.environ.get("API_KEY")
    category: str = "unknown"
    try:
        response = requests.get(
            f"https://www.airnowapi.org/aq/observation/zipCode/current/"
            f"?format=application/json&zipCode={zipcode}&distance=5&API_KEY={API_KEY}"
        ).json()
        
        if response and response[0]:
            category = {
                "Good": "good",
                "Moderate": "moderate",
                "Unhealthy for Sensitive Groups": "usg",
                "Unhealthy": "unhealthy",
                "Very Unhealthy": "veryunhealthy",
                "Hazardous": "hazardous",
            }.get(response[0]["Category"]["Name"], "unknown")
    except Exception as e:
        error_message = "Error: " + str(e)
    return render(
        request, 'home.html',
        {
            "error": error_message,
            "weather_response": response,
            "category": category,
        }
    )

def about(request):
   return render(request, 'about.html', {}) 
