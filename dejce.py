'''
Descripttion: 
Author: yumu
Email: 2@33.al
Date: 2021-01-28 20:31:16
LastEditors: yumu
LastEditTime: 2021-01-28 20:58:29
'''
#coding=utf-8
import re
import sys
import logging
import argparse

logging.basicConfig(level=logging.DEBUG,format="%(message)s")

def decode(inpath,topath):
    num = 0
    with open(inpath) as f:
        contents = f.read()
        # unicode decode
        p1 = re.compile(r'\\u+?[0-9a-f]{4,6}?')
        res1 = p1.findall(contents)
        for x in res1:
            contents = contents.replace(x,chr(int(x[x.index('0'):],16)))
        # cdata decode
        p2 = re.compile(r'<\!\[CDATA\[.\]\]>')
        res2 = p2.findall(contents)
        for x in res2:
            #print(x[9])
            contents = contents.replace(x,x[9])
        # html decode
        p3 = re.compile(r'&#.*?;')
        res3 = p3.findall(contents)
        for x in res3:
            contents = contents.replace(x,chr(int(x[3:-1],16)))
    with open(topath,'w+') as fs:
        fs.write(contents)
    f.close()
    fs.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'DeJCE - JSP/JPSX CodeDecode')
    parser.add_argument('-i', '--infile', help = 'Need Decode JSP/JSPX File')
    parser.add_argument('-o', '--outfile',help = 'Save Decode JSP/JSPX File')
    args = parser.parse_args()
    if args.infile and args.outfile:
        try:
            decode(args.infile,args.outfile)
            logging.info("\033[1;36m Deocde Success !\033[0m")
        except Exception as e:
            logging.info("\033[1;31m "+ e +" \033[0m")
    else:
        logging.info("\033[1;31m Please -h ! \033[0m")