import unittest
from GameOfLife import GameOfLife

class TestGameOfLife(unittest.TestCase):

    def setUp(self):
        self.game = GameOfLife()
        self.game.generateBoard()

    def test_canAddToBoard(self):
        self.game.generateBoard()
        self.game.addLiveCell((1,1))

    def test_canCheckIfCellAlive(self):
        self.game.addLiveCell((1,2))
        self.assertEqual(self.game.CellIsAlive((1,2)), 1)
        self.assertEqual(self.game.CellIsAlive((2,2)), 0)

#    def test_canKillCell(self):
#        self.game.addLiveCell((1,2))
#        self.game.addLiveCell((2,2))
#        self.game.killCell((2,2))
#        self.assertEqual(self.game.CellIsAlive((1,2)), 1)
#        self.assertEqual(self.game.CellIsAlive((2,2)), 0)

    def test_canGetNeighbors(self):
        self.game.addLiveCell((0,0))
        self.game.addLiveCell((1,1))
        self.game.addLiveCell((2,2))
        self.assertEqual(self.game.getNumNeighbors((1,1)), 2)

    def test_cellIsLonely(self):
        self.game.addLiveCell((0,0))
        self.game.addLiveCell((1,1))
        self.game.addLiveCell((2,2))
        self.game.addLiveCell((3,3))
        self.assertEqual(self.game.cellIsLonely((1,1)), 0)
        self.assertEqual(self.game.cellIsLonely((3,3)), 1)

    def test_cellIsOvercrowded(self):
        self.game.addLiveCell((0,0))
        self.game.addLiveCell((1,1))
        self.game.addLiveCell((2,2))
        self.game.addLiveCell((2,1))
        self.game.addLiveCell((0,1))
        self.assertEqual(self.game.cellIsOvercrowded((1,1)), 1)
        self.assertEqual(self.game.cellIsOvercrowded((2,2)), 0)

    def test_canAdvanceByKillingCells(self):
        self.game.addLiveCell((0,0))
        self.game.addLiveCell((1,1))
        self.game.addLiveCell((2,2))
        self.game.addLiveCell((2,1))
        self.game.addLiveCell((0,1))
        self.game.addLiveCell((3,3))
        self.game.advanceGame()
        self.assertEqual(self.game.CellIsAlive((1,1)), 0)
        self.assertEqual(self.game.CellIsAlive((3,3)), 0)

#    def test_canAdvanceByBirthingCells(self):
#        self.game.addLiveCell((0,0))
#        self.game.addLiveCell((0,1))
#        self.game.addLiveCell((2,2))
#        self.assertEqual(self.game.CellIsAlive((1,1)), 0)
#        self.game.advanceGame()
#        self.assertEqual(self.game.CellIsAlive((1,1)), 1)
