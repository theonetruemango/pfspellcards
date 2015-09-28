import argparse
from spellscsvtodict import SpellsCsvToDict

def makeSpellCards(spellNames):
    spellDescriptions = SpellsCsvToDict()
    spells = spellDescriptions.getSpells(spellNames)

    # print(spells)
    for key, value in spells.items():
        print (key + ": " + value['description'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('spells', nargs = '*', help='Names of spells to get cards for')
    parser.add_argument('-f', '--files', nargs = '*', help = 'File mode. Input file names containing names of spells separated by a newline')
    args = parser.parse_args()
    spells = args.spells
    for file in args.files:
        with open(file) as spellList:
            for spell in spellList:
                spells.append(spell.strip())

    makeSpellCards(spells)