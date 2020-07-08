from tethys_sdk.base import TethysAppBase, url_map_maker


class Covid(TethysAppBase):
    """
    Tethys app class for Covid.
    """

    name = 'COVID-19'
    index = 'covid:home'
    icon = 'covid/images/covid-logo.jpg'
    package = 'covid'
    root_url = 'covid'
    color = '#2c3e50'
    description = ''
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='covid',
                controller='covid.controllers.home',
                handler='covid.handlers.home_handler',
                handler_type='bokeh',
            ),
            UrlMap(
                name='page',
                url='covid/{page}',
                controller='covid.controllers.home',
                handler='covid.handlers.home_handler',
                handler_type='bokeh',
            ),
        )

        return url_maps
