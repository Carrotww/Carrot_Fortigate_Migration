import sys
import time

class ASA_migration:
    def __init__(self, forti_addr, forti_grp):
        self.forti_addr = forti_addr
        self.forti_grp = forti_grp
    def asa_readfile(self, file):
        

