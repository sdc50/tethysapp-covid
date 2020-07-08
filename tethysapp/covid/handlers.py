from bokeh.document import Document

from covid_dashboard.covid_dashboard import CovidDashboard, CovidSummary, CovidMapper, CovidPlotter
from tethys_sdk.base import with_request

PAGES = {
    'summary': CovidSummary(),
    'map': CovidMapper(),
    'plots': CovidPlotter(),
}


@with_request
def home_handler(doc: Document) -> None:
    try:
        page = doc.request.url_route['kwargs'].get('page', 'summary')
        cd = PAGES[page].panel()
        cd.server_doc(doc)
    except Exception as e:
        print(e)
