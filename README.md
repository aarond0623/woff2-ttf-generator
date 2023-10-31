Woff2 Font Generator
====================

This project is for converting variable woff2 files downloaded from a website into static ttf files for desktop use.

Woff font files are sometimes divided into separate unicode ranges. While fonttools can merge separate fonts into one font, it presently cannot do this with variable fonts. This tool first creates static fonts for different weights, then combines them into static ttf files.

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

Make woff2 tools.
```bash
cd woff2
make clean all
cd ..
```

Usage
-----

Save your variable woff2 files into the input folder. Normal fonts should go in the "normal" folder and italic fonts should go in the "italic" folder.

Make `convert.sh` executable and run it.
```bash
chmod +x convert.sh
./convert.sh
```

The static ttf files will be saved into the output folder.
