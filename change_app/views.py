from django.shortcuts import render
from .models import Amount
from forms import TotalAmountForm, MultiplierForm


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

    # if request.method == 'POST':
    #     multiplier = MultiplierForm(request.POST)
    #     if multiplier.is_valid():
    #         multiplier.save()

    #     total_amount = TotalAmountForm(request.POST)
    #     # print(total_amount.values)
    #     if total_amount.is_valid():
    #         total_amount.save()

    multiplier = MultiplierForm()
    total_amount = TotalAmountForm()

    whole_amount = Amount.objects.all()
    args = {
        'whole_amount': whole_amount,
        'multiplier': multiplier,
        'total': total,
    }
    return render(request, template_name='index.html', context=args)
