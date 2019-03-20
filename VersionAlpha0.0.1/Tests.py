import requests 
import unittest 
import time 
from testing import config
import psycopg2 as db
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class TestFlatZipSubmission(unittest.TestCase):
    con = None
    cur = None
    @classmethod
    def setUpClass(cls):
        #connect to the DB to verify that indexing occured as expected 
        cls.con = db.connect(
            host        =   config.POSTGRES_ADDRESS,
            port        =   config.POSTGRES_PORT,
            database    =   config.POSTGRES_DB,
            user        =   config.POSTGRES_USER,
            password    =   config.POSTGRES_PASS
        ) 
        cls.cur = cls.con.cursor()

        #clean the DB just in case
        cls.cur.execute("DELETE FROM " + config.TABLE_ASSOCIATIONS + ";")
        cls.con.commit()
        cls.cur.execute("DELETE FROM " + config.TABLE_INDEXES + ";")
        cls.con.commit()
        cls.cur.execute("DELETE FROM " + config.TABLE_SUBMISSIONS + ";")
        cls.con.commit()

        #post to the backend server and wait for the files to be indexed 
        r = None
        with open('testing/flatZip.zip', 'rb') as f:
            r = requests.post('https://0.0.0.0:8001/api/v1/uploadsubmission', files={'file': f}, data={'uID':0, 'aID':0}, verify=False)

        cls.assertTrue(r.status_code == 200, "Failed to post file")

        time.sleep(30) 

    @classmethod
    def tearDownClass(cls):
        cls.cur.execute("DELETE FROM " + config.TABLE_ASSOCIATIONS + ";")
        cls.con.commit()
        cls.cur.execute("DELETE FROM " + config.TABLE_INDEXES + ";")
        cls.con.commit()
        cls.cur.execute("DELETE FROM " + config.TABLE_SUBMISSIONS + ";")
        cls.con.commit()
        cls.cur.close()
        cls.con.close()

    def test_submissions_were_stored(self):
        """Testing that the submit files from the flat zip were stored in the DB"""

        self.cur.execute("SELECT COUNT(*) FROM " + config.TABLE_SUBMISSIONS + ";")
        totalSubmissions = self.cur.fetchall()[0][0]

        self.assertTrue(totalSubmissions == 2, "not all files were stored in the data base")

    def test_indexes_were_generated(self):
        """Testing that indexes were generated on each file from the flat zip"""
        self.cur.execute("SELECT COUNT(*) FROM " + config.TABLE_INDEXES + " GROUP BY SUBMISSION_ID;") 

        totals = self.cur.fetchall() 

        for r in totals:
            self.assertTrue(r[0] > 0, "Indexers were not generated for all documents.")

    def test_associations_were_found(self):
        """Testing that associations between the submit files from the flat zip were stored in the DB"""
        self.cur.execute("SELECT count(submissions.id) from " + config.TABLE_ASSOCIATIONS + ", " + config.TABLE_SUBMISSIONS + " WHERE submissions.ID = document1 or submissions.ID = document2 GROUP BY submissions.id;")
        totals = self.cur.fetchall()

        for r in totals:
            self.assertTrue(r[0] > 0, "Associations were not generated for all documents.")

    def test_getAssociations_rejects_malformed_requests(self):
        "Testing to ensure that the endpoint for retrieving associations rejects malformed requests."""
        r = requests.post('https://0.0.0.0:8001/api/v1/getAssociations' , data={'fsdfID':0}, verify=False)

        self.assertTrue(r.status_code == 400, "getAssociations should have rejected the malformed request")

    def test_associations_can_be_retrieved(self):
        "Testing to ensure that found associations can be retrieved."""
        r = requests.post('https://0.0.0.0:8001/api/v1/getAssociations' , data={'fID':0}, verify=False)

        self.assertTrue(r.status_code == 200, "Response from getAssociations was not 200")
        self.assertTrue(len(r.content) > 0, "No associations were retrieved")

    def test_get_submissions_for_assignment(self):
        """Geting submissions from the flat zip"""
        r = requests.post('https://0.0.0.0:8001/api/v1/getSubmissionsList', verify=False, allow_redirects=False, data= {'assignmentID':0})

        ar = r.json() 
        
       
        self.assertTrue(len(ar) == 2, "There should be 2 submissions to the assingment with id 0")

    def test_get_assignment_list_malformed_input(self):
        """Testing for malformed input after submission from the flat zip"""
        r = requests.post('https://0.0.0.0:8001/api/v1/getSubmissionsList', verify=False, allow_redirects=False, data= {'offegID':0})

        self.assertTrue(r.status_code == 400, "getsubmissionsList failed to detect malformed input.")

    def test_get_submissions_for_assignment(self):
        """Geting submission with id 1 from the flat zip"""
        r = requests.post('https://0.0.0.0:8001/api/v1/getSubmission', verify=False, allow_redirects=False, data= {'submissionID':1})

        ar = r.json()
        
       
        self.assertTrue(len(ar) == 3, "A single submission should be returned " + str(ar))

    def test_get_assignment_list_malformed_input(self):
        """Testing for malformed input to getSubmission after submit from the flat zip"""
        r = requests.post('https://0.0.0.0:8001/api/v1/getSubmission', verify=False, allow_redirects=False, data= {'offegID':0})

        self.assertTrue(r.status_code == 400, "getSubmission failed to detect malformed input.")

    

