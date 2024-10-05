import requests
from django.shortcuts import render
from django.http import JsonResponse
from .utils import clean_url


def index(request):
    header_nav = [
        {'name': 'Home', 'path': '/'},
        {'name': 'About', 'path': '/about/'},
        {'name': 'Blog', 'path': '/blog'},
    ]
    context = {
        'header_nav': header_nav,
    
    }
    return render(request, 'index.html', context)

    
def predict_category_api(request):
    if request.method == 'POST':
        url_input = request.POST.get('url')
        if url_input:
            cleaned_input = clean_url("url_input")  

            # Data to send to the external API
            data = {
                "url": cleaned_input
            }

            try:
                # Make the request to the external API
                external_api_url = 'https://phishing-urls-pred-api.onrender.com/predict'
                response = requests.post(external_api_url, json=data)

                # Check if the request was successful
                if response.status_code == 200:
                    result = response.json()

                    # Return the prediction and confidence score from the external API
                    return JsonResponse({
                        'prediction': result.get('prediction'),
                        'confidence_score': result.get('confidence_score')
                    })
                else:
                    return JsonResponse({'error': 'Failed to get a valid response from the external API'}, status=500)

            except requests.RequestException as e:
                return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=400)

def about(request):
    header_nav = [
        {'name': 'Home', 'path': '/'},
        {'name': 'About', 'path': '/about/'},
        {'name': 'Blog', 'path': '/'},
    ]
    return render(request, 'about.html', {'header_nav': header_nav})

def contact(request):
    header_nav = [
        {'name': 'Home', 'path': '/'},
        {'name': 'About', 'path': '/about/'},
        {'name': 'Blog', 'path': '/blog/'},
        {'name': 'Contact', 'path': '/contact/'},
    ]

    return render(request, 'contact.html',{'header_nav': header_nav} )

def blog(request):
    header_nav = [
        {'name': 'Home', 'path': '/'},
        {'name': 'About', 'path': '/about/'},
        {'name': 'Blog', 'path': '/'},
    ]
    return render(request, 'blog.html', {'header_nav': header_nav})