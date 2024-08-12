from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .utils import tokenize, load_model_and_vectorizer, predict_url_category

def index(request):
    return render(request, 'index.html')

def predict_category(request):
    if request.method == 'POST':
        user_input = request.POST.get('url_input')
        cleaned_url = clean_url(user_input)
        cleaned_input = [tokenize(cleaned_url)]

        model, vectorizer = load_model_and_vectorizer()
        try:
            prediction = predict_url_category(cleaned_input, model, vectorizer)
        except Exception as e:
            return HttpResponse("An error occurred: {}".format(e), status=500)
        return render(request, 'index.html', {'prediction': prediction})
    return render(request, 'index.html')
