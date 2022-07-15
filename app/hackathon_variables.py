# -*- coding: utf-8 -*-
# HACKATHON PERSONALIZATION
import os

from dotenv import load_dotenv
load_dotenv("app.env")

from django.utils import timezone

HACKATHON_NAME = 'Hack WashU'
# What's the name for the application
HACKATHON_APPLICATION_NAME = 'My HackWashU'
# Hackathon timezone
TIME_ZONE = 'America/Chicago'
# This description will be used on the html and sharing meta tags
HACKATHON_DESCRIPTION = 'Hack WashU is taking place from Octover 14th to 16th.'
# Domain where application is deployed, can be set by env variable
HACKATHON_DOMAIN = os.environ.get('DOMAIN', None)
HEROKU_APP_NAME = os.environ.get('HEROKU_APP_NAME', None)
if HEROKU_APP_NAME and not HACKATHON_DOMAIN:
    HACKATHON_DOMAIN = '%s.herokuapp.com' % HEROKU_APP_NAME
elif not HACKATHON_DOMAIN:
    HACKATHON_DOMAIN = 'localhost:80'
# Hackathon contact email: where should all hackers contact you. It will also be used as a sender for all emails
HACKATHON_CONTACT_EMAIL = os.environ.get('DEV_EMAIL', 'organizer@hackwashu.io')
# Hackathon logo url, will be used on all emails
HACKATHON_LOGO_URL = 'https://www.hackwashu.io/img/hackwashu-ab.32b7d0b4.svg'

HACKATHON_OG_IMAGE = 'https://www.hackwashu.io/img/hackwashu-ab.32b7d0b4.svg'
# (OPTIONAL) Track visits on your website
HACKATHON_GOOGLE_ANALYTICS = 'G-FSJQ7KKMGF'
# (OPTIONAL) Hackathon Twitter user
# HACKATHON_TWITTER_ACCOUNT = 'hackupc'
# (OPTIONAL) Hackathon Facebook page
# HACKATHON_FACEBOOK_PAGE = 'hackupc'
# (OPTIONAL) Hackathon YouTube channel
HACKATHON_YOUTUBE_PAGE = 'UCiiRorGg59Xd5Sjj9bjIt-g'
# (OPTIONAL) Hackathon Instagram user
HACKATHON_INSTAGRAM_ACCOUNT = 'hackwashu'
# (OPTIONAL) Hackathon Medium user
# HACKATHON_MEDIUM_ACCOUNT = 'hackupc'
# (OPTIONAL) Github Repo for this project (so meta)
HACKATHON_GITHUB_REPO = 'https://github.com/hack-washu/myhackwashu'

# (OPTIONAL) Applications deadline
HACKATHON_APP_DEADLINE = timezone.datetime(2022, 9, 16, 23, 59, tzinfo=timezone.pytz.timezone(TIME_ZONE))
# (OPTIONAL) Online checkin activated
ONLINE_CHECKIN = timezone.datetime(2022, 4, 29, 17, 00, tzinfo=timezone.pytz.timezone(TIME_ZONE))
# (OPTIONAL) When to arrive at the hackathon
HACKATHON_ARRIVE = ''

# (OPTIONAL) When to arrive at the hackathon
HACKATHON_LEAVE = ''

# (OPTIONAL) Hackathon live page
HACKATHON_LIVE_PAGE = 'https://live.hackupc.com'

# (OPTIONAL) Regex to automatically match organizers emails and set them as organizers when signing up
REGEX_HACKATHON_ORGANIZER_EMAIL = '^.*@hackupc\.com$'

HACKATHON_ORGANIZER_EMAILS = ['jackheuberger@wustl.edu', 'e.sheehan@wustl.edu', 'b.hsu@wustl.edu', 'skim27@wustl.edu']

# (OPTIONAL) Send 500 errors to email while on production mode
HACKATHON_DEV_EMAILS = ['organizer@hackwashu.io', ]

# Baggage configuration
BAGGAGE_ENABLED = True
BAGGAGE_PICTURE = True

# Reimbursement configuration
REIMBURSEMENT_ENABLED = False
DEFAULT_REIMBURSEMENT_AMOUNT = 100
CURRENCY = '€'
REIMBURSEMENT_EXPIRY_DAYS = 5
REIMBURSEMENT_REQUIREMENTS = 'You have to submit a project and demo it during the event in order to get reimbursed'
REIMBURSEMENT_DEADLINE = timezone.datetime(2022, 4, 22, 23, 59, tzinfo=timezone.pytz.timezone(TIME_ZONE))

# (OPTIONAL) Max team members. Defaults to 4
TEAMS_ENABLED = True
HACKATHON_MAX_TEAMMATES = 4

# (OPTIONAL) Code of conduct link
# CODE_CONDUCT_LINK = "https://pages.hackcu.org/code_conduct/"

# (OPTIONAL) Slack credentials
# Highly recommended to create a separate user account to extract the token from
SLACK = {
    'team': os.environ.get('SL_TEAM', 'test'),
    # Get it here: https://api.slack.com/custom-integrations/legacy-tokens
    'token': os.environ.get('SL_TOKEN', None)
}

# (OPTIONAL) Logged in cookie
# This allows to store an extra cookie in the browser to be shared with other application on the same domain
# LOGGED_IN_COOKIE_DOMAIN = '.gerard.space'
# LOGGED_IN_COOKIE_KEY = 'hackassistant_logged_in'

# Hardware configuration
# Hardware request time length (in minutes)
HARDWARE_ENABLED = False
#Hardware request time length (in minutes)
HARDWARE_REQUEST_TIME = 15


SLACK_BOT = {
    'id': os.environ.get('SL_BOT_ID', None),
    'token': os.environ.get('SL_BOT_TOKEN', None),
    'channel': os.environ.get('SL_BOT_CHANNEL', None),
    'director1': os.environ.get('SL_BOT_DIRECTOR1', None),
    'director2': os.environ.get('SL_BOT_DIRECTOR2', None)
}
# Enable judging tab
JUDGING_ENABLED = False

# Can Hackers start a request on the hardware lab?
# HACKERS_CAN_REQUEST = False

# Enable dubious separate pipeline (disabled by default)
DUBIOUS_ENABLED = True


# Enable blacklist separate pipeline (disabled by default)
BLACKLIST_ENABLED = True

SUPPORTED_RESUME_EXTENSIONS = ['.pdf']

# Mentor/Volunteer applications can expire if they are invited, set to False to not
MENTOR_EXPIRES = False
VOLUNTEER_EXPIRES = False

DISCORD_HACKATHON = False
HYBRID_HACKATHON = True
N_MAX_LIVE_HACKERS = 350

SERVER_EMAIL = 'MyHackWashU <organizers@hackwashu.io>'

CODE_CONDUCT_LINK = 'https://legal.hackersatupc.org/hackupc/code_of_conduct'
LEGAL_LINK = 'https://legal.hackersatupc.org/hackupc/legal_notice'
PRIVACY_LINK = 'https://docs.google.com/document/d/1lU2Jg9d9MVRokEEiWw8N-aMKH8suRlZhjiT56oI6K9o/edit#heading=h.g8lp823ap289'
TERMS_LINK = 'https://legal.hackersatupc.org/hackupc/terms_and_conditions'
