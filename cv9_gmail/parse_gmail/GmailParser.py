import pandas as pd
from constants.CONSTANTS import COLUMNS_IN_ROW, MATRIX_OUTPUT
import math
import numpy as np
from itertools import product





class GmailParser():
    def __init__(self):
        self.emails = []
        self.matrix = None

    def parse(self, path_to_file, names=COLUMNS_IN_ROW):
        raw_gmail_data = pd.read_csv(path_to_file, delimiter=';', encoding='unicode_escape', header=None)
        raw_gmail_data.columns = names
        self.build_matrix(raw_gmail_data)

    def parse_email_item(self, item):
        lIndex = item.find('<')
        rIndex = item.find('>')

        if lIndex == -1:
            name = None
            mail = item.strip()
        else:
            name = item[0:lIndex].strip()
            mail = item[lIndex+1:rIndex]    
        return (mail, name)

    def parse_from(self, from_email):
        parsed = [self.parse_email_item(e.strip()) for e in from_email.split(',')]
        return parsed

    def parse_to(self, to_emails):
        parsed = [self.parse_email_item(e.strip()) for e in to_emails.split(',')]
        return parsed

    def parse_cc(self, cc_string):
        result = None if pd.isnull(cc_string) else [cc.strip() for cc in cc_string.split(',')]
        return result

    #delete
    def parse_from_or_to_mail(self, from_or_to_string):
        lIndex = from_or_to_string.find('<')
        rIndex = from_or_to_string.find('>')

        if lIndex == -1:
            name = None
            mail = from_or_to_string.strip()
        else:
            name = from_or_to_string[0:lIndex].strip()
            mail = from_or_to_string[lIndex+1:rIndex]    
        return (mail, name)


    def parse_row(self, row):
        return (self.parse_from(row['from']), self.parse_to(row['to']), self.parse_cc(row['cc']))

    def create_emails_set(self, raw_data):
        for index, row in list(raw_data.iterrows())[0:2]:
            self.process_row_with_add_to_emails(*self.parse_row(row))
        self.emails = list(set(self.emails)) #unique

    def process_row_with_add_to_emails(self, from_mail, to_mail, cc_mails):
        from_emails, from_names = zip(*from_mail)
        to_emails, to_names = zip(*to_mail)
        self.emails += from_emails
        self.emails += to_emails
        if cc_mails is not None:
            self.emails += cc_mails
        
    def create_matrix_from_set(self, raw_data, emails_set):
        lE = len(emails_set)
        self.matrix = np.zeros(shape=(lE, lE))
        dic_email_index = {email:index for index,email in enumerate(emails_set)}
        for index, row in list(raw_data.iterrows())[0:2]:
            self.process_row_with_add_to_matrix(*self.parse_row(row), dic_email_index)
        
    def process_row_with_add_to_matrix(self, from_mails, to_mails, cc_mails, emails_dic_email_index):
        current_emails = []
        from_emails, from_names = zip(*from_mails)
        to_emails, to_names = zip(*to_mails)

        current_emails += from_emails
        current_emails += to_emails

        if cc_mails is not None:
            current_emails += cc_mails
        prod = list(product(current_emails,current_emails))
        result = list(filter(lambda a: a[0] != a[1], prod))

        for tup in result:
            i = emails_dic_email_index[tup[0]]
            j = emails_dic_email_index[tup[1]]
            self.matrix[i][j] += 1



    def build_matrix(self, raw_data):
        self.create_emails_set(raw_data)
        self.create_matrix_from_set(raw_data, self.emails)
        output = pd.DataFrame(self.matrix, columns=self.emails, index=self.emails).to_string()
        with open(MATRIX_OUTPUT, "w") as file1: 
            file1.writelines(output) 
        return (self.emails, self.matrix)
    
