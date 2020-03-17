#!/usr/bin/env python3
from os.path import join as join_path, normpath
from shlex import quote as shlex_quote
from subprocess import run as subproc_run, PIPE, CompletedProcess
from typing import List


class ElementDBus:
	def __init__(self, name: str):
		self.name = self.quote(name)

	def __str__(self):
		return self.name

	@classmethod
	def execute_busctl(self, com: List[str]) -> CompletedProcess:
		com.insert(0, "busctl")
		return subproc_run(
			" ".join(com),
			shell = True,
			encoding = "utf-8",
			stdout = PIPE,
			stderr = PIPE)

	def quote(self, content: str) -> str:
		return shlex_quote(content)

	def join(self, name: str, other: str) -> str:
		name = '/' + name.replace('.', '/') + '/'
		other = other.replace('.', '/')
		return join_path(name, other)
