import os
pathtolookfor = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'corporations'))

# This will create a allhosts.txt file under the "merge_all" folder:
# merge_all/allhosts.txt

# Clean the file first so it doesn't get appended
def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()

with open("allhosts.txt", "w") as txt:
    deleteContent(txt)

# Open each file
for file in os.listdir(pathtolookfor):
    if file.endswith("txt"):
        print(f'Read {file}')
        with open(f'{pathtolookfor}/{file}', "r") as fi:
            for ln in fi:
                if ln.startswith("0.0.0.0"):
                    with open("allhosts.txt", "a") as rs:
                        rs.write(f'{ln}')
                        
