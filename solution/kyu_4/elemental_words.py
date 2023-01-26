"""
Elemental Words
https://www.codewars.com/kata/56fa9cd6da8ca623f9001233
"""
"""
Each element in the periodic table has a symbol associated with it. For instance, the symbol for the element Yttrium is Y. A fun thing to do is see if we can form words using symbols of elements strung together. The symbol for Einsteinium is Es, so the symbols for Yttrium and Einsteinium together form:

Y + Es = YEs

Yes! Ignoring capitalization, we can think of any string of letters formed by the concatenation of one or more element symbols as an elemental word -- per the above,yes is an elemental word. There is only one combination of element symbols that can form yes, but in general, there may be more than one combination of element symbols that can form a given elemental word. Let's call each different combination of element symbols that can form a given elemental word word an elemental form of word.

Your task is to implement the function elementalForms(word), which takes one parameter (the string word), and returns an array (which we'll call forms). If word can be formed by combining element symbols from the periodic table, then forms should contain one or more sub-arrays, each consisting of strings of the form 'elementName (elementSymbol)', for each unique combination of elements that can form word.
Example

The word 'snack' can be formed by concatenating the symbols of 3 different combinations of elements:

----------------------------------------------------
|       1        |       2        |       3        |
|---------------------------------------------------
| Sulfur    (S)  | Sulfur    (S)  | Tin       (Sn) |
| Nitrogen  (N)  | Sodium    (Na) | Actinium  (Ac) |
| Actinium  (Ac) | Carbon    (C)  | Potassium (K)  |
| Potassium (K)  | Potassium (K)  |                |
----------------------------------------------------

So elementalForms('snack') should return the following array:

[
  ['Sulfur (S)', 'Nitrogen (N)', 'Actinium (Ac)', 'Potassium (K)'],
  ['Sulfur (S)', 'Sodium (Na)', 'Carbon (C)', 'Potassium (K)'],
  ['Tin (Sn)', 'Actinium (Ac)', 'Potassium (K)']
]

Guidelines

    Symbols can have length 1, 2 or 3 (this kata uses pre-2016 temporary symbols for elements 113, 115, 117 and 118).
    Capitalization does not matter:

elemental_forms('beach')
// => [ ['Beryllium (Be)', 'Actinium (Ac)', 'Hydrogen (H)'] ]
elemental_forms('BEACH')
// => [ ['Beryllium (Be)', 'Actinium (Ac)', 'Hydrogen (H)'] ]

    The order of the returned sub-arrays does not matter, but the order of the strings within each sub-array does matter -- they should be in the order that "spells out" word.
    If word is not an elemental word (that is, no combination of one or more element symbols can form word), return an empty array.
    You do not need to check the type of word. It will always be a (possibly empty) string.

Finally, a dict ELEMENTS has been preloaded and is accessible from your code, which is a map from each element symbol to its corresponding full name (e.g. ELEMENTS['Na'] == 'Sodium').

Have fun!
"""

