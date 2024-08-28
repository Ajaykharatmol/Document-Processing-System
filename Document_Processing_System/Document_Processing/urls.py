from . import views
from django.contrib.auth import views as auth 
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from . import views
from . import views as user_view 
from django.contrib.auth import views as auth 
urlpatterns = [
    path('', views.index, name ='index'),
    path('register/', user_view.register, name ='register'),
    path('login/', user_view.Login, name ='login'), 
    path('logout/', auth.LogoutView.as_view(template_name ='index.html'), name ='logout'), 
    path('Document_Upload/', user_view.Document_Upload, name ='Document_Upload'),
    
   

]