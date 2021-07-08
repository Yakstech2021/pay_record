
from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('', views.home, name="home"),
    # path('payment/list', ),
    # path('payment/detail/<int:payment_id>', ),
    path('payment/create/', views.create_payment, name="create_payment"),
    path('payment/pdf/<int:pk>/', views.pdf_preview, name="pdf_preview"),
    path('payment/', views.pdf_preview, name="pdf_preview"),
]