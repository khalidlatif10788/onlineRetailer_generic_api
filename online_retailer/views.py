from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from .models import product
from django.views.generic.edit import UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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
