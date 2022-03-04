from django.contrib import messages
from django.shortcuts import render

from .forms import CustomerForm

# Create your views here.
def index(response):
    form = CustomerForm()
    if response.method == "POST":
        form = CustomerForm(response.POST)
        if form.is_valid:
            try:
                form.save()
                messages.success(response, 'A new customer has been added!')
            except:
                pass
    return render(response, 'myapp/index.html', {'form':form})