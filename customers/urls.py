
from django.urls import path
from .views import render_pdf_view, CustomerListView, customer_render_pdf_view

app_name = 'customers'

urlpatterns = [
    path('', render_pdf_view, name='test'),
    path('pdf/', CustomerListView.as_view(), name='customer-pdf'),
    path('pdf/<int:pk>', customer_render_pdf_view  , name='customer-pdf-view'),
]
