# -*- coding: utf-8 -*-
#
# vim: set ts=4 sw=4 sts=4 et :

import qubesadmin


def pci_devs():
    """
    Useful PCI devices lists.
    """

    app = qubesadmin.Qubes()

    def find_devices_of_class(klass):
        for dev in app.domains["dom0"].devices["pci"]:
            if repr(dev.interfaces[0]).startswith("p" + klass):
                yield dev.port_id

    grains = {
        'pci_net_devs': list(find_devices_of_class("02")),
        'pci_usb_devs': list(find_devices_of_class("0c03")),
        'pci_audio_devs': list(find_devices_of_class("0403")),
    }

    return grains
