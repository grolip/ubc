#!/usr/bin/env python3
from subprocess import CompletedProcess

from .element_dbus import ElementDBus
from .object_dbus import ObjectDBus


class ServiceDBus(ElementDBus):
	def __init__(self, name: str):
		super().__init__(name)

	@classmethod
	def list(self) -> CompletedProcess:
		com = ["list"]
		return self.execute_busctl(com)

	def obj(self, name: str):
		return ObjectDBus(self.name, self.quote(name))

	def tree(self, args: str) -> CompletedProcess:
		com = ["tree", "--list", self.name]
		return self.execute_busctl(com)
