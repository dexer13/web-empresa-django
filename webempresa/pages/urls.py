from django.urls import path
from . import views
app_name='pages'
urlpatterns = [
    path('page/<int:page_id>/', views.page, name='page'),
]