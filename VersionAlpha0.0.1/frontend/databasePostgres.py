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
        self.cursor.execute("SELECT USER_ID, NAME, ID FROM "+config.TABLE_SUBMISSIONS+" WHERE ASSIGN_ID = %(a)s;", {"a":aid})
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

    def find_cosine_similar_indicies(self, itype, index):
        total = sum([v**2 for v in index])
 
        LIMITPERDIM = 50

        perpendicularValues = []

        for v in index:
            perpendicularValues.append((-total-(v**2))/v)

        cmd = ""

        for i in range(len(index)):
            low = index[i] - 0.01
            high = index[i] + 0.01

            cmd += "(SELECT submission_id, block_id, index FROM " + config.TABLE_INDEXES + " WHERE type = '" + itype + "' AND (index[ " + str(i+1) + " ] >= " + str(low) + " AND index[ " + str(i+1) + " ] <= " + str(high) + ") ORDER BY ABS(" + str(index[i]) + " - index[ " + str(i+1) + " ]) "

            cmd += " LIMIT " + str(LIMITPERDIM) + ")"

            if i < len(index)-1:
               cmd += " INTERSECT "
        cmd += ";"

        self.cursor.execute(cmd) 
        return self.cursor.fetchall()

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
        #TODO this should return lineStartFile1, lineEndfile1, file2ID, lineStartFile2, lineEndfile2, score 
        self.cursor.execute("SELECT document1, document2, index1, index2, similarity FROM "+config.TABLE_ASSOCIATIONS+" WHERE document1=%(a)s OR document2 = %(a)s;",{"a":fid})
        return self.cursor.fetchall()

    def list_students_who_submitted(self, aid):
        self.cursor.execute("SELECT USER_ID FROM "+config.TABLE_SUBMISSIONS+" WHERE ASSIGN_ID=%s",(aid,))
        return self.cursor.fetchall()

    def get_assignment_list(self, oid):
        print(oid)
        self.cursor.execute("SELECT ID FROM " + config.TABLE_ASSIGNMENTS + " WHERE OFFERING_ID=%(a)s;",{"a":oid})
        return self.cursor.fetchall()

    #close the database connection
    def close(self):
        self.cursor.close()
        self.connection.close()

    #deconstructor
    def __del__(self):
        self.close()