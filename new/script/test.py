import time

def amyadd(p1, p2):
    print(p1+p2)

def main(connect):
    con = connect
    while 1:
        amyadd(2,3)
        tpstr = con.sendcmd("ver\n","")
        con.MessageBox(tpstr)
        time.sleep(1)





