from django.shortcuts import render
from tethys_sdk.permissions import login_required

from bokeh.embed import server_document

@login_required()
def home(request, page='summary'):
    """
    Controller for the app home page.
    """
    script = server_document(request.get_full_path())

    context = {
        'page': page,
        'script': script,
    }

    return render(request, 'covid/home.html', context)
