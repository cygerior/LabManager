def date(request):
    return render(request, 'ConfManager/date.html', {'date': datetime.now()})