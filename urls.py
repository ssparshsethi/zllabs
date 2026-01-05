from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ardapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # main pages
    path('', views.account, name="account"),
    path('home/', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('view/', views.view, name="view"),
    path('project/', views.project, name="project"),
    path('add/', views.add, name="add"),
    path('review/', views.review, name="review"),
    path('shop/', views.shop, name="shop"),
    path('account/', views.account, name="account"), 

     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
