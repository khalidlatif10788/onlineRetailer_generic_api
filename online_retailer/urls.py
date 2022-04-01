
from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from online_retailer import views
from django.urls import path,include
from online_retailer.views import productList,productUpdateView,productDeleteView

# create object  Default Router class
router=DefaultRouter()
# register class 
router.register('track',views.productModelviewset,basename='Product')
urlpatterns = [
    path('', productList.as_view(),name="ho"),
     path('<pk>/update', productUpdateView.as_view(),name="Product_update"),
    path('<pk>/delete/', productDeleteView.as_view(),name="Product_delete"),
    # ModelViewSet Api
     path('apimodelViewSet/',include(router.urls), name="apimodelviewSet"),
  
]+ static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
