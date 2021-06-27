from .utils import *
from django.shortcuts import render, redirect


def index(request):
    if request.GET:
        if request.GET['group_id']:
            return redirect('duty_day_group', request.GET['day'], request.GET['group_id'])
        return redirect('all_duties_day', request.GET['day'])

    return render(request, 'index.html', {})


def duty_view(request, day, group_id):
    context = {}

    data = open_json_file('media/duty.json')

    is_find = False

    for group in data:
        if group_id == group['groupId']:
            for user in group['usersDutyList']:
                for dutyDay in user['dutyDays']:
                    if dutyDay['isDuty'] == 'true' and dutyDay['day'] == str(day):
                        context['userName'] = user['userName']
                        context['userEmail'] = user['userEmail']
                        context['userPhone'] = user['userPhone']
                        context['groupName'] = group['groupName']
                        is_find = True
                        break
                        pass
                    pass
                if is_find:
                    break
            pass
        if is_find:
            break
        pass

    return render(request, 'duty_day_group.html', context)


def all_duties_view(request, day):
    context = {}

    data = open_json_file('media/duty.json')

    users = []
    for group in data:
        for user in group['usersDutyList']:
            for dutyDay in user['dutyDays']:
                if dutyDay['isDuty'] == 'true' and dutyDay['day'] == str(day):
                    users.append({
                        'userName': user['userName'],
                        'userEmail': user['userEmail'],
                        'userPhone': user['userPhone'],
                        'userGroup': group['groupName']
                    })
    context['users'] = users

    return render(request, 'all_duties_day.html', context)


def calendar_table_view(request):
    context = {}

    data = open_json_file('media/duty.json')

    days = {str(day): [] for day in range(1, 31)}
    for group in data:
        for user in group['usersDutyList']:
            for dutyDay in user['dutyDays']:
                if dutyDay['isDuty'] == 'true':
                    days[dutyDay['day']].append({
                        'userName': user['userName'],
                        'userGroup': group['groupName']
                    })
    context['days'] = days
    return render(request, 'calendar_table.html', context)
