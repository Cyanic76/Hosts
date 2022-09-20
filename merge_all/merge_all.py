import os

pathtolookfor = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'corporations'))
tries = 0

def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()

# Clean the file first so it doesn't get appended
with open("allhosts.txt", "w") as txt:
    deleteContent(txt)

# Open each file
for file in os.listdir(pathtolookfor):
    if file.endswith("txt") and not file.startswith("folderlist") and tries == 0:
        print(f'{file}')
        with open(f'{pathtolookfor}/{file}', "r") as fi:
            for ln in fi:
                if ln.startswith("0.0.0.0"):
                    with open("allhosts.txt", "a") as rs:
                        rs.write(f'{ln}')
                        
