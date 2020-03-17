#!/usr/bin/env python3
from os.path import join as path_join
from subprocess import CompletedProcess

from .element_dbus import ElementDBus


class InterfaceDBus(ElementDBus):
	def __init__(self, service_name: str, object_name: str, name: str):
		super().__init__(name)
		self.service_name = service_name
		self.object_name = object_name

		if self.name == '.':
			self.name = ""
		complete_name = self.join(self.service_name, self.name)
		self.name = complete_name[1:].replace('/', '.')

		if self.name.endswith('.'):
			self.name = self.name[:-1]

	def introspect(self) -> CompletedProcess:
		com = ["introspect", "--list",
			self.service_name, 
			self.object_name, 
			self.name]
		return self.execute_busctl(com)

	def get_property(self, prop_name: str) -> CompletedProcess:
		com = ["get-property",
			self.service_name, 
			self.object_name,
			self.name,
			self.quote(prop_name)]
		return self.execute_busctl(com)
