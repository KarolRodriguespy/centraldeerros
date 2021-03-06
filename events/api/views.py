# Create your views here.

from django.shortcuts import redirect, render
from django.views import generic
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from events.forms import EventModelForm
from events.models import Event


def index(request):
    return render(request, 'registration/login.html')

@permission_classes([IsAuthenticated])
def create_event(request):
    if request.method == 'POST':
        form = EventModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('events:list')
    else:
        form = EventModelForm()

    context = {
        'form': form
    }

    return render(request, 'events/create.html', context=context)


@permission_classes([IsAuthenticated])
def delete_event(request, event_id):
    """
        Deleted a log

    """
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('events:list')


@permission_classes([IsAuthenticated])
def update_event(request, event_id):
    """
        updated a event using a event_id

    :param request: PUT
    :param event_id: int
    :return: data
    """
    event = Event.objects.get(pk=event_id)

    if request.method == 'POST':
        form = EventModelForm(data=request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('events:list')
    else:
        form = EventModelForm(instance=event)

    context = {
        'form': form,
        'event_id': event_id
    }

    return render(request, 'events/update.html', context=context)


@permission_classes([IsAuthenticated])
def detail_event(request, event_id):
    """
    details a log using an event_id

    :param request: GET
    :param event_id: int
    :return: data
    """

    event = Event.objects.get(pk=event_id)

    return render(request, 'events/detail.html', context={'event': event})


class EventApiListView(generic.ListView):
    """
    list of the events

    """
    permission_classes = [IsAuthenticated]

    model = Event
    context_object_name = 'list'
    queryset = Event.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['log', 'level']
    ordering_fields = ['level']
    template_name = 'events/list.html'
