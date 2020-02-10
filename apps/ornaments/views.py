from django.shortcuts import render, get_object_or_404

import logging

from apps.ornaments.models import OrnamentDevice

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


def controller_nickname_view(request, nickname):
    ornament = get_object_or_404(OrnamentDevice, nickname=nickname)
    context = {
        'mac_address': ornament.mac_address,
        'nickname': nickname,
    }
    return render(
        request=request,
        template_name='controller.html',
        context=context,
    )
