from catalog.common import *


class Game(Item):
    category = ItemCategory.Game
    igdb = PrimaryLookupIdDescriptor(IdType.IGDB)
    steam = PrimaryLookupIdDescriptor(IdType.Steam)
    douban_game = PrimaryLookupIdDescriptor(IdType.DoubanGame)
    platforms = jsondata.ArrayField(default=list)
