import config
import psycopg2 as db
import datetime

#fun garbage because psycopg2 returns a weird format when querying "Numeric" columns
DEC2FLOAT = db.extensions.new_type(
    db.extensions.DECIMAL.values,
    'DEC2FLOAT',
    lambda value, curs: float(value) if value is not None else None)
db.extensions.register_type(DEC2FLOAT)

#A simple test database manager, does not have everything nessicary for MVP
#TODO: THis entire this needs to be re-written from scratch once we have the database proper
#TODO: Most other functions
#TODO: Make ALL this resiliant to disconnects
class DatabaseManager:
    def __init__(self):
        #Connect to database
        #TODO: add asymetric key auth
        self.connection = db.connect(
            host        =   config.POSTGRES_ADDRESS,
            port        =   config.POSTGRES_PORT,
            database    =   config.POSTGRES_DB,
            user        =   config.POSTGRES_USER,
            password    =   config.POSTGRES_PASS
        ) 

        #Generate cursor
        print("setting cursor")
        self.cursor = self.connection.cursor()

    def addUser(self, id, password):
        self.cursor.execute(
            "INSERT INTO "+config.TABLE_USERS+" (USERNAME,PASSWORD) SELECT %(a)s, crypt(%(p)s,gen_salt('md5'))\
            WHERE NOT EXISTS (SELECT (USERNAME, PASSWORD) FROM "+config.TABLE_USERS+" WHERE USERNAME=%(a)s);",{"a":id,"p":password})
        self.connection.commit()



    def validateUser(self, id, password):
        self.cursor.execute(
            "SELECT PASSWORD = crypt(%(a)s, PASSWORD) FROM " + config.TABLE_USERS + " WHERE USERNAME = %(b)s;", {"a":password,"b":id}
        )
        return self.cursor.fetchall()

    #get ids for all the submissions for a single assignement
    def get_submissions_for(self, aid):
        self.cursor.execute(
            "SELECT \
                "+config.TABLE_SUBMISSIONS+".ID, \
                "+config.TABLE_USERS+".USERNAME, \
                "+config.TABLE_SUBMISSIONS+".NAME, \
                ("+config.TABLE_SUBMISSIONS+".SIMILARITY/"+config.TABLE_SUBMISSIONS+".ASSOCIATIONCOUNT) as scr\
            FROM "+config.TABLE_SUBMISSIONS+" \
            INNER JOIN "+config.TABLE_USERS+" ON\
                "+config.TABLE_SUBMISSIONS+".USER_ID = "+config.TABLE_USERS+".ID\
            WHERE ASSIGN_ID = %(a)s \
            ORDER BY scr DESC", {"a":aid})
        return self.cursor.fetchall()

    #generate a student if they dont exist already
    def gen_student(self, uid):
        self.cursor.execute("INSERT INTO "+config.TABLE_USERS+" (USERNAME,PASSWORD) SELECT %(a)s, %(p)s \
            WHERE NOT EXISTS (SELECT (USERNAME,PASSWORD) FROM "+config.TABLE_USERS+" WHERE USERNAME=%(a)s)",{"a":uid,"p":"pass"})
        self.connection.commit()
        return 

    #get a single file from a submission
    def get_file(self, sid):
        print("getfile")
        print(sid)
        self.cursor.execute("SELECT name,data,language FROM "+config.TABLE_SUBMISSIONS+" WHERE id=%(a)s;",{"a":sid})
        return self.cursor.fetchone()

    #load an assignment into the database
    def put_file(self,theFile,name,language,assignID,userID):
        contents = theFile.read()
        length = contents.decode("utf-8").count("\n")
        #TODO:figure out if an assignment is late
        late = '0'
        self.cursor.execute("INSERT INTO "+config.TABLE_SUBMISSIONS+" (ASSIGN_ID, USER_ID, LATE, DATA, NAME, LENGTH, LANGUAGE) VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING ID;",(assignID,userID,late,contents,name,length,language))
        id_of_new_row = self.cursor.fetchone()[0]
        self.connection.commit()
        return id_of_new_row

    #find the progress of indexing of a set of files
    #WARNING: EXTREMELY SLOW
    def find_progress(self,assign_id):

        n_indexers = 1 #TODO: query number of indexers
        # "+config.TABLE_SUBMISSIONS+".LENGTH, \
        # self.cursor.execute("\
        # SELECT \
        #     MAX(CAST(("+ config.TABLE_INDEXES +".END_LINE - "+ config.TABLE_INDEXES +".START_LINE) AS REAL) / CAST("+config.TABLE_SUBMISSIONS+".LENGTH AS REAL)),\
        #     "+ config.TABLE_INDEXES +".TYPE,\
        #     "+ config.TABLE_INDEXES +".SUBMISSION_ID\
        # FROM "+ config.TABLE_INDEXES +"\
        # INNER JOIN "+config.TABLE_SUBMISSIONS+" ON\
        #     "+config.TABLE_INDEXES+".SUBMISSION_ID = "+config.TABLE_SUBMISSIONS+".ID\
        # WHERE "+config.TABLE_SUBMISSIONS+".ASSIGN_ID = %s \
        # GROUP BY \
        #     "+ config.TABLE_INDEXES +".TYPE,\
        #     "+ config.TABLE_INDEXES +".SUBMISSION_ID\
        # ;",(assign_id,))
        # rows = self.cursor.fetchall()

        # self.cursor.execute("\
        # SELECT \
        #     COUNT(ID)\
        # FROM "+config.TABLE_SUBMISSIONS+"\
        # WHERE ASSIGN_ID = %s",(assign_id,))
        # count = self.cursor.fetchone()[0]

        # if(len(rows)>0):
        #     avg = sum(list(zip(*rows))[0])/(count*n_indexers)
        #     return (avg/0.15)
        # else:
        #     return 1

        print(assign_id)
        self.cursor.execute("\
        SELECT \
            COUNT(ID)\
        FROM "+config.TABLE_SUBMISSIONS+"\
        WHERE ASSIGN_ID = %s",(assign_id,))
        total = self.cursor.fetchone()[0]*n_indexers

        self.cursor.execute(
            "SELECT COUNT(ID) FROM " + config.TABLE_SUBMISSIONS + "\
                INNER JOIN " + config.TABLE_PROGRESS + " ON \
                    " + config.TABLE_SUBMISSIONS + ".ID = " + config.TABLE_PROGRESS + ".SUBMISSION_ID\
                WHERE ASSIGN_ID = %(a)s;\
            ", {"a":assign_id}
        )

        finished = self.cursor.fetchone()[0]

        return finished/total 

    #store an index vector for a subsection of a file
    def store_index(self, itype, submission_id, index, start_line=0, end_line=0):
        self.cursor.execute(
            "INSERT INTO "+config.TABLE_INDEXES+" (submission_id, start_line, end_line, type, index) VALUES (%(a)s, %(b)s, %(c)s, %(d)s, %(e)s) ON CONFLICT ON CONSTRAINT "+config.TABLE_INDEXES+"_pkey DO UPDATE SET index=%(e)s RETURNING block_id;",
            {"a":submission_id, "b":start_line, "c":end_line, "d":itype, "e":index}
        )
        id_of_new_row = self.cursor.fetchone()[0]
        self.connection.commit()
        return id_of_new_row

    # def find_cosine_similar_indicies(self, itype, index):
    #     LIMITPERDIM = 300

    #     perpendicularValues = []

    #     cmd = ""

    #     for i in range(len(index)):
    #         #low = index[i] - 0.3
    #         #high = index[i] + 0.3
         

    #         cmd += "(SELECT submission_id, block_id, index FROM " + config.TABLE_INDEXES + " WHERE type = '" + itype + "' AND (index[ " + str(i+1) + " ] >= " + str(low) + " AND index[ " + str(i+1) + " ] <= " + str(high) + ") ORDER BY ABS(" + str(index[i]) + " - index[ " + str(i+1) + " ]) "

    #         cmd += " LIMIT " + str(LIMITPERDIM) + ")"

    #         if i < len(index)-1:
    #            cmd += " INTERSECT "
    #     cmd += ";"

    #     self.cursor.execute(cmd) 
    #     return self.cursor.fetchall()

    def associate_indicies(self, doc1ID, doc2ID, index1ID, index2ID, similarity):
        if doc1ID > doc2ID:
            tmp = doc1ID
            doc1ID = doc2ID
            doc2ID = tmp
        if index1ID > index2ID:
            tmp = index1ID
            index1ID = index2ID
            index2ID = tmp 
        
        self.cursor.execute(
            "INSERT INTO "+ config.TABLE_ASSOCIATIONS +"(document1, document2, index1, index2, similarity) VALUES (%(a)s, %(b)s, %(c)s, %(d)s, %(e)s) ",{"a":doc1ID, "b":doc2ID, "c":index1ID, "d":index2ID, "e":similarity}
        )
        self.connection.commit()

    def get_associations(self, fid):
        self.cursor.execute("SELECT \
            ass.document1, \
            ass.document2, \
            ind1.start_line,\
            ind1.end_line, \
            ind2.start_line,\
            ind2.end_line, \
            similarity \
        FROM "+config.TABLE_ASSOCIATIONS+" ass\
        INNER JOIN "+config.TABLE_INDEXES+" ind1 ON ind1.block_id = ass.index1\
        INNER JOIN "+config.TABLE_INDEXES+" ind2 ON ind2.block_id = ass.index2\
        WHERE ass.document1=%(a)s OR ass.document2 = %(a)s ORDER BY similarity DESC;",{"a":fid})
        ret = self.cursor.fetchall()
        print(ret)
        return ret 

    def get_class_list(self):
        self.cursor.execute("SELECT ID,COURSECODE FROM " + config.TABLE_CLASSES + ";")
        ret = self.cursor.fetchall()
        return ret

    def get_offering_list(self, cid,uid):
        self.cursor.execute("SELECT ID,SEMESTER FROM " + config.TABLE_OFFERINGS + "," + config.TABLE_OFFERING_OWNERS +" WHERE "+ config.TABLE_OFFERINGS +".CLASS_ID=%(a)s and " + config.TABLE_OFFERING_OWNERS +".OFFERINGID=" + config.TABLE_OFFERINGS + ".ID and " + config.TABLE_OFFERING_OWNERS +".USERID=%(b)s;",{"a":cid,"b":uid})
        return self.cursor.fetchall()

    def get_assignment_list(self, oid):
        print(oid)
        self.cursor.execute("SELECT ID FROM " + config.TABLE_ASSIGNMENTS + " WHERE OFFERING_ID=%(a)s;",{"a":oid})
        return self.cursor.fetchall()

    def look_up_user_ID(self, uName, generate_if_missing):
        if(generate_if_missing):
            self.gen_student(uName)
        self.cursor.execute("SELECT ID FROM " + config.TABLE_USERS + " WHERE USERNAME = '" + uName + "';")
        return self.cursor.fetchone() 

    def make_class(self, cid):
        self.cursor.execute("SELECT * FROM " + config.TABLE_CLASSES+ " WHERE COURSECODE = '" + cid + "';")
        ret = self.cursor.fetchall()
        print(ret)
        if len(ret) == 0:
            self.cursor.execute("INSERT INTO "+ config.TABLE_CLASSES +"(COURSECODE) VALUES (%(a)s) ",{"a":cid})
            self.connection.commit()
            return True
        else:
            return False

    def own_offering(self, oid, uid):
        self.cursor.execute(
            "INSERT INTO " + config.TABLE_OFFERING_OWNERS + " (USERID, OFFERINGID) VALUES (%(a)s, %(b)s);", {"a":uid, "b":oid})
        self.connection.commit()
        return True 

    def make_offering(self, cid):
        self.cursor.execute("INSERT INTO "+ config.TABLE_OFFERINGS +"(CLASS_ID,SEMESTER,DONE) VALUES (%(a)s,%(b)s,%(c)s) RETURNING ID;",{"a":cid,"b":datetime.datetime.today(),"c":0})
        id_of_new_row = self.cursor.fetchone()[0]
        self.connection.commit()
        
        return id_of_new_row

    def make_assignment(self, oid):
        self.cursor.execute("INSERT INTO "+ config.TABLE_ASSIGNMENTS +"(OFFERING_ID,OPENING,CLOSE) VALUES (%(a)s,%(b)s,%(c)s) ",{"a":oid,"b":datetime.datetime.today(),"c":datetime.datetime.today()})
        self.connection.commit()
        return True

    #close the database connection
    def close(self):
        self.cursor.close()
        self.connection.close()

    #deconstructor
    def __del__(self):
        self.close()