class TestNonFlatZipSubmission(unittest.TestCase):
    con = None
    cur = None
    @classmethod
    def setUpClass(cls):
        #connect to the DB to verify that indexing occured as expected 
        cls.con = db.connect(
            host        =   config.POSTGRES_ADDRESS,
            port        =   config.POSTGRES_PORT,
            database    =   config.POSTGRES_DB,
            user        =   config.POSTGRES_USER,
            password    =   config.POSTGRES_PASS
        ) 
        cls.cur = cls.con.cursor()

        #Clean the DB just in case
        cls.cur.execute("DELETE FROM " + config.TABLE_ASSOCIATIONS + ";")
        cls.con.commit()
        cls.cur.execute("DELETE FROM " + config.TABLE_INDEXES + ";")
        cls.con.commit()
        cls.cur.execute("DELETE FROM " + config.TABLE_SUBMISSIONS + ";")
        cls.con.commit()
        
        #post to the backend server and wait for the files to be indexed 
        r = None
        with open('testing/nonFlatZip.zip', 'rb') as f:
            r = requests.post('https://0.0.0.0:8001/api/v1/uploadsubmission', files={'file': f}, data={'uID':0, 'aID':0}, verify=False)

        cls.assertTrue(r.status_code == 200, "Failed to post file")

        time.sleep(30) 

    @classmethod
    def tearDownClass(cls):
        cls.cur.execute("DELETE FROM " + config.TABLE_ASSOCIATIONS + ";")
        cls.con.commit()
        cls.cur.execute("DELETE FROM " + config.TABLE_INDEXES + ";")
        cls.con.commit()
        cls.cur.execute("DELETE FROM " + config.TABLE_SUBMISSIONS + ";")
        cls.con.commit()
        cls.cur.close()
        cls.con.close()

    def test_submissions_were_stored(self):
        """Testing that the submit files from the non-flat zip were stored in the DB"""

        self.cur.execute("SELECT COUNT(*) FROM " + config.TABLE_SUBMISSIONS + ";")
        totalSubmissions = self.cur.fetchall()[0][0]

        self.assertTrue(totalSubmissions == 2, "There should be 2 submissions in the DB not " + str(totalSubmissions))

    def test_indexers_were_generated(self):
        """Testing that indexes were generated on each file from the non-flat zip """
        self.cur.execute("SELECT COUNT(*) FROM " + config.TABLE_INDEXES + " GROUP BY SUBMISSION_ID;") 

        totals = self.cur.fetchall() 

        for r in totals:
            self.assertTrue(r[0] > 0, "Indexers were not generated for all documents.")

    def test_associations_were_found(self):
        """Testing that associations between the submit files were stored in the DB"""
        self.cur.execute("SELECT count(submissions.id) from " + config.TABLE_ASSOCIATIONS + ", " + config.TABLE_SUBMISSIONS + " WHERE submissions.ID = document1 or submissions.ID = document2 GROUP BY submissions.id;")
        totals = self.cur.fetchall()

        for r in totals:
            self.assertTrue(r[0] > 0, "Associations were not generated for all documents.")

    def test_getAssociations_rejects_malformed_requests(self):
        "Testing to ensure that the endpoint for retrieving associations rejects malformed requests."""
        r = requests.post('https://0.0.0.0:8001/api/v1/getAssociations' , data={'fsdfID':0}, verify=False)

        self.assertTrue(r.status_code == 400, "getAssociations should have rejected the malformed request")

    def test_associations_can_be_retrieved(self):
        "Testing to ensure that found associations can be retrieved. After submission from the non-flat zip """
        r = requests.post('https://0.0.0.0:8001/api/v1/getAssociations' , data={'fID':0}, verify=False)

        self.assertTrue(r.status_code == 200, "Response from getAssociations was not 200")
        self.assertTrue(len(r.content) > 0, "No associations were retrieved")

    def test_get_submissions_for_assignment(self):
        """Getting submissions from the endpoint after submission from the non-flat zip """
        r = requests.post('https://0.0.0.0:8001/api/v1/getSubmissionsList', verify=False, allow_redirects=False, data= {'assignmentID':0})

        ar = r.json() 
        
       
        self.assertTrue(len(ar) == 2, "There should be 2 submissions to the assingment with id 0 not " + str(len(ar)))

    def test_get_assignment_list_malformed_input(self):
        r = requests.post('https://0.0.0.0:8001/api/v1/getSubmissionsList', verify=False, allow_redirects=False, data= {'offegID':0})

        self.assertTrue(r.status_code == 400, "getsubmissionsList failed to detect malformed input.")

    def test_get_submissions_for_assignment(self):
        """Geting submission with id 1 from the non-flat zip"""
        r = requests.post('https://0.0.0.0:8001/api/v1/getSubmission', verify=False, allow_redirects=False, data= {'submissionID':3})

        ar = r.json() 
        
       
        self.assertTrue(len(ar) == 3, "A single submission should be returned")

    def test_get_assignment_list_malformed_input(self):
        """Testing for malformed input to the getSubmission page"""
        r = requests.post('https://0.0.0.0:8001/api/v1/getSubmission', verify=False, allow_redirects=False, data= {'offegID':0})

        self.assertTrue(r.status_code == 400, "getSubmission failed to detect malformed input.")

