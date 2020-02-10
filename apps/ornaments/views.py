from django.shortcuts import render

import logging
logger = logging.getLogger(__name__)


def device_view(request, mac_address):
    """Not a real device, just the test js view we're using"""
    logger.info('Device view')
    return render(
        request=request,
        template_name='device.html',
        context={'mac_address': mac_address},
    )


def controller_view(request, mac_address):
    logger.info('Controller view!')
    return render(
        request=request,
        template_name='controller.html',
        context={'mac_address': mac_address},
    )
