import os

ITEM_NAME = 'name'
ITEM_RECIPE = 'recipe'
ITEM_RECIPE_NORMAL = 'normal'
ITEM_RECIPE_EXPENSIVE = 'expensive'
ITEM_RECIPE_SOURCEC = 'source'
ITEM_RECIPE_OUTPUT = 'result'
ITEM_RECIPE_TIME = 'time'

ITEM_RECIPE_INGREDIENT_NAME = 'name'
ITEM_RECIPE_INGREDIENTT_AMOUNT = 'amount'
ITEM_RECIPE_INGREDIENT_URL = 'url'
ITEM_RECIPE_INGREDIENT_IMG = 'img'

PARSE_RECIPE_PLUS = '+'
PARSE_RECIPE_EQUAL = '→'

ITEM_OTHER_NAME = 'name'
ITEM_OTHER_URL = 'url'
ITEM_OTHER_IMG = 'img'

ITEM_OTHER_COMMENT = 'comment'

TECH_UPGRADE_LIST = 'upgrade'
TECH_VERSION = 'version'

ITEM_JSON_DIRECTORY = os.path.abspath(os.path.join(os.path.dirname(__file__), r'..\json\item'))
TECH_JSON_DIRECTORY = os.path.abspath(os.path.join(os.path.dirname(__file__), r'..\json\tech'))

ITEM_PROTOTYPE = 'Prototype type'