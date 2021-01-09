from django.shortcuts import render
from .models import Amount



def request_change(request):
    whole_amount = Amount.objects.all()
    args = {
        'whole_amount':whole_amount,
    }
    return render(request, template_name='index.html', context=args)
