from django.urls import path
from .views import HomeView, PostDetailView
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='posts'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
    path('search/', views.search, name='search'),
    path('about-us/', views.aboutus, name='aboutus'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


