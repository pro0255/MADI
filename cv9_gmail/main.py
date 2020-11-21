from parse_gmail.GmailParser import GmailParser
from constants.CONSTANTS import PATH_TO_FILE



parser = GmailParser()
parser.parse(PATH_TO_FILE)