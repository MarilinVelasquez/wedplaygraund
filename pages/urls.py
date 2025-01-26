from django.urls import path
from . import views
from.views import PagesListView, PagesDetailView

urlpatterns = [
    path('', PagesListView.as_view(), name='pages'),
    path('<int:page_id>/<slug:slug>/', PagesDetailView.as_view(), name='page'),
]