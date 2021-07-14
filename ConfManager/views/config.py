def view_config(request, id_config):
    if id_config > 100:
        raise Http404
    return HttpResponse("Vous avez demandé à voir la config #{}".format(id_config))
