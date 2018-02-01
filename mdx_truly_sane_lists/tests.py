import unittest
from textwrap import dedent

from markdown import markdown


class TrulySaneListTest(unittest.TestCase):
    def test_simple(self):
        raw = '''
        - Zero
        
        - One
        - Two
        '''
        expected = '<ul>\n<li>Zero</li>\n</ul>\n<ul>\n<li>One</li>\n<li>Two</li>\n</ul>'
        actual = markdown(dedent(raw), extensions=["mdx_truly_sane_lists"])
        self.assertEqual(expected, actual)

    def test_comlex(self):
        raw = '''
        + attributes
         
        - customer 
          + first_name
          + family_name
          + email
        - person
          + first_name
          + family_name
          + birth_date
        - subscription_id
        
        + request
        '''
        expected = '<ul>\n<li>attributes</li>\n</ul>\n<ul>\n<li>customer <ul>\n<li>first_name</li>\n<li>family_name</li>\n<li>email</li>\n</ul>\n</li>\n<li>person<ul>\n<li>first_name</li>\n<li>family_name</li>\n<li>birth_date</li>\n</ul>\n</li>\n<li>subscription_id</li>\n</ul>\n<ul>\n<li>request</li>\n</ul>'
        actual = markdown(dedent(raw), extensions=["mdx_truly_sane_lists"])
        self.assertEqual(expected, actual)

    def test_sane(self):
        raw = '''
        1. Ordered
        2. List
        
        * Unordered
        * List
        
        1. Ordered again
        
        Paragraph
        * not a list item
        
        1. More ordered
        * not a list item
        
        * Unordered again
        1. not a list item
        '''
        expected = '<ol>\n<li>Ordered</li>\n<li>List</li>\n</ol>\n<ul>\n<li>Unordered</li>\n<li>List</li>\n</ul>\n<ol>\n<li>Ordered again</li>\n</ol>\n<p>Paragraph\n* not a list item</p>\n<ol>\n<li>More ordered\n* not a list item</li>\n</ol>\n<ul>\n<li>Unordered again\n1. not a list item</li>\n</ul>'
        actual = markdown(dedent(raw), extensions=["mdx_truly_sane_lists"])
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()