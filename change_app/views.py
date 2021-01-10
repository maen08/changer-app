from django.shortcuts import render
from .models import Amount
from forms import TotalAmountForm, MultiplierForm
from django.contrib.auth.models import  User


def request_change(request):
    multiplier = request.POST.get('multiplier')
    obj = Amount()
    obj.multiplier = multiplier
    obj.save()

    # Amount(multiplier=multiplier)

    print(multiplier)
    total = request.POST.get('total')
    obj.total_amount = total
    obj.save()


    multiplier = MultiplierForm()
    total_amount = TotalAmountForm()

    whole_amount = Amount.objects.all()
    args = {
        'whole_amount': whole_amount,
        'multiplier': multiplier,
        'total': total,
    }
    return render(request, template_name='index.html', context=args)


def history_view(request):
    user = User.objects.get(username=request.user)
    details = Amount.objects.all()
  
    args = {
       'details':details,
        'user': user,

    }

    return render(request, template_name='change_hist.html', context=args)


def change_provider_view(request):


    
    return render(request, template_name='provider.html')