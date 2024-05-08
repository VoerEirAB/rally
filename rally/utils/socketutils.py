# Copyright 2024: VoerEir AB
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import socket

from rally.consts import SocketAF


def get_address_family(af_opt, has_ipv6):
    """
    Returns Address Family by resolving user and python config.

    :param af_opt: Address Family user option.
    :param has_ipv6: True, if python is compiled with IPv6.
    :returns: socket.AddressFamily enum.
    """
    # Default: Unspecified Address Family.
    address_family = socket.AF_UNSPEC

    # AF_INET for IPv4.
    if af_opt == SocketAF.IPV4:
        address_family = socket.AF_INET

    # Check for IPv6
    elif af_opt == SocketAF.IPV6:

        # Raise Error if python is not compiled with IPv6 Support.
        if not has_ipv6:
            raise ValueError(
                'Python venv for rally/xrally does not support IPv6.'
                ' Python might be compiled with `--disable-ipv6` flag.'
                ' Rebuild with IPv6 support or use another build.'
            )

        # AF_INET6 for IPv6.
        address_family = socket.AF_INET6

    return address_family
