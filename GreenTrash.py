import os
from datetime import date, time, datetime
import datetime

# Configuration
number_of_days      = 3                                             # you can change this           
number_of_commits   = 10                                            # you can change this
repositories        = "https://github.com/riecho14/Green-Trash.git" # you can change this

NoD = number_of_days
ctr = 1
now = datetime.datetime.now()

f = open("GreenTrash.txt", "w")
os.system("git config user.name")
os.system("git config user.email")
os.system("git init")

pointer = 0

# Loop through the number of days
while NoD > 0:
    NoC = number_of_commits
    while NoC > 0:
        f           = open("GreenTrash.txt", "a+")
        x_date      = now + datetime.timedelta(days=-pointer)
        formatdate  = x_date.strftime("%Y-%m-%d")
        f.write(f"Commit ke {ctr}: {formatdate}\n")
        f.close()
        os.system("git add .")
        os.system(f"git commit --date=\"{formatdate} 12:15:10\" -m \"Commit ke {ctr}\"")
        print(f"Commit ke {ctr}: {formatdate}")
        NoC -= 1
        ctr += 1
    pointer += 1
    NoD     -= 1

# Logic for the commit
os.system(f"git remote add origin {repositories}")
os.system("git branch -M main")
os.system("git push -u origin main -f")