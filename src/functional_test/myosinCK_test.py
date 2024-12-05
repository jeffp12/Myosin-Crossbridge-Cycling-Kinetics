# This is a function test to make sure my conditions and simulations above produces the right amount of time points and graphs it correctly.
# This is important as not only as this serves as a checkpoint to evalualte if the code functions, but also later I will be implementing code that calls back upon the values produced in the simulations so I want to make sure these values are generated and stored correctly. 
# PASTE NEW PAREMTERS HERE
import unittest
import tellurium as te
import numpy as np

class TestCrossBridgeDynamics(unittest.TestCase):
    def biochemrxn(self):
        self.r = te.loada('''
        J0: CB0 -> CB1; (k1 * CB0 + k20 * CB2 - (k10 + k2) * CB1);
        J1: CB1 -> CB2; (k2 * CB1 + k30 * CB3 - (k20 + k3) * CB2);
        J2: CB2 -> CB3; (k3 * CB2 + k40 * CB4 - (k30 + k4) * CB3);
        J3: CB3 -> CB4; (k4 * CB3 + k50 * CB5 - (k40 + k5) * CB4);
        J4: CB4 -> CB5; (k5 * CB4 + k60 * CB6 - (k50 + k6) * CB5);
        J5: CB5 -> CB6; (k6 * CB5 + k70 * CB0 - (k60 + k7) * CB6);
        J6: CB6 -> CB0; (k7 * CB6 + k10 * CB1 - (k70 + k1) * CB0);

        # Initial conditions
        CB0 = 0.478; CB1 = 0.0; CB2 = 0.014;
        CB3 = 0.143; CB4 = 0.0; CB5 = 0.144; CB6 = 0.221;

        # Rate Constant Parameters
        k1 = 40; k10 = 70;
        k2 = 140; k20 = 80;
        k3 = 150; k30 = 15;
        k4 = 20; k40 = 0.2;
        k5 = 10; k50 = 0.1;
        k6 = 25; k60 = 0.25;
        k7 = 200; k70 = 50;
        ''')

    def test_simulating_it(self):
        self.biochemrxn()  
        time_end = 0.3
        num_points = 500
        m = self.r.simulate(0, time_end, num_points)
        self.assertEqual(m.shape, (num_points, 8))  # 8 columns: time + 7 reactants

    def test_initial_concentrations(self):
      # Verify initial conditions. CHANGING THIS IN CODE WILL NEED TO BE CHANGED HERE FOR TEST
        self.biochemrxn()  
        self.assertAlmostEqual(self.r["CB0"], 0.478)
        self.assertAlmostEqual(self.r["CB1"], 0.0)
        self.assertAlmostEqual(self.r["CB2"], 0.014)
        self.assertAlmostEqual(self.r["CB3"], 0.143)
        self.assertAlmostEqual(self.r["CB4"], 0.0)
        self.assertAlmostEqual(self.r["CB5"], 0.144)
        self.assertAlmostEqual(self.r["CB6"], 0.221)

    def test_concentrations_total(self):
       # Again these are proportion to 1 so all the concentrations at any given time point must still yield 1.
        self.biochemrxn()  
        m = self.r.simulate(0, 0.3, 500)
        total_concentration = np.sum(m[:, 1:], axis=1) # this does the reactant coloumns and doesnt include time coloiumn
        for value in total_concentration:
            self.assertAlmostEqual(value, 1.0, places=3) # my intial conditions used 3 decimal places so I just set 3 here but this could be even higher for more exact approximation

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
