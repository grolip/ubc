#!/usr/bin/env python3
from os.path import join as path_join
from subprocess import CompletedProcess

from .element_dbus import ElementDBus
from .interface_dbus import InterfaceDBus


class ObjectDBus(ElementDBus):
	def __init__(self, service_name: str, name: str):
		super().__init__(name)
		self.service_name = service_name

		if self.name == '.':
			self.name = ""
		self.name = self.join(self.service_name , self.name)

		if self.name.endswith('/'):
			self.name = self.name[:-1]

	def iface(self, name: str) -> InterfaceDBus:
		return InterfaceDBus(self.service_name, self.name, name)

	def introspect(self) -> CompletedProcess:
		com = ["introspect", "--list", self.service_name, self.name]
		return self.execute_busctl(com)
