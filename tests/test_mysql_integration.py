import unittest
import MySQLdb

class TestMySQLIntegration(unittest.TestCase):

    def test_add_state_to_database(self):
        # Connect to the MySQL database
        db = MySQLdb.connect(host='localhost', user='cloggings', passwd='12345204001', db='AirBnB_clone_v2')
        cursor = db.cursor()

        # Get the initial number of records in the 'states' table
        cursor.execute("SELECT COUNT(*) FROM states")
        initial_count = cursor.fetchone()[0]

        # Execute the command to add a new state (e.g., via a function or SQL query)
        # Example: cursor.execute("INSERT INTO states (name) VALUES ('California')")

        # Get the number of records after the action
        cursor.execute("SELECT COUNT(*) FROM states")
        final_count = cursor.fetchone()[0]

        # Close the database connection
        db.close()

        # Check if the difference is +1 (a new record was added)
        self.assertEqual(final_count, initial_count + 1)

if __name__ == '__main__':
    unittest.main()

