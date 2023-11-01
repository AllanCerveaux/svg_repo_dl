from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
	name = 'svgrepodl',
	author="callan",
	author_email="cerveauxallanjean@gmail.com",
	description="Pack Downloader for SVG REPO",
	long_description=long_description,
	long_description_content_type="text/markdown",
	homepage="https://github.com/AllanCerveaux/svg_repo_dl/blob/master/README.md",
	version = '0.0.1',
	license="MIT",
	py_modules=['svgrepodl'],
	install_requires = [
		'bs4',
		'requests',
		'progress',
		'click',
		'colored',
	],
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	entry_points = {
		'console_scripts': [
			'svgrepodl = svgrepodl.__main__:main'
		]
	}
)
