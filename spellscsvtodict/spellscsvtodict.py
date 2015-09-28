import csv
import os


class SpellsCsvToDict:
    """
    Builds the spell dictionary
    """

    def __init__ (self, filename = "SpellsDB.csv", useRelativePath = False, keyName = 'name', dbEncoding = 'utf-8') :
        """
        Reads the db from the specified location, defaulting to the one in the project.
        Imports the csv into a dictionary keyed by a lowercased version of the specified key
        :param filename: the name of the file to import
        :param useRelativePath: should we use a file relative to execution location, or in direct relation to this script?
        :param keyName: what key of the csv to key the dictionary by
        :param dbEncoding: what character set the db is encoded in
        :return:
        """
        self.db = {}
        toOpen = filename if useRelativePath else os.path.join(os.path.dirname(__file__), filename)
        with open(toOpen, encoding=dbEncoding) as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                self.db[row[keyName].lower()] = row

    def getSpell(self, spellName):
        """
        Get the row for the specified spell
        :param spellName: the spell to get
        :return: description of specificed spell
        """
        trueName = spellName.lower()
        return self.db[trueName] if trueName in self.db else None

    def getSpells(self, spellNames):
        """
        get multiple spells
        :param spellNames:  the names of multiple spells
        :return: a list of descriptions of specified spells
        """
        if isinstance(spellNames, list):
            toRet = {}
            for spell in spellNames:
                desc = self.getSpell(spell)
                if desc is not None:
                    toRet[spell] = desc
            return toRet
        elif isinstance(spellNames, dict):
            toRet = {}
            for _, spell in spellNames:
                desc = self.getSpell(spell)
                if desc is not None:
                    toRet[spell] = desc
            return toRet
        elif isinstance(spellNames, str):
            desc = self.getSpell(spellNames)
            return {spellNames : desc } if desc is not None else {}
        else :
            return None