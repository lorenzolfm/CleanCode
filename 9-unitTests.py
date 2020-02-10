class TestEmployee(unittest.TestCase):

    def test_fullName(self):
        #Build
        employee = Employee('Lorenzo','Maturano', 1000)

        #Operate
        employee.firstName = 'Joao'
        
        #Check
        self.assertEqual(employee.fullName, = 'Joao Maturano')

#================================================================

class TestTermometer(unittest.TestCase):
    
    def setUp(self):
        self.termometer = Termometer()
        self.termometer.setTemperature(wayToCold)

    def test_turnOnLoTempAlarmAtThreashold(self):
        self.assertTrue(self.termometer.heaterState())
        self.assertTrue(self.termometer.blowerState())
        self.assertFalse(self.termometer.coolerState())
        self.assertFalse(self.termometer.hiTempAlarm())
        self.assertTrue(self.termometer.loTempAlarm())

#vs

class TestTermometer(unittest.TestCase):

    def test_turnOnLoTempAlarmAtThreashold(self):
        wayToCold()
        self.assertEquals("HBchL", self.termometer.getState())

#================================================================


