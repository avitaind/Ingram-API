from django.urls import path

from . import views


app_name = 'product'

urlpatterns = [
    # ex: api/product/<str:token>/
    path('<str:token>/', views.ListProductView.as_view(), name='List Product'),
    # ex: api/product/<str:token>/detail/
    path('<str:token>/detail/', views.ProductDetailView.as_view(), name='Product Detail'),
    # ex: api/product/<str:token>/validate/
    path('<str:token>/validate/', views.ValidateSerialNoView.as_view(), name='Validate Product'),
    # ex: api/product/<str:token>/block/
    path('<str:token>/block/', views.BlockProductView.as_view(), name='Block Product'),
    # ex: api/product/<str:token>/unblock/
    path('<str:token>/unblock/', views.UnblockProductView.as_view(), name='Unblock Product'),
]
