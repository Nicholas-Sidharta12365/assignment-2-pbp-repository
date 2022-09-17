from django.urls import path, include
from . import views
# TODO: Implement Routings Here

urlpatterns= {
   path('html/', views.mywatchlist, name="mywatchlist"),
   path('xml/', views.mywatchlist_xml, name="mywatchlist_xml"),
   path('json/', views.mywatchlist_json, name="mywatchlist_json"),
}