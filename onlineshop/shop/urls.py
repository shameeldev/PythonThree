from django.urls import path
from . import views
app_name = 'shop'

urlpatterns = [
    path('', views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/', views.allProdCat,name='prodByCat'),
    path('<slug:c_slug>/<slug:p_slug>/', views.prodDetail,name='prodCatDetail'),
]