ELEMENTS = {
    'H': 'Hydrogen',
    'He': 'Helium',
    'Li': 'Lithium',
    'Be': 'Beryllium',
    'B': 'Boron',
    'C': 'Carbon',
    'N': 'Nitrogen',
    'O': 'Oxygen',
    'F': 'Fluorine',
    'Ne': 'Neon',
    'Na': 'Sodium',
    'Mg': 'Magnesium',
    'Al': 'Aluminium',
    'Si': 'Silicon',
    'P': 'Phosphorus',
    'S': 'Sulfur',
    'Cl': 'Chlorine',
    'Ar': 'Argon',
    'K': 'Potassium',
    'Ca': 'Calcium',
    'Sc': 'Scandium',
    'Ti': 'Titanium',
    'V': 'Vanadium',
    'Cr': 'Chromium',
    'Mn': 'Manganese',
    'Fe': 'Iron',
    'Co': 'Cobalt',
    'Ni': 'Nickel',
    'Cu': 'Copper',
    'Zn': 'Zinc',
    'Ga': 'Gallium',
    'Ge': 'Germanium',
    'As': 'Arsenic',
    'Se': 'Selenium',
    'Br': 'Bromine',
    'Kr': 'Krypton',
    'Rb': 'Rubidium',
    'Sr': 'Strontium',
    'Y': 'Yttrium',
    'Zr': 'Zirconium',
    'Nb': 'Niobium',
    'Mo': 'Molybdenum',
    'Tc': 'Technetium',
    'Ru': 'Ruthenium',
    'Rh': 'Rhodium',
    'Pd': 'Palladium',
    'Ag': 'Silver',
    'Cd': 'Cadmium',
    'In': 'Indium',
    'Sn': 'Tin',
    'Sb': 'Antimony',
    'Te': 'Tellurium',
    'I': 'Iodine',
    'Xe': 'Xenon',
    'Cs': 'Caesium',
    'Ba': 'Barium',
    'La': 'Lanthanum',
    'Ce': 'Cerium',
    'Pr': 'Praseodymium',
    'Nd': 'Neodymium',
    'Pm': 'Promethium',
    'Sm': 'Samarium',
    'Eu': 'Europium',
    'Gd': 'Gadolinium',
    'Tb': 'Terbium',
    'Dy': 'Dysprosium',
    'Ho': 'Holmium',
    'Er': 'Erbium',
    'Tm': 'Thulium',
    'Yb': 'Ytterbium',
    'Lu': 'Lutetium',
    'Hf': 'Hafnium',
    'Ta': 'Tantalum',
    'W': 'Tungsten',
    'Re': 'Rhenium',
    'Os': 'Osmium',
    'Ir': 'Iridium',
    'Pt': 'Platinum',
    'Au': 'Gold',
    'Hg': 'Mercury',
    'Tl': 'Thallium',
    'Pb': 'Lead',
    'Bi': 'Bismuth',
    'Po': 'Polonium',
    'At': 'Astatine',
    'Rn': 'Radon',
    'Fr': 'Francium',
    'Ra': 'Radium',
    'Ac': 'Actinium',
    'Th': 'Thorium',
    'Pa': 'Protactinium',
    'U': 'Uranium',
    'Np': 'Neptunium',
    'Pu': 'Plutonium',
    'Am': 'Americium',
    'Cm': 'Curium',
    'Bk': 'Berkelium',
    'Cf': 'Californium',
    'Es': 'Einsteinium',
    'Fm': 'Fermium',
    'Md': 'Mendelevium',
    'No': 'Nobelium',
    'Lr': 'Lawrencium',
    'Rf': 'Rutherfordium',
    'Db': 'Dubnium',
    'Sg': 'Seaborgium',
    'Bh': 'Bohrium',
    'Hs': 'Hassium',
    'Mt': 'Meitnerium',
    'Ds': 'Darmstadtium',
    'Rg': 'Roentgenium',
    'Cn': 'Copernicium',
    'Uut': 'Ununtrium',
    'Fl': 'Flerovium',
    'Uup': 'Ununpentium',
    'Lv': 'Livermorium',
    'Uus': 'Ununseptium',
    'Uuo': 'Ununoctium',
}


def elemental_forms(word: str, current_form: list[str] = None, all_forms: list[list[str]] = None) -> list[list[str]]:
    if all_forms is None:  # init lists
        all_forms, current_form = [], []  # all_forms stores valid results for fully processed words from all recursions, current_form stores work-in-progress partial word for current recursion
    if not word:  # the word is fully processed (or empty input)
        all_forms.append(current_form)  # store result to list of results
    for el in ELEMENTS.keys():  # iterate elements
        if word.lower().startswith(el.lower()):  # word starts with element code
            current_form_copy = current_form.copy() + [f'{ELEMENTS[el]} ({el})']  # copy current result (to separate from current recursion) and add element to a copy
            word_remainder = word[len(el):]  # remove element code from start of the word
            elemental_forms(word_remainder, current_form_copy, all_forms)  # start new recursion to process remainder of the word
    return all_forms  # return results
