from django.shortcuts import render
from django.http import HttpResponse
from .forms import MyForm
from .utils import clean_url, load_model_and_vectorizer, predict_url_category



def index(request):
    header_nav = [
        {'name': 'Home', 'path': '/'},
        {'name': 'About ', 'path': '/about/'},
        {'name': 'Blog', 'path': '/blog/'},
    
    ]
    context = {
        'form': MyForm(),
        'header_nav': header_nav,
    }
    return render(request, 'index.html', context)

def predict_category(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # user_input = form.cleaned_data['url_input']
            cleaned_input = [clean_url('form')]

            try:
                model, vectorizer = load_model_and_vectorizer()
                prediction = predict_url_category(cleaned_input, model, vectorizer)
                return render(request, 'index.html', {'form': form, 'prediction': prediction})
            except ValueError as e:
                return HttpResponse(f"ValueError: {e}", status=500)
            except Exception as e:
                return HttpResponse(f"An error occurred: {e}", status=500)
    
    form = MyForm()
    return render(request, 'index.html', {'form': form})

# def predict_category(request):
#     if request.method == 'POST':
#         form = MyForm(request.POST)
#         # cleaned_input = [tokenize(user_input)]
#         cleaned_input = [clean_url('form')]

#         model, vectorizer = load_model_and_vectorizer()
#         try:
#             form = predict_url_category(cleaned_input, model, vectorizer)
#         except Exception as e:
#             return HttpResponse("An error occurred: {}".format(e), status=500)
#         return render(request, 'index.html', {'form': form})
#     return render(request, 'index.html')


def about(request):
    header_nav = [
        {'name': 'Home', 'path': '/'},
        {'name': 'About ', 'path': '/about/'},
        {'name': 'Blog', 'path': '/blog/'},
        
    ]
    return render(request, 'about.html', {'header_nav': header_nav})


def contact(request):
    return render(request, 'contact.html')

def blog(request):
    header_nav = [
        {'name': 'Home', 'path': '/'},
        {'name': 'About ', 'path': '/about/'},
        {'name': 'Blog', 'path': '/blog/'},
    
    ]
    return render(request, 'blog.html', {'header_nav': header_nav})

