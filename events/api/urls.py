from django.urls import path

from . import views

app_name = 'events'

urlpatterns = [
    path('list', views.EventApiListView.as_view(), name='list'),
    path('create', views.create_event, name='create'),
    path('delete/<int:event_id>', views.delete_event, name='delete'),
    path('update/<int:event_id>', views.update_event, name='update'),
    path('detail/<int:event_id>', views.detail_event, name='detail')

]
