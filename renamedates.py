#!python3
# renamedates.py - Rename filenames with american MM-DD-YYYY date format
# to European DD-MM-YYYY
import shutil ,os, re
# create regex that matches  files with american date format
p=re.compile(r"""^(.*?) #all text before the date
((0|1)?\d)- # one or two digits for the month-
((0|1|2|3)?\d)-   #one or two digits for the day
((19|20)\d\d)  #four digits for the year
(.*?)$           #all text after the date
""",re.VERBOSE)

#todo :loop over the files in the working directory .
for fn in os.listdir("."):
    mo=p.search(fn)




#todo: skip files without a date.
    if mo==None:
        continue

#todo: get the different parts of the filename.
    bp=mo.group(1)
    mp=mo.group(2)
    dp=mo.group(4)
    yp=mo.group(6)
    ap=mo.group(8)

#todo: form the european-style filename.
    efn=bp+dp+"-"+mp+"-"+yp+ap
#todo:get the full absulate file path.
    wd=os.path.abspath(".")
    fn=os.path.join(wd,fn)
    efn=os.path.join(wd,efn)

#todo: rename the files.
    print('renaming "%s" to "%s"...' % (fn,efn))
    #shutil.move(fn,efn)
