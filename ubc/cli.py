#!/usr/bin/env python3
from argparse import ArgumentParser, Namespace
from subprocess import CompletedProcess
from sys import argv as sys_argv
from typing import List, Type

from .element_dbus import ElementDBus
from .interface_dbus import InterfaceDBus
from .service_dbus import ServiceDBus


def parse_args(args: List[str]) -> Namespace:
	parser = ArgumentParser(
		prog = "ubc",  
		description = "Lecture de propriété et introspection avec busctl")
	parser.add_argument("-s", "--service", 
		help = "service d-bus",
		default = "")
	parser.add_argument("-o", "--object", 
		help = "objet lié au service",
		default = "")
	parser.add_argument("-i", "--interface",
		help = "interface liée à l'objet",
		default = "")
	parser.add_argument("property",
		help = "nom de la propriété à afficher",
		nargs = '?',
		default = "")
	return parser.parse_args(args)

def get_driver(args: Namespace) -> Type[ElementDBus]:
	"""Choix de la classe à instancier"""
	driver = ServiceDBus(args.service)

	if args.object:
		driver = driver.obj(args.object)

		if args.interface:
			driver = driver.iface(args.interface)
	return driver

def execute_com(args: Namespace) -> CompletedProcess:
	"""Choix de la méthode à appeler"""
	driver = get_driver(args)

	if not args.service:
		# Uniformisation defaut introspect pour vide
		return driver.list()

	if type(driver) == ServiceDBus:
		# Uniformisation defaut introspect pour service
		return driver.tree()

	if type(driver) == InterfaceDBus and args.property:
		return driver.get_property(args.property)
	return driver.introspect()

def main() -> str:
	args = parse_args(sys_argv[1:])
	res = execute_com(args)

	if res.returncode == 0:
		return res.stdout.strip()
	return res.stderr.strip()
