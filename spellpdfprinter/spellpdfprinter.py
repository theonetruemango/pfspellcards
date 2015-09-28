import fpdf


class SpellPdfPrinter:
    """
    Make the spells pretty
    Note: This module works on the assumption that the standard csv has been imported, with standard keys
    """
    def __init__(self, spellDict):
        self.spellDict = spellDict

    def getExampleDoc(self):
        pdf = fpdf.FPDF(format="letter", unit='pt')
        pdf.set_margins(0,0,0)
        pdf.add_page()
        pdf.set_font('Arial','', 16)
        pdf.cell(306, 244, "SPELL 1", align= 'C', border=1)
        pdf.cell(306, 244, "SPELL 2", align='C', ln=1, border=1)
        pdf.cell(306, 244, "SPELL 3", align='C', border=1)
        pdf.cell(306, 244, "SPELL 4", align='C', ln=1, border=1)
        pdf.cell(306, 244, "SPELL 5", align='C', border=1)
        pdf.cell(306, 244, "SPELL 6", align='C', border=1, ln=1)

        pdf.add_page()
        pdf.set_font('Arial','', 12)
        pdf.cell(306, 244, "DESC 1", align= 'C', border=1)
        pdf.cell(306, 244, "DESC 2", align='C', ln=1, border=1)
        pdf.cell(306, 244, "DESC 3", align='C', border=1)
        pdf.cell(306, 244, "DESC 4", align='C', ln=1, border=1)
        pdf.cell(306, 244, "DESC 5", align='C', border=1)
        pdf.cell(306, 244, "DESC 6", align='C', border=1)
        pdf.output('test.pdf')

    def getSixPerSheetPdf(self):
        cardWidth = 306
        titleHeight = 30
        lineHeight = 22
        nameSize = 24
        titleSize = 12
        lineSize = 8

        pdf = fpdf.FPDF(format='letter', unit='pt')
        pdf.set_margins(0,0,0)
        pdf.add_page()
        # rotate every 6
        i=0
        backside = []
        for _, spell in self.spellDict.items():
            frontText = self.__getFrontsideStrings(spell)
            # name
            pdf.set_font('Arial','', nameSize)
            pdf.cell(cardWidth, titleHeight, frontText['name'], align='C', ln=1)

            pdf.set_font('Arial','', lineSize)

            # school, subschool, descriptor
            pdf.cell(cardWidth/2, lineHeight, frontText['schoolString'], align='C')

            # Domain
            pdf.cell(cardWidth/2, lineHeight, frontText['domainString'], align='C', ln=1)

            # Level
            pdf.cell(cardWidth, lineHeight, frontText['levelString'], align='C', ln=1)

            # Casting Stats
            pdf.set_font('Arial','', titleSize)
            pdf.cell(cardWidth, titleHeight, "Casting Information", align='C', ln=1)
            pdf.set_font('Arial','', lineSize)

            # Casting Time
            pdf.cell(cardWidth, lineHeight, frontText['castingTimeString'], align='C', ln=1)
            # Components
            pdf.cell(cardWidth, lineHeight, frontText['componentsString'], align='C', ln=1)

            # Effects
            pdf.set_font('Arial','', titleSize)
            pdf.cell(cardWidth, titleHeight, "Effects", align='C', ln=1)
            pdf.set_font('Arial','', lineSize)

            # Range
            pdf.cell(cardWidth/2, lineHeight, frontText['rangeString'], align='C')
            # Duration
            pdf.cell(cardWidth/2, lineHeight, frontText['durationString'], align='C', ln=1)

            # Area/Effect
            pdf.cell(cardWidth/2, lineHeight, frontText['areaOrEffectString'], align='C')
            # Target
            pdf.cell(cardWidth/2, lineHeight, frontText['targetString'], align='C', ln=1)

            # Saving Throw
            pdf.cell(cardWidth/2, lineHeight, frontText['savingThrowString'], align='C')
            # Spell Resistance
            pdf.cell(cardWidth/2, lineHeight, frontText['spellResistanceString'], align='C', ln=1)

            pdf.output('test.pdf')
            break

    def __getFrontsideStrings(self, spell):
        toRet ={}
        toRet['name'] = spell['name']
        toRet['schoolString'] = "School: " + spell['school'] + \
                                (" (" + spell['subschool'] + ") " if spell['subschool'] else "") + \
                                (" [" + spell["descriptor"] + "] " if spell['descriptor'] else "")
        toRet['levelString'] = "Level: " + spell['spell_level']
        toRet['domainString'] = "Domain: " + spell['domain'] if spell['domain'] else ""
        toRet['castingTimeString'] = "Casting Time: " + spell['casting_time']
        toRet['componentsString'] = "Components: " + spell['components']
        toRet['rangeString'] = "Range: " + spell['range']
        if spell['area'] and spell['effect']:
            toRet['areaOrEffectString'] = "Area/Effect: See Text"
        elif spell['area']:
            toRet['areaOrEffectString'] = "Area: " + spell['area']
        elif spell['effect']:
            toRet['areaOrEffectString'] = "Effect: " + spell['effect']
        else:
            toRet['areaOrEffectString'] = ""
        toRet['targetString'] = "Targets: " + spell['targets'] if spell['targets'] else ""
        toRet['durationString'] = "Duration: " + spell['duration']
        toRet['savingThrowString'] = "Saving Throw: " + spell['saving_throw']
        toRet['spellResistanceString'] = "Spell Resistance: " + spell['spell_resistence']
        return toRet