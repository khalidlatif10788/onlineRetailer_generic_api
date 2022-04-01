
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from online_retailer import views
from online_retailer.views import productList,productUpdateView,productDeleteView

urlpatterns = [
    path('', productList.as_view(),name="ho"),
     path('<pk>/update', productUpdateView.as_view(),name="Product_update"),
    path('<pk>/delete/', productDeleteView.as_view(),name="Product_delete"),
    # api product retrive url
    path('productList/',views.prodcutList.as_view(), name="productList" ),
    path('productReteriveSingle/<int:pk>',views.productRetrieve.as_view(), name="productSingle"),
    # api product update
     path('productUpdate/<int:pk>',views.productUpdateView.as_view(), name="productUpdate"),
     #
    path('productDelete/<int:pk>',views.productDestroy.as_view(), name="productDelete"),
    #
  
]+ static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
