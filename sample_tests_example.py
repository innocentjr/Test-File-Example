# import * from program file where code is written
import unittest # can do this within any Python file -- it's in the standard library

# Let's say I have a code idea --
# I'll define a class Beverage
# I'll also define subclasses of Beverage: Coffee, and Milk
# And I know that after my code is run, a special menu file should be created
# I'll still need to work out some of those details, but writing the tests is part of defining how this works -- what if I have to pass this beverage / menu project off to someone else? My words might not be specific enough, but my tests are specific and accurate (so far anyway).

# Here's an example of what some of your tests for such a tool file might look like... though the file isn't totally finished in this case, of course.

class TestBeverage(unittest.TestCase): # making a subclass of unittest.TestCase
	def setUp(self): # create a method with a name. Must begin with "test"
	# any setup code for this test method
		self.bev1 = Beverage('lemonade',1.5,'juice')
		self.bev2 = Beverage('...',0.0)

	def test_constructor(self):
		self.assertEqual(self.bev1.name,'lemonade','Got the first one')
		self.assertEqual(self.bev2.name,'...')
		self.assertEqual(self.bev1.cost,1.5)
		self.assertEqual(type(self.bev2.cost),type(1.9))
		self.assertEqual(self.bev1.type,'juice')
		self.assertEqual(self.bev2.type,'unknown')

    # No need for tearDown because there's nothing else to do to 'end' stuff here

class TestCoffee(unittest.TestCase):
	pass # Add tests for the subclass Coffee

class TestMilk(unittest.TestCase):
	pass # Add tests for the subclass Milk

class TestMenu(unittest.TestCase):
	def setUp(self):
		self.file = open('menu.csv','r')
		self.rows = self.file.readlines()
		self.row = self.rows[1]
		self.header = self.rows[0]

	def test_headers(self):
		self.assertEqual(self.header,'Name,Cost,Type\n')

	def test_rows(self):
		self.assertIn('\n',self.row)
		self.assertIsInstance(float(self.row.split(',')[1]),float)

	def tearDown(self):
		self.file.close()

# at the very end of your file
unittest.main(verbosity=2) #verbosity determines how much info you get
