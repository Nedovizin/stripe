import django.conf
import stripe as st
from django.http import Http404, JsonResponse
from django.shortcuts import render
from django.conf import settings
from api.models import Item

st.api_key = settings.STRIPE_SECRET_KEY


def buy(request, buy_id):
    try:
        item = Item.objects.get(pk=buy_id)
    except Item.DoesNotExist:
        raise Http404("Question does not exist")

    session = st.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'rub',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=f"{request.scheme}://{request.get_host()}/stub",
        cancel_url=f"{request.scheme}://{request.get_host()}/stub",
    )
    return JsonResponse({'id': session.id})


def item(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'api/item.html', {'item': item, 'id': item_id})


def stub(request):
    return render(request, 'api/index.html')
