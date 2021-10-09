from django.shortcuts import get_object_or_404, render

from ConfManager.models import TestPlatform


def view_config(request, pk):
    config = get_object_or_404(TestPlatform, pk=pk)

    return render(
        request,
        'ConfManager/config.html',
        {
            'config': config,
            'has_permission': True
        }
    )