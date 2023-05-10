import pickle

from django.shortcuts import render
from django.views import generic

from .models import Owners, NotOwners, Ads, Indicators

from django.shortcuts import render, redirect


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_owners = Owners.objects.all().count()
    num_notowners = NotOwners.objects.all().count()
    num_ads = Ads.objects.all().count()
    num_indicators = Indicators.objects.all().count()
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_owners': num_owners, 'num_indicators': num_indicators,
                 'num_notowners': num_notowners, 'num_ads': num_ads},
    )
#
# def top_clients_array():
#     top_clients = []
#     help_top_clients = {}
#     for e in Ads.objects.all():
#         try:
#             help_top_clients[e.id_car] += 1
#         except:
#             help_top_clients[e.id_car] = 1
#     sorted_help_clients = dict(sorted(help_top_clients.items(), key=lambda item: item[1]))
#     for key, value in sorted_help_clients.items():
#         top_clients.append([key, value])
#     top_clients = top_clients[::-1]
#     if len(top_clients) > 10:
#         top_clients = top_clients[:10]
#     for e in Clients.objects.all():
#         for i in range(len(top_clients)):
#             if top_clients[i][0] == int(e.id):
#                 top_clients[i][0] = e.full_name
#     return top_clients
#
# def top_workers_array():
#     top_workers = []
#     help_top_workers = {}
#     for e in Ads.objects.all():
#         try:
#             help_top_workers[e.id_worker] += 1
#         except:
#             help_top_workers[e.id_worker] = 1
#     sorted_help_workers = dict(sorted(help_top_workers.items(), key=lambda item: item[1]))
#     for key, value in sorted_help_workers.items():
#         top_workers.append([key, value])
#     top_workers = top_workers[::-1]
#     if len(top_workers) > 10:
#         top_workers = top_workers[:10]
#     for e in NotOwner.objects.all():
#         for i in range(len(top_workers)):
#             if top_workers[i][0] == int(e.id):
#                 top_workers[i][0] = e.full_name
#     return top_workers
#
# def all_parts():
#     numbers_all = 0
#     cost_all_parts = 0
#     for e in Indicators.objects.all():
#         cost_all_parts += e.sum * e.average_cost
#         numbers_all += e.sum
#     average_cost_all = cost_all_parts / numbers_all
#     return [numbers_all, cost_all_parts, average_cost_all]
#
# def managedeck(request):
#     num_clients = Owner.objects.all().count()
#     num_workers = NotOwner.objects.all().count()
#     num_fixes = Ads.objects.all().count()
#     num_parts = Indicators.objects.all().count()
#     top_clients = top_clients_array()
#     top_workers = top_workers_array()
#     for_parts = all_parts()
#     numbers_all_parts = for_parts[0]
#     cost_all_parts = for_parts[1]
#     average_cost_all_parts = round(for_parts[2])
#     return render(
#         request,
#         'managedeck.html',
#         context={'num_clients': num_clients, 'num_workers': num_workers,
#                  'num_fixes': num_fixes, 'num_parts': num_parts,
#                  'top_clients': top_clients, 'top_workers': top_workers,
#                  'numbers_all_parts': numbers_all_parts, 'cost_all_parts': cost_all_parts, 'average_cost_all_parts': average_cost_all_parts},
#     )

class OwnerListView(generic.ListView):
    model = Owners


class NotownerListView(generic.ListView):
    model = NotOwners

class AdsListView(generic.ListView):
    model = Ads
#
# def fixesview(request):
#     fixes_list = []
#     type = {
#         'BL': 'Backlog',
#         'TD': 'To do',
#         'IP': 'In progress',
#         'DE': 'Done'
#     }
#     clients = {}
#     workers = {}
#     parts = {}
#     for e in Clients.objects.all():
#         clients[e.id] = e.full_name
#     for e in Workers.objects.all():
#         workers[e.id] = e.full_name
#     for e in Parts.objects.all():
#         parts[e.id] = e.name
#     for e in Fixes.objects.all():
#         fixes_list.append([e.id, type[e.type_active], clients[e.id_car], workers[e.id_worker], parts[e.id_parts], e.repair_cost, e.comment])
#
#     return render(
#         request,
#         'fixes_list.html',
#         context={'fixes_list': fixes_list},
#     )
#


class IndicatorsListView(generic.ListView):
    model = Indicators



from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class IndicatorsCreate(CreateView):
    model = Indicators
    fields = '__all__'
    success_url = reverse_lazy('indicators')

class IndicatorUpdate(UpdateView):
    model = Indicators
    fields = ['id_owner', 'gas', 'water', 'electric']
    success_url = reverse_lazy('indicators')

class IndicatorsDelete(DeleteView):
    model = Indicators
    success_url = reverse_lazy('indicators')

class OwnerCreate(CreateView):
    model = Owners
    fields = '__all__'
    success_url = reverse_lazy('owners')

class OwnerUpdate(UpdateView):
    model = Owners
    fields = ['full_name', 'mail', 'phone', 'land_adress', 'home_adress']
    success_url = reverse_lazy('owners')

class OwnerDelete(DeleteView):
    model = Owners
    success_url = reverse_lazy('owners')

class AdsCreate(CreateView):
    model = Ads
    fields = '__all__'
    success_url = reverse_lazy('ads')

class AdsUpdate(UpdateView):
    model = Ads
    fields = ['type_ads', 'title', 'content', 'date_posted', 'author']
    success_url = reverse_lazy('ads')

class AdsDelete(DeleteView):
    model = Ads
    success_url = reverse_lazy('ads')


class NotownerCreate(CreateView):
    model = NotOwners
    fields = '__all__'
    success_url = reverse_lazy('notowner')

class NotownerUpdate(UpdateView):
    model = NotOwners
    fields = ['full_name', 'mail', 'phone', 'home_adress']
    success_url = reverse_lazy('notowner')

class NotownerDelete(DeleteView):
    model = NotOwners
    success_url = reverse_lazy('notowner')


