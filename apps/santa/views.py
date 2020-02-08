from django.shortcuts import render

import logging
logger = logging.getLogger(__name__)


def test_view(request):
    logger.info('Rendering the view!')
    return render(
        request=request,
        template_name='test.html',
        context={},
    )
