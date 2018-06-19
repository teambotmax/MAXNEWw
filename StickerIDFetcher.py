# -*- coding: utf-8 -*-

import TyfeAPI
from TyfeAPI.lib.curve.ttypes import *

print("\nWelcome to Sticker ID Fetcher\n")

def loginStatement(url):
    print("Login with this URL to continue: "+url+"\n")

cl = TyfeAPI.LINE()
cl.nxtQRLogin(callback=loginStatement)

def operate(op):
    try:
        if op.type == 25:
            msg = op.message
            if msg.contentType == 7:
                print("{")
                print("    \033[1;32m'STKPKGID'\033[0m: \033[1;32m'"+msg.contentMetadata["STKPKGID"]+"'\033[0m,")
                print("    \033[1;32m'STKTXT'\033[0m: \033[1;32m'"+msg.contentMetadata["STKTXT"]+"'\033[0m,")
                print("    \033[1;32m'STKVER'\033[0m: \033[1;32m'"+msg.contentMetadata["STKVER"]+"'\033[0m,")
                print("    \033[1;32m'STKID'\033[0m: \033[1;32m'"+msg.contentMetadata["STKID"]+"'\033[0m")
                print("}\n")
    except:
        pass

print("Now, send a sticker to any chat room. The program will automatically fetch the ID of the sticker\n")

try:
    while True:
        try:
            Ops = cl.fetchOps(cl.Poll.rev, 5)
        except EOFError:
            raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))
        for Op in Ops:
            if (Op.type != 0 and Op.type != OpType.END_OF_OPERATION):
                cl.Poll.rev = max(cl.Poll.rev, Op.revision)
                operate(Op)
except:
    print("\nEnd of operation\nThis program is created by Sven team\n")
