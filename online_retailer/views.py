
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


from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin


class prodcutList(GenericAPIView,ListModelMixin):
    queryset = product.objects.all()
    serializer_class = productSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class prodcutCreate(GenericAPIView,CreateModelMixin):
    queryset = product.objects.all()
    serializer_class = productSerializer

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class productRetrieve(GenericAPIView,RetrieveModelMixin):
    queryset = product.objects.all()
    serializer_class = productSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)


class productUpdate(GenericAPIView,UpdateModelMixin ):
    queryset = product.objects.all()
    serializer_class = productSerializer

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
class productDestroy(GenericAPIView,DestroyModelMixin ):
    queryset = product.objects.all()
    serializer_class = productSerializer

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)