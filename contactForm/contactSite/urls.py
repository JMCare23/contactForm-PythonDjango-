
from django.urls import path, include
from . import views
from .views import contactListView

urlpatterns = [
   path('', views.index, name = 'index'),
   path('get-csrf-token/', views.get_csrf_token, name='get_csrf_token'),
   path('api/contacts/', contactListView.as_view(), name='contact-list')
]
