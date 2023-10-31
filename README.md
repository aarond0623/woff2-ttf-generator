Woff2 Font Generator
====================

This project is for converting variable woff2 files downloaded from a website into static ttf files for desktop use.

Requirements
------------

This project requires Google's Woff2 tools to decompress the woff files as well
as fonttools to convert to static fonts, as listed in requirements.txt.

Installation
------------

Clone this repository
```bash
git clone --recursive https://github.com/aarond0623/woff2-ttf-generator.git
cd woff2-ttf-generator
```

Create a virtual environment and activate it.
```bash
python -m venv .venv
source .venv/bin/activate
```

Install requirements.
```bash
python -m pip install -r requirements.txt
```

Make woff2 tools.
```bash
cd woff2
make clean all
cd ..
```
