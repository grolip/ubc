# ubc

Interface pour l'outil busctl

## Objectif

Simplifier l'utilisation de l'outil [busctl](https://www.freedesktop.org/software/systemd/man/busctl.html) 
sur les fonctions: 

* list
* introspect
* tree
* get-property

## Installation

```bash
git clone https://github.com/grolip/ubc.git
pip3 install ubc
```

## Utilisation comme outil

```bash
ubc
ubc -s org.freedesktop.NetworkManager

ubc -s org.freedesktop.NetworkManager -o Devices/2
ubc -s org.freedesktop.NetworkManager -o Devices/2 -i Device

ubc -s org.freedesktop.NetworkManager -o Devices/2 -i Device Driver
ubc -s org.freedesktop.NetworkManager -o . -i . AllDevices
```

Au lieu de respectivement:

```bash
busctl list --list
busctl tree --list org.freedesktop.NetworkManager

busctl introspect org.freedesktop.NetworkManager /org/freedesktop/NetworkManager/Devices/2
busctl introspect org.freedesktop.NetworkManager /org/freedesktop/NetworkManager/Devices/2 org.freedesktop.NetworkManager.Device

busctl get-property org.freedesktop.NetworkManager /org/freedesktop/NetworkManager/Devices/2 org.freedesktop.NetworkManager.Device Driver
busctl get-property org.freedesktop.NetworkManager /org/freedesktop/NetworkManager org.freedesktop.NetworkManager AllDevices
```

## Utilisation comme module

```python
from ubc import *

ServiceDBus.list()

ser = ServiceDBus("org.freedesktop.NetworkManager")
obj = ser.obj("Devices/2")
obj.introspect()

iface = obj.iface("Device")
iface.get_property("Driver")
```

Toutes les méthodes calquées sur busctl (list, tree, introspect, get_property) retournent un objet 
[CompletedProcess](https://docs.python.org/3.6/library/subprocess.html#subprocess.CompletedProcess).
