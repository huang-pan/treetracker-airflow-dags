import capture_export
import unittest   # The test framework

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_capture_export(self):
        import psycopg2
        # read env variables DB_URL
        import os
        print("capture export");
        # read env variables DB_URL
        DB_URL = os.environ['DB_URL']
        print("DB_URL:", DB_URL)
        conn = psycopg2.connect(DB_URL, sslmode='require')
        self.assertEqual(capture_export.capture_export(conn, '2020-12'), "Done")

if __name__ == '__main__':
    # Run the unit tests in the test suite with name 'Test_TestIncrementDecrement'
    unittest.main()