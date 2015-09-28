import argparse
from spellscsvtodict import SpellsCsvToDict
from spellpdfprinter import SpellPdfPrinter

def makeSpellCards(spellNames):
    spellDescriptions = SpellsCsvToDict()
    spells = spellDescriptions.getSpells(spellNames)

    pdfPrinter = SpellPdfPrinter(spells)
    pdfPrinter.getSixPerSheetPdf()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('spells', nargs = '*', help='Names of spells to get cards for')
    parser.add_argument('-f', '--files', nargs = '*', help = 'File mode. Input file names containing names of spells separated by a newline')
    args = parser.parse_args()
    spells = args.spells if args.spells else []
    if(args.files):
        for file in args.files:
            with open(file) as spellList:
                for spell in spellList:
                    spells.append(spell.strip())

    makeSpellCards(spells)