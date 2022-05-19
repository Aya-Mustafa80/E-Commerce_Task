from nturl2path import url2pathname
from django.urls import path


from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('shop/',views.shop,name='shop'),
    path('shopre/<int:catid>/',views.shopre,name='shopre'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('prodDetail/<int:prodid>/',views.prodDetail,name='prodDetail'),
    path('cart/<int:pID>/',views.cart,name='cart'),
    path('shopCart/',views.shopCart,name='shopCart'),
    path('Cartdel/<int:CID>/',views.Cartdel,name='Cartdel'),
]
 
