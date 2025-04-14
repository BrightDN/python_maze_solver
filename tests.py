import unittest
from maze import Maze

class TestMaze(unittest.TestCase):
    def setUp(self):
        self.maze1 = Maze(0, 0, 12, 10, 10, 10)

    def test_mazes(self):
        self.assertEqual(len(self.maze1._cells[0]), 12)
        self.assertEqual(len(self.maze1._cells), 10)
        self.assertEqual(self.maze1._cells[0][0].has_top_wall, False)
        self.assertEqual(self.maze1._cells[9][11].has_bottom_wall, False)

if __name__ == '__main__':
    unittest.main()