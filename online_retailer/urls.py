
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from online_retailer.views import productList,productUpdateView,productDeleteView
urlpatterns = [
    path('', productList.as_view(),name="ho"),
    path('<pk>/update', productUpdateView.as_view(),name="Product_update"),
    path('<pk>/delete/', productDeleteView.as_view(),name="Product_delete"),
] + static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)