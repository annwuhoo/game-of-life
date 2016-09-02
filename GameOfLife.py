class CellStruct(object):
    def __init__(self, position, currState, nextState):
        self.position = position
        self.currState = currState
        self.nextState = nextState

class GameOfLife():
    def generateBoard(self):
        self.board = []
        # Make some sort of data structure

    def addLiveCell(self, pos):
        self.board.append(CellStruct(pos, 0, 1))
        # Sort the list

    def CellIsAlive(self, pos):
        for cell in self.board:
            if (cell.position == pos):
                return 1
        return 0
        #return 1 if (pos in self.board) else 0

    def killCell(self, cell):
        self.board[cell].nextState = 0
        #self.board.remove(cell)

    def getNumNeighbors(self, pos):
        numNeighbors = 0
        for i in range(pos[0]-1, pos[0]+2):
            for j in range(pos[1]-1, pos[1]+2):
                numNeighbors += self.CellIsAlive((i,j))
        return numNeighbors-self.CellIsAlive(pos)

    def cellIsLonely(self, pos):
        return 1 if (self.getNumNeighbors(pos) < 2) else 0

    def cellIsOvercrowded(self, pos):
        return 1 if (self.getNumNeighbors(pos) > 3) else 0

    def advanceGame(self):
        for cell in self.board:
            # Check if it lives or dies
            if (self.cellIsOvercrowded(cell.position) or self.cellIsLonely(cell.position)):
                cell.nextState == 0

            # Check if its neighbors can be birthed...this needs to be more efficient
            for j in range(cell.position[0] - 1, cell.position[0] + 2):
                for k in range(cell.position[1] - 1, cell.position[1] + 2):
                    if ((self.getNumNeighbors((j,k)) == 3) and (not self.CellIsAlive((j,k)))):
                        self.addLiveCell((j,k))

    def updateBoard(self):
        for cell in self.board:
            if (cell.nextState == 0)
                self.board.remove(cell)
            if (cell.currState == 0 and cell.nextState == 1):
                cell.currState = 1