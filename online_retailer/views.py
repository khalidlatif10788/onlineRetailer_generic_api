
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import product,order,customer
from .Serializers import productSerializer

@method_decorator(login_required, name="dispatch")
class productList(ListView):

    model = product
    #paginate_by=3
    
@method_decorator(login_required, name="dispatch")
class productUpdateView(UpdateView):
    model = product
    fields = [
        "pname",
        "pdescription",
        "psalep",
        "photo"
    ]

    success_url ="/"
    
@method_decorator(login_required, name="dispatch")
class productDeleteView(DeleteView):
    model = product
    success_url ="/"


# Api code



from rest_framework import viewsets

class productModelviewset(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class = productSerializer