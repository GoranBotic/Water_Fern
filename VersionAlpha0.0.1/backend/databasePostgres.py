import config
import psycopg2 as db

#TODO: does not have everything nessicary 
#TODO: Most other functions
#TODO: Make ALL this resiliant to disconnects
class DatabaseManager:
    def __init__(self):
        #Connect to database
        #TODO: add asymetric key auth
        #TODO: make the database being connected to dynamic based on the frontend request
        self.connection = db.connect(
            host        =   config.POSTGRES_ADDRESS,
            port        =   config.POSTGRES_PORT,
            database    =   config.POSTGRES_DB,
            user        =   config.POSTGRES_USER,
            password    =   config.POSTGRES_PASS
        ) 

        #Generate cursor
        self.cursor = self.connection.cursor()

        

    #get ids for all the submissions for a single assignement
    # def get_assignment(self, aid):
    #     self.cursor.execute("SELECT ID FROM "+config.TABLE_SUBMISSIONS+";")
    #     return self.cursor.fetchall()

    #get a single file from a submission
    def get_file(self, sid):
        self.cursor.execute("SELECT NAME, DATA, LANGUAGE FROM "+config.TABLE_SUBMISSIONS+" WHERE id=%s;",(sid,))
        return self.cursor.fetchone()

    #store an index vector for a subsection of a file
    def store_index(self, itype, submission_id, index, start_line=0, end_line=0):
        self.cursor.execute(
            "INSERT INTO "+config.TABLE_INDEXES+" (SUBMISSION_ID, START_LINE, END_LINE, TYPE, INDEX) VALUES (%(a)s, %(b)s, %(c)s, %(d)s, %(e)s) ON CONFLICT ON CONSTRAINT "+config.TABLE_INDEXES+"_pkey DO UPDATE SET index=%(e)s RETURNING block_id;",
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

            # if index[i] <= perpendicularValues[i]:
            #     low = index[i] 
            #     high = perpendicularValues[i]
            # else:
            #     high = index[i] 
            #     low = perpendicularValues[i]
            low = index[i] - 0.01
            high = index[i] + 0.01

            cmd += "(SELECT SUBMISSION_ID, BLOCK_ID, INDEX FROM " + config.TABLE_INDEXES + " WHERE TYPE = '" + itype + "' AND (INDEX[ " + str(i+1) + " ] >= " + str(low) + " AND INDEX[ " + str(i+1) + " ] <= " + str(high) + ") ORDER BY ABS(" + str(index[i]) + " - INDEX[ " + str(i+1) + " ]) "

            # if perpendicularValues[i] < index[i]:
            #     cmd += "DESC"

            cmd += " LIMIT " + str(LIMITPERDIM) + ")"

            if i < len(index)-1:
               cmd += " INTERSECT "
        cmd += ";"


        ##FIXME
        #cmd = "SELECT submission_id, block_id, index FROM " + config.TABLE_INDEXES + ";"
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
            "INSERT INTO " + config.TABLE_ASSOCIATIONS +"(DOCUMENT1, DOCUMENT2, INDEX1, INDEX2, SIMILARITY) VALUES (%(a)s, %(b)s, %(c)s, %(d)s, %(e)s) ",{"a":doc1ID, "b":doc2ID, "c":index1ID, "d":index2ID, "e":similarity}
        )
        self.connection.commit()

    #close the database connection
    def close(self):
        self.cursor.close()
        self.connection.close()

    #deconstructor
    def __del__(self):
        self.close()