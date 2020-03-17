#!/usr/bin/env python3
import setuptools


setuptools.setup(
	name = "ubc",
	version = "0.0.1",
	author = "grolip",
	url = 'https://github.com/grolip/ubc',
	project_urls = {
		'Source': 'https://github.com/grolip/ubc'},
	description = "Interface pour l'outil busctl",
	packages = setuptools.find_packages(),
	classifiers = [
		'Environment :: Console',
		'Natural Language :: French',
		'Programming Language :: Python :: 3.6',
		'License :: OSI Approved :: MIT License',
		'Intended Audience :: End Users/Desktop',
		'Intended Audience :: System Administrators',
		'Operating System :: POSIX :: Linux',
		'Topic :: Utilities',
	],
	entry_points = {
		"console_scripts": ["ubc = ubc.cli:main"],
	},
)
