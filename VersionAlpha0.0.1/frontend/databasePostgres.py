import config
import psycopg2 as db

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

    #get ids for all the submissions for a single assignement
    def get_submissions_for(self, aid):
        self.cursor.execute(
            "SELECT \
                "+config.TABLE_SUBMISSIONS+".ID, \
                "+config.TABLE_USERS+".USERNAME, \
                "+config.TABLE_SUBMISSIONS+".NAME \
            FROM "+config.TABLE_SUBMISSIONS+" \
            INNER JOIN "+config.TABLE_USERS+" ON\
                "+config.TABLE_SUBMISSIONS+".USER_ID = "+config.TABLE_USERS+".ID\
            WHERE ASSIGN_ID = %(a)s ", {"a":aid})
        return self.cursor.fetchall()

    #get a single file from a submission
    def get_file(self, sid):
        print("getfile")
        print(sid)
        self.cursor.execute("SELECT name,data,language FROM "+config.TABLE_SUBMISSIONS+" WHERE id=%(a)s;",{"a":sid})
        return self.cursor.fetchone()

    #load an assignment into the database
    def put_file(self,theFile,name,language,assignID,userID):
        contents = theFile.read()
        #TODO:figure out if an assignment is late
        late = '0'
        self.cursor.execute("INSERT INTO "+config.TABLE_SUBMISSIONS+" (ASSIGN_ID, USER_ID, LATE, DATA, NAME, LANGUAGE) VALUES (%s,%s,%s,%s,%s,%s) RETURNING ID;",(assignID,userID,late,contents,name,language))
        id_of_new_row = self.cursor.fetchone()[0]
        self.connection.commit()
        return id_of_new_row

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
            "INSERT INTO " + config.TABLE_ASSOCIATIONS +"(document1, document2, index1, index2, similarity) VALUES (%(a)s, %(b)s, %(c)s, %(d)s, %(e)s) ",{"a":doc1ID, "b":doc2ID, "c":index1ID, "d":index2ID, "e":similarity}
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
        WHERE ass.document1=%(a)s OR ass.document2 = %(a)s;",{"a":fid})
        ret = self.cursor.fetchall()
        print(ret)
        return ret 

    def get_class_list(self):
        self.cursor.execute("SELECT ID,COURSECODE FROM " + config.TABLE_CLASSES + ";")
        ret = self.cursor.fetchall()
        return ret

    def get_offering_list(self, cid):
        self.cursor.execute("SELECT ID,SEMESTER FROM " + config.TABLE_OFFERINGS + " WHERE CLASS_ID=%(a)s;",{"a":cid})
        return self.cursor.fetchall()

    def get_assignment_list(self, oid):
        print(oid)
        self.cursor.execute("SELECT ID FROM " + config.TABLE_ASSIGNMENTS + " WHERE OFFERING_ID=%(a)s;",{"a":oid})
        return self.cursor.fetchall()

    def look_up_user_ID(self, uName):
        self.cursor.execute("SELECT ID FROM " + config.TABLE_USERS + " WHERE USERNAME = '" + uName + "';")
        return self.cursor.fetchone() 

    #close the database connection
    def close(self):
        self.cursor.close()
        self.connection.close()

    #deconstructor
    def __del__(self):
        self.close()