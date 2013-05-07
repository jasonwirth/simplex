import unittest
from simplex import Tableau
import numpy as np

class TestSimplex(unittest.TestCase):

    def test_problem_1(self):
        # Setup Array and Tableau
        # Which problem is this?
        arr = np.array([[  -1.,    0.,    1.,    0.,    0.,    1.,    0.,    0.,    0.,    0.,    0.,    0.,   20.],
                        [  -1.,    0.,    0.,    1.,    0.,    0.,    1.,    0.,    0.,    0.,    0.,    0.,    8.],
                        [  -1.,    0.,    0.,    0.,    1.,    0.,    0.,    1.,    0.,    0.,    0.,    0.,   10.],
                        [   0.,   -1.,    1.,    0.,    0.,    0.,    0.,    0.,    1.,    0.,    0.,    0.,   12.],
                        [   0.,   -1.,    0.,    1.,    0.,    0.,    0.,    0.,    0.,    1.,    0.,    0.,   22.],
                        [   0.,   -1.,    0.,    0.,    1.,    0.,    0.,    0.,    0.,    0.,    1.,    0.,   18.],
                        [ 400.,  600., -200., -300., -400.,    0.,    0.,    0.,    0.,    0.,    0.,    1.,    0.]], 
                        dtype=np.float)

        t = Tableau(arr)
        t.solve()

        answer = np.array([ 0., 100., 0., 0., 0., 0., 300., 100., 200., 0., 300., 1., 11200.])

        self.assertEqual(t.answer().all(), answer.all())




if __name__ == '__main__':
    unittest.main()