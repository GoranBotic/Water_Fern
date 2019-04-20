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
        self.cursor = self.connection.cursor()

       
    #this method is used to record that the indexing of a submission is finished
    def finish_indexing(self, sid,iid):
        self.cursor.execute(
            "INSERT INTO " + config.TABLE_PROGRESS + " (SUBMISSION_ID, INDEXER_ID) VALUES (%(a)s, %(b)s);", {"a":sid, "b":iid}
            )
        self.connection.commit()

        

    #get ids for all the submissions for a single assignement
    def get_assignment(self, aid):
        self.cursor.execute("SELECT id FROM "+config.TABLE_SUBMISSIONS+";")
        return self.cursor.fetchall()

    #get a single file from a submission
    def get_file(self, sid):
        self.cursor.execute("SELECT name,data,language FROM "+config.TABLE_SUBMISSIONS+" WHERE id=%s;",(sid,))
        return self.cursor.fetchone()

    #get the assignment id for a submission 
    def get_assign_id(self, sID):
        self.cursor.execute(
            "SELECT ASSIGN_ID FROM " + config.TABLE_SUBMISSIONS + " WHERE ID = %(a)s;", {"a":sID}
        )
        return self.cursor.fetchone()

    #store an index vector for a subsection of a file
    def store_index(self, itype, submission_id, assignID, index, start_line=0, end_line=0):
        self.cursor.execute(
            "INSERT INTO "+config.TABLE_INDEXES+" (submission_id, assign_id, start_line, end_line, index, type) VALUES (%(a)s, %(b)s, %(c)s, %(d)s, %(e)s, %(f)s) ON CONFLICT ON CONSTRAINT "+config.TABLE_INDEXES+"_pkey DO UPDATE SET index=%(e)s RETURNING block_id;",
            {"a":submission_id, "b":assignID, "c":start_line, "d":end_line, "e":index, "f":itype}
        )
        id_of_new_row = self.cursor.fetchone()[0]
        self.connection.commit()
        return id_of_new_row

    def find_cosine_similar_indicies(self, itype, index, sID, aID):
        
        print(aID)
        LIMITSKIP = 0
        LIMITPERDIM = 25

        perpendicularValues = []

      
        cmd = ""

        for i in range(len(index)):
            low = index[i] - 0.001
            high = index[i] + 0.001

            cmd += "(SELECT submission_id, block_id, index \
                FROM " + config.TABLE_INDEXES + " \
                WHERE assign_id = " + str(aID) + " AND \
                    type = '" + itype + "' AND \
                    (index[ " + str(i+1) + " ] >= " + str(low) + " AND \
                    index[ " + str(i+1) + " ] <= " + str(high) + ") AND \
                    submission_id != " + str(sID) + " \
                    ORDER BY ABS(" + str(index[i]) + " - index[ " + str(i+1) + " ])"

            cmd += " OFFSET " + str(LIMITSKIP) + " LIMIT " + str(LIMITPERDIM) + ")"

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

    #close the database connection
    def close(self):
        self.cursor.close()
        self.connection.close()

    #deconstructor
    def __del__(self):
        self.close()