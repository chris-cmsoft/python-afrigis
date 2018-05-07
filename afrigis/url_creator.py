# -*- coding: utf-8 -*-

"""
URL Creator for Afrigis Services

Afrigis uses a HMAC method to authenticate request to ensure the correct
service is calling their API.

This method is described below:

You url is formatted as follows:

    https:// < Afrigis service base uri > / < service name > /
        < your saas key > / < hmac authentication code >

    < Afrigis service base uri >: The URL where we will call Afrigis services.
        This URL is changeable to cater for organizations whom use proxies and
        restrict internet access to their servers. We therefor allow the
        base service url.

    < service name >: The target service at afrigis.

    < your saas key >: SAAS key retrieved from Afrigis. This is the SAAS
        account where credits can be loaded for Afrigis services.

    < hmac authentication code >: HMAC authentication code generated by
        authentication.get_auth_code_digest()

The URL Creator takes care of creating and formatting this URL for you.

It will also take care of encoding parameters to keep them consistent
through the web service call.

"""

from .authentication import get_auth_code_digest


def create_full_url(
        afrigis_key,
        afrigis_secret,
        afrigis_base_uri,
        service_name,
        query_parameters=None,
):
    """
    Create URL in Afrigis authentication format with auth code
    """

    if not query_parameters:
        query_parameters = {}

    return '{}{}/{}/{}'.format(
        afrigis_base_uri,
        service_name,
        afrigis_key,
        get_auth_code_digest(
            afrigis_key=afrigis_key,
            afrigis_secret=afrigis_secret,
            service_name=service_name,
            query_params=query_parameters,
        )
    )