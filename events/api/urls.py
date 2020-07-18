from django.urls import path

from .views import create_event, EventApiListView, delete_event, update_event, detail_event

app_name = 'events'

urlpatterns = [
    path('list', EventApiListView.as_view(), name='list'),
    path('create', create_event, name='create'),
    path('delete/<int:event_id>', delete_event, name='delete'),
    path('update/<int:event_id>', update_event, name='update'),
    path('detail/<int:event_id>', detail_event, name='detail')

]
