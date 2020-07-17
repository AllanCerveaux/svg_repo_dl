from setuptools import setup

setup(
	name = 'svgrepodl',
	author="callan",
	author_email="cerveauxallanjean@gmail.com",
	description="Pack Downloader for SVG REPO",
	homepage="https://github.com/AllanCerveaux/svg_repo_dl/blob/master/README.md",
	version = '0.0.1',
	license="MIT",
	py_modules=['svgrepodl'],
	install_requires = [
		'selenium',
		'progress',
		'click',
	],
	entry_points = {
		'console_scripts': [
			'svgrepodl = svgrepodl.__main__:main'
		]
	}
)