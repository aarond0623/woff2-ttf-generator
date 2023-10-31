import json
import os
from fontTools import ttLib
from fontTools.merge import Merger
from fontTools.varLib import mutator

# Get the font info from the json file.
with open('font_settings.json', 'r') as f:
    settings = json.load(f)
name = settings['font_name']
weights = settings['weights']
version = settings['version']
year = settings['year']
vendor = settings['vendor']
copyright_text = settings['copyright']

# Folders for normal and italic files:
folders = {
    'Regular': os.path.join('input', 'normal'),
    'Italic': os.path.join('input', 'italic')
}

for slant, folder in folders.items():
    for style, weight in weights.items():
        # Don't use the name "Regular" for the weight
        if style == 'Regular':
            style = ''

        # Remove spaces in the style name.
        style = ''.join(style.split())

        # Merge the different font files with different unicode spans into one
        # ttf file.
        merger = Merger()
        separate_fonts = []
        font_list = [x for x in os.listdir(folder) if x.endswith('.ttf')]
        for font in font_list:
            temp_name = os.path.join(folder, font[:-4] + '-temp.ttf')
            font = ttLib.TTFont(os.path.join(folder, font))
            # For each weight, we create temporary font files for that weight.
            font2 = mutator.instantiateVariableFont(font, {'wght': weight})
            font2.save(temp_name)
            separate_fonts.append(temp_name)

        # Create the merged font
        new_font = merger.merge(separate_fonts)

        # Remove the temporary font files
        delete_fonts = [x for x in os.listdir(folder) if x.endswith('-temp.ttf')]
        for font in delete_fonts:
            os.remove(os.path.join(folder, font))

        # Modify the name table with the provided values
        name_t = new_font['name']
        fullstyle = style
        if slant != 'Regular':
            fullstyle = f'{style} {slant}'.strip()
        fullstyle_ps = fullstyle.replace(' ', '')
        fullname = name
        if fullstyle:
            fullname = f'{name} {fullstyle}'.strip()
        if fullstyle_ps:
            fullname_ps = f'{name}-{fullstyle_ps}'.replace(' ', '').strip()
        name_t.setName(copyright_text, 0, 3, 1, 0x409)
        name_t.setName(copyright_text, 0, 1, 0, 0x0)
        name_t.setName(f'{name} {style}'.strip(), 1, 3, 1, 0x409)
        name_t.setName(f'{name} {style}'.strip(), 1, 1, 0, 0x0)
        name_t.setName(slant, 2, 3, 1, 0x409)
        name_t.setName(slant, 2, 1, 0, 0x0)
        name_t.setName(f'Version {version};{vendor};{fullname_ps};{year}', 3, 3, 1, 0x409)
        name_t.setName(f'Version {version};{vendor};{fullname_ps};{year}', 3, 1, 0, 0x0)
        name_t.setName(fullname, 4, 3, 1, 0x409)
        name_t.setName(fullname, 4, 1, 0, 0x0)
        name_t.setName(f'Version {version}', 5, 3, 1, 0x409)
        name_t.setName(f'Version {version}', 5, 1, 0, 0x0)
        name_t.setName(fullname_ps, 6, 3, 1, 0x409)
        name_t.setName(fullname_ps, 6, 1, 0, 0x0)
        name_t.setName(name, 16, 3, 1, 0x409)
        if style:
            name_t.setName(style, 17, 3, 1, 0x409)

        # Delete any extraneous name entries
        for i in range(273, 285):
            name_t.removeNames(i, 3, 1, 0x409)

        # Save the font file
        if fullstyle_ps:
            print(f"Saving {fullname_ps}.ttf")
            new_font.save(os.path.join('output', f'{fullname_ps}.ttf'))
        else:
            print(f"Saving {name}-Regular.ttf")
            new_font.save(os.path.join('output', f'{name}-Regular.ttf'))



