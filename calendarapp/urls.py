from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('duty_day_group/<int:day>/<int:group_id>/', duty_view, name='duty_day_group'),
    path('all_duties_day/<int:day>/', all_duties_view, name='all_duties_day'),
    path('calendar_table', calendar_table_view, name='calendar_table'),
]