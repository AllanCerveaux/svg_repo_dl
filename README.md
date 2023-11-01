<div align="center">
	<img src=".github/README/Logo.svg" alt="logo"/>
	<p><strong>SVG_REPO Pack</strong> Downloader A small personal tool that will allow you to download an icon pack on <a href="https://www.svgrepo.com/">SVGREPO</a> with the CLI.</p>

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![last_commit](https://img.shields.io/github/last-commit/AllanCerveaux/svg_repo_dl?style=flat-square)](https://github.com/AllanCerveaux/svg_repo_dl/commits/master)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/AllanCerveaux/svg_repo_dl/blob/master/LICENSE)
</div>

___

## Requirement :

- Python 3
- BeautifulSoup
- Progress

## Installation
Follow this step:

Clone the repo
```bash
git clone git@github.com:AllanCerveaux/svg_repo_dl.git
```

Go in folder
```bash
cd svg_repo_dl
```

And run install.sh
```bash
sh install.sh
```

or alternatively:
```bash
PYTHONPATH=$(pwd) python -m svgrepodl --help
```
## Usage :

```bash
$ svgrepodl [URL] --path[-p]
$ svgrepodl --help # Show all commands
$ svgrepodl https://www.svgrepo.com/collection/role-playing-game/ # Run downloader
```

By default, the program saves the icons in the current directory.

Enjoy !

## License
The MIT License (MIT) 2020 - Callan, 2023 - Drzraf. Please have a look at the [License](https://github.com/AllanCerveaux/svg_repo_dl/blob/master/LICENSE) for more details.

## Metadata

Concurrency is not supported but it's possible to rely on `svgrepodl` for listing URL and actually download resources using another tool like `aria2c`

The same applies to metadata: Once SVG files are retrieved, assuming consistent `<id>-<slug>.svg` names, downloading is a matter of:
$ `find . -name '*.svg' -printf '%f\n' | sed -r 's!([0-9]+)-(.*)\.svg!https://api.svgrepo.com/svg/\1/\2\n\tout=\1-\2.json!' | aria2c --auto-file-renaming=false --allow-overwrite=false -i - -j 4`