class TestSubmissionOfBrokenCode(unittest.TestCase):
    
    def test_missing_assignment_ID_field(cls):
        #post to the backend server and wait for the files to be indexed 
        r = None
        with open('testing/brokenCode.zip', 'rb') as f:
            r = requests.post('https://0.0.0.0:8001/api/v1/uploadsubmission', files={'file': f}, data={'uID':0}, verify=False)

        cls.assertTrue(r.status_code == 400, "Missing field aID should have been detected")

    def test_missing_user_ID_field(cls):
        with open('testing/brokenCode.zip', 'rb') as f:
            r = requests.post('https://0.0.0.0:8001/api/v1/uploadsubmission', files={'file': f}, data={'aID':0}, verify=False)

        cls.assertTrue(r.status_code == 400, "Missing field uID should have been detected")

    def test_invalid_source_code_java(cls):
        with open('testing/brokenCode.zip', 'rb') as f:
            r = requests.post('https://0.0.0.0:8001/api/v1/uploadsubmission', files={'file': f}, data={'uID':0, 'aID':0}, verify=False)

        cls.assertTrue(str(r.content).find("Invalid Code") != -1, "Invalid code should have been detected")


class TestVisitingFrontEnd(unittest.TestCase):
    
    def test_https_redirect(cls): 
        r = requests.get('http://0.0.0.0:8000', verify=False, allow_redirects=False)

        cls.assertTrue(r.status_code == 301, "http on port 80 should redirect to https on port 443")

    def test_get_list_of_classes(self):
        r = requests.post('https://0.0.0.0:8001/api/v1/getClassList', verify=False, allow_redirects=False)

        ar = r.json() 
        memes = None
        for row in ar:
            if row[0] == 0:
                memes = row[1]
        self.assertTrue(memes == "memes123", "The course with ID 0 shoud be called memes123")

    def test_get_offerings(self):
        r = requests.post('https://0.0.0.0:8001/api/v1/getOfferingList', verify=False, allow_redirects=False, data= {'classID':0})

        ar = r.json() 
        date = None
        count = 0
        for row in ar:
            if row[0] == 0:
                count += 1
                date = row[1]
       
        self.assertTrue(count == 1, "There should be only one offering of the class with id 0")
        self.assertTrue(date == "Sun, 01 Jan 2017 00:00:00 GMT", "The offering of class with ID 0 should start on Sunday, January 1, 2017")

    def test_get_offerings(self):
        r = requests.post('https://0.0.0.0:8001/api/v1/getOfferingList', verify=False, allow_redirects=False, data= {'clasdsID':0})

        self.assertTrue(r.status_code == 400, "getOfferingList failed to detect malformed input.")


    def test_get_assignment_list(self):
        r = requests.post('https://0.0.0.0:8001/api/v1/getAssignmentList', verify=False, allow_redirects=False, data= {'offeringID':0})

        ar = r.json() 
        theID = None
        count = 0
        for row in ar:
            if row[0] == 0:
                count += 1
                theID = row[0]
       
        self.assertTrue(count == 1, "There should be only one assignment for the offering with id 0")

        self.assertTrue(theID == 0, "The assignment should have id = 0")

    def test_get_assignment_list_malformed_input(self):
        r = requests.post('https://0.0.0.0:8001/api/v1/getAssignmentList', verify=False, allow_redirects=False, data= {'offegID':0})

        self.assertTrue(r.status_code == 400, "getAssignmentList failed to detect malformed input.")
    
#TODO:  adding classes, adding offerings add assignments, addNewUser,