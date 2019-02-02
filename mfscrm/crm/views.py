# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from .models import *
from .forms import *

now = timezone.now()
def home(request):
   return render(request, 'crm/home.html',
                 {'crm': home})

@login_required


def customer_list(request):
    customer = Customer.objects.filter(created_date__lte=timezone.now())
    return render(request, 'crm/customer_list.html',
                 {'customers': customer})

@login_required
def customer_edit(request, pk):
 customer = get_object_or_404(Customer, pk=pk)
 if request.method == "POST":
       # update
       form = CustomerForm(request.POST, instance=customer)
       if form.is_valid():
           customer = form.save(commit=False)
           customer.updated_date = timezone.now()
           customer.save()
           customer = Customer.objects.filter(created_date__lte=timezone.now())
           return render(request, 'crm/customer_list.html',
                         {'customers': customer})
 else:
    # edit
    form = CustomerForm(instance=customer)
    return render(request, 'crm/customer_edit.html', {'form': form})
@login_required
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return redirect('crm:customer_list')
