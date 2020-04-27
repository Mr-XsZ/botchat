import os

w = '\x1b[1;37m'
g = '\x1b[1;32m'
y = '\x1b[1;33m'

def banner():
 os.system('clear')
 print(f'''
            {w}[{g}     Author : {w}sCuby07     ]
        [   {g}Fungsi : {w}Bot Chat {g}({w}SimSimi{g}){w}   ]
        _____________________________________{y}
                    Version 0.4
''')
