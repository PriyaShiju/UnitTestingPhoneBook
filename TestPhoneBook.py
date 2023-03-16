import unittest
from PhoneBook import PhoneBook

class PhoneBookTest(unittest.TestCase):    
    
    def setUp(self) -> None:
        self.phonebook = PhoneBook()
        
    #def tearDown(self) -> None:
    #    pass
    
    def test_lookupbyname(self):        
        self.phonebook.add("Bob", "12345")
        self.number = self.phonebook.lookup("Bob")
        self.assertEqual("12345", self.number)
        
       
    def test_missing_name(self):        
        with self.assertRaises(KeyError) as er:
            self.phonebook.lookup("Jon")
            
    #@unittest.skip("WIP")
    def test_Phonebook_Empty_isconsistent(self):       
        self.assertTrue(self.phonebook.is_consistent())
        
    def test_Phonebook_values_isconsistent(self):
        self.phonebook.add(name="Bob",number="12345")
        self.phonebook.add(name ="Anna",number ="0123")
        self.assertTrue(self.phonebook.is_consistent())
    
    def test_Phonebook_duplicateprefix_isconsistent(self):
        self.phonebook.add("Bob","12345")
        self.phonebook.add("Sue","123")
        self.assertFalse(self.phonebook.is_consistent())
        
    def test_Phonebook_duplicates_isconsistent(self):
        self.phonebook.add("Bob","12345")
        self.phonebook.add("Anna","12345")
        self.assertFalse(self.phonebook.is_consistent())
        
    def test_PhoneBook_adds(self):
        self.phonebook.add("Sue","123456")
        
        
        