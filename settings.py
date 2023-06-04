from os import environ

use_bot_ug = eval(environ.get('USE_BOT_UG')) if environ.get('USE_BOT_UG') is not None else False

SESSION_CONFIGS = [
    dict(
        name='public_goods_simple',
        display_name="Public Goods Game",
        num_demo_participants=3,
        app_sequence=['public_goods_simple', 'payment_info'],
        endowment_default=40,
        MPCR=0.5
    ),
    dict(
        name='ultimatum_game',
        display_name="Ultimatum Game",
        app_sequence=['ultimatum_game', 'payment_info'],
        num_demo_participants=2,
        use_browser_bots=use_bot_ug
    ),
dict(
        name='distributive_bargaining_game',
        display_name="Distributive Bargaining Game",
        app_sequence=['distributive_bargaining_game', 'payment_info'],
        num_demo_participants=2,
        use_browser_bots=False
    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as session.config,
# e.g. session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = True

ROOMS = [
    dict(
        name='room_ug',
        display_name='Room UG (all players)',
        participant_label_file='_rooms/room_ug.txt',
        use_secure_urls=True
    ),
    dict(
        name='room1_pgg',
        display_name='Room 1 PGG (1-10 players)',
        participant_label_file='_rooms/room1_pgg.txt',
        use_secure_urls=True
    ),
    dict(
        name='room2_pgg',
        display_name='Room 2 PGG (11-20 players)',
        participant_label_file='_rooms/room2_pgg.txt',
        use_secure_urls=True
    ),
    dict(
        name='room3_pgg',
        display_name='Room 3 PGG (21-30 players)',
        participant_label_file='_rooms/room3_pgg.txt',
        use_secure_urls=True
    ),
    dict(
        name='room4_pgg',
        display_name='Room 4 PGG (31-40 players)',
        participant_label_file='_rooms/room4_pgg.txt',
        use_secure_urls=True
    ),
    dict(
        name='room5_pgg',
        display_name='Room 5 PGG (41-50 players)',
        participant_label_file='_rooms/room5_pgg.txt',
        use_secure_urls=True
    ),
    dict(
        name='room6_pgg',
        display_name='Room 6 PGG (51-60 players)',
        participant_label_file='_rooms/room6_pgg.txt',
        use_secure_urls=True
    )
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

# don't share this with anybody.
SECRET_KEY = 'skeyskeyskeyskeyskeyskeyskeyskeyskeyskeyskeyskeyskeyskey'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

# inactive session configs
