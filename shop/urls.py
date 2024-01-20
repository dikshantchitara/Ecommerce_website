
from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home,name="ShopHome"),
    path('about/',views.aboutus,name="AboutUs"),
    path('contact/',views.contact,name="ContactUs"),
    path('tracker/',views.tracker,name="TrackingStatus"),
    path('products/<int:myid>',views.productview,name="Search"),
    path('search/',views.search,name="Search"),
    path('checkout/',views.checkout,name="checkout"),
    
]
