import sqlite3
import os

class DB:
    def __init__(self, DBName):
        self.dims = 5
        needInit = False
        if not os.path.exists(DBName):
            needInit = True

        self.DB = sqlite3.connect(DBName)
        self.c = self.DB.cursor() 

        if needInit:
            cmd = "CREATE TABLE blocks ("
            for v in range(self.dims):
                cmd += ("v" + str(v) +" real, ")
            
            cmd += "fileID integer, line integer, length integer)" 

            self.c.execute(cmd)

            cmd = ""
            cmd += "CREATE TABLE rawFiles (id integer primary key autoincrement, theFile blob)"
            self.c.execute(cmd)

            self.DB.commit()
            

    def shutdown(self):
        self.DB.close()   

    def putFile(self, srcFile):
        #print(srcFile)
        self.c.execute("INSERT INTO rawFiles VALUES (NULL,'"+srcFile.encode('hex')+"')")
        ret = self.c.execute("SELECT last_insert_rowid()")
        self.DB.commit()
        return next(ret)

    def putBlock(self, vect, fileID, line, length):
        cmd = "INSERT INTO blocks VALUES ("
        for v in vect:
            cmd += (str(v) + ", ")
        cmd += str(fileID) + ", "
        cmd += str(line) + ", "
        cmd +=  str(length) + ")"
        self.c.execute(cmd) 
        self.DB.commit()


# data = DB("test.db")

# ID1 = data.putFile("abcdefg")
# ID2 = data.putFile("12345")

# data.putBlock([1,2,3,4,5,6,7,8,9], 0, 0, 2)

# print(ID1)
# print(ID2)

# for r in data.c.execute("SELECT * FROM rawFiles"):
#     print(r)

# for r in data.c.execute("SELECT * FROM blocks"):
#     print(r)

# data.shutdown()
