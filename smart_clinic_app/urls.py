from django.urls import path
from . import views


urlpatterns = [
    path('', views.Resigter_Doctor, name='SignUpAsDoctor'),
    path('login', views.login_Doctor, name='loginDoctor'),
    path('about', views.about),
    path('appointment', views.appointment),
    path('blog', views.blog),
    path('contact', views.contact),
    path('detail', views.detail),
    path('index', views.index, name='index'),
    path('service', views.service),
    path('testimonial', views.testimonial),
    path('treatment', views.treatment),
    path('whatare', views.whatare),
    path('whatis', views.whatis),
    path('camera/', views.camera_view, name='camera_view'),
    path('save_picture/', views.save_picture, name='save_picture'),
]
