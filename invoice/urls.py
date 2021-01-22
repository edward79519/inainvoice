from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='Index'),
    path('add/', views.invoice_add, name='AddInvoice'),
    path('<int:invoice_id>/', views.invoice_detail, name='InvoiceDetail'),
    path('<int:invoice_id>/update/', views.invoice_update, name='InvoiceUpdate'),
    path('<int:invoice_id>/delete/', views.invoice_delete, name='InvoiceDelete'),
    path('<int:invoice_id>/<int:item_id>/delete/', views.invoiveitem_delete, name='ItemDelete'),
]