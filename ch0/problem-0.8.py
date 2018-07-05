import unittest


def increments(L): return [x + 1 for x in L]

def cubes(L): return [x**3 for x in L]

def tuple_sum(A, B): return [(x+a, y+b) for [(x,y),(a,b)] in zip(A,B)]

def inv_dict(d): return {k:v for v, k in zip(d.keys(), d.values())}

def row(p, n): return [p + i for i, _ in enumerate(range(p, p+n))]


class TestProblems(unittest.TestCase):

    def test_increments(self):
        ex081 = [1, 5, 7]
        self.assertEqual(increments(ex081), [2,6,8])

    def test_cubes(self):
        ex082 = [1, 2, 3]
        self.assertEqual(cubes(ex082), [1, 8, 27])

    def test_tuple_sum(self):
        ex083a = [(1, 2), (10, 20)]
        ex083b = [(3, 4), (30, 40)]
        self.assertEqual(tuple_sum(ex083a, ex083b), [(4, 6), (40, 60)])

    def test_inv_dict(self):
        ex084 = {'thank you': 'merci', 'goodbye': 'au revoir'}
        self.assertEqual(inv_dict(ex084),
                {'merci': 'thank you', 'au revoir': 'goodbye'})

    def test_row(self):
        ex085 = [10, 11, 12, 13]
        self.assertEqual(row(10, 4), ex085)



if __name__ == '__main__':
    unittest.main()
