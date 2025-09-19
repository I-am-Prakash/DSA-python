class Spreadsheet:

    def __init__(self, rows: int):
        self.hashMap = {}
        

    def setCell(self, cell: str, value: int) -> None:
        self.hashMap[cell] = value
        

    def resetCell(self, cell: str) -> None:
        self.hashMap[cell] = 0
        

    def getValue(self, formula: str) -> int:
        plusPosition = formula.index("+")
        left_cell = formula[1 : plusPosition]
        right_cell = formula[plusPosition+1 : ]

        if left_cell[0].isalpha():
            left_value = self.hashMap.get(left_cell, 0)
        else:
            left_value = int(left_cell)

        if right_cell[0].isalpha():
            right_value = self.hashMap.get(right_cell, 0)
        else:
            right_value = int(right_cell)
        return left_value+right_value