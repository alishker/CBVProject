from django.urls import path

from CBVApp.views import SchoolListView, SchoolDetailView, IndexView

app_name = 'CBVApp'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('list/', SchoolListView.as_view(), name='list'),
    path('CBVApp/details/(?P<pk>[0-9]+)/$',
         SchoolDetailView.as_view(), name='detail'),

]
