#Tocas 2 Auto Update System
#written by Toby Chui
#因為該死的洨安隨便的把 tocas.min.css 移除了為了方便所有用了 tocas 2 min 版的用家，推出這個自動更新程式。
#輸入你要更改的 資料夾，本程式會自動更新 php 或 html 裡面的所有 tocasui 連接到最新版本。
from tempfile import mkstemp
from shutil import move
from os import close, remove
import os
webdir = '' #這裡填入網站的路徑
old_css = '<link rel="stylesheet" href="//cdn.rawgit.com/TeaMeow/TocasUI/master/dist/tocas.min.css">'
newcss = '<link rel="stylesheet" href="//cdn.rawgit.com/TeaMeow/TocasUI/2.3.1/dist/tocas.css">'
def main():
    directory = webdir
    for filename in os.listdir(directory ):
        if filename.endswith(".html") or filename.endswith(".php"): 
             print(os.path.join(directory, filename))
             replace(directory + filename,old_css,newcss)
             continue
        else:
             continue
    print("Update Finished.\n")
    print("2016 始春\n")
def replace(file_path, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    with open(abs_path,'w',encoding = 'utf8') as new_file:
        with open(file_path,encoding = 'utf8') as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    close(fh)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)
    
main()
