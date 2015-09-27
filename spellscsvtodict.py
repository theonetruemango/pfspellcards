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
        :return:
        """
        return self.db[spellName.lower()] if spellName in self.db else None