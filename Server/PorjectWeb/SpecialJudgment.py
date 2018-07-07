# Ãÿ ‚≈–∂œ
import re
class CheckIsLegal:

    def check_for_length(self, str):
        length = len(str)
        return length

    def check_for_upper(self, str):
        pattern = re.compile('[A-Z]+')
        match = pattern.findall(str)
        if match:
            return True
        else:
            return False

    def check_for_lower(self, str):
        pattern = re.compile('[a-z]+')
        match = pattern.findall(str)
        if match:
            return True
        else:
            return False

    def check_for_num(self, str):
        pattern = re.compile('[0-9]+')
        match = pattern.findall(str)
        if match:
            return True
        else:
            return False

    def check_for_symbol(self, str):
        pattern = re.compile('([^a-z0-9A-Z])+')
        match = pattern.findall(str)
        if match:
            return True
        else:
            return False

    def check_for_username(self, username):
        if self.check_for_length(username) < 6:
            return False
        if self.check_for_lower(username) is True:
            return False
        if self.check_for_symbol(username) is True:
            return False
        if self.check_for_upper(username) is True:
            return False
        if self.check_for_num(username) is False:
            return False
        return True

    def check_for_password(self, pwd):
        if self.check_for_length(pwd) < 8:
            return False
        if self.check_for_lower(pwd) is False:
            return False
        if self.check_for_symbol(pwd) is False:
            return False
        if self.check_for_upper(pwd) is False:
            return False
        if self.check_for_num(pwd) is False:
            return False
        return True

    def check_for_identity(self, id):
        if self.check_for_lower(id) is False:
            return False
        if self.check_for_symbol(id) is False:
            return False
        if self.check_for_upper(id) is False:
            return False
        if self.check_for_num(id) is False:
            return False
        return True