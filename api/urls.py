from django.urls import path

from . import views

urlpatterns = [
    path('buy/<int:buy_id>', views.buy, name='buy'),
    path('item/<int:item_id>', views.item, name='item'),
    path('stub', views.stub),
]
