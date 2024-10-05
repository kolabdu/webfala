from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('predict-category-api/', views.predict_category_api, name='predict_category_api'),
    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
    # path('blog/', views.blog, name='blog'),


    path('', views.index, name='index'),  
    path('about/', views.about, name='about'),  
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),  
    path('predict/', views.predict_category_api, name='predict_category_api'),  # API view for URL prediction


]
