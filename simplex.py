# Simplex solver
import numpy as np


class Tableau(object):
    def __init__(self, arr, show_steps=False):
        self.t = arr.copy()
        self.pivot = None
        self.solved = False
        self._pivot_count = 0
        self._show_steps = show_steps
        
        
    def __repr__(self):
        return "\n" + self.t.__repr__()
    
    
    def get_pivot_point(self):
        # Find the pivot column, the smallest number in the bottom row
        col, = np.where(self.t[-1] == self.t[-1].min())
        assert col.size == 1 # If there are two equal values we might have a problem
        col = col[0] # Unpack the array
        
        # Find the pivot row
        # Divide the last column by the pivot column.
        # The pivot row is the smallest positive quotent (excluding the bottom row)
        ratios = self.t[:,-1] / self.t[:,col]
        ratios = ratios[:-1]           # Remove the last element in the ratios
        if self._show_steps:
            print "The ratio column is:", ratios
        ratios = np.where(ratios < 0, 0, ratios)    # This removes all negative numbers. 
        
        row, = np.where(ratios == ratios[np.nonzero(ratios)].min())  #np.nonzero stops us from finding a zero
        row = row[0] # Unpack the array
        assert row.size == 1 # We could have a probleme if the numbers are equal
        self.pivot = (row, col)
        if self._show_steps:
            print "The pivot point is", self.pivot
        return self.pivot
               
    def one_row(self):
        row, col = self.pivot
        self.t[row] = self.t[row] / self.t[row, col]
        if self._show_steps:
            print self.t
        
        
    def zero_rows(self):
        pivot_row, pivot_col = self.pivot
        tab_rows, tab_cols = self.t.shape
        for row in range(tab_rows):
            if row != pivot_row and self.t[row, pivot_col] != 0:
                if self._show_steps:
                    print "zeroing row:", row
                self._zero_row(row, pivot_row, pivot_col)
        if self._show_steps:
            print self.t, "\n\n"
        
    
    def _zero_row(self, row, pivot_row, pivot_col):
        self.t[row] = self.t[row] + -self.t[row, pivot_col] * self.t[pivot_row] 
    
    
    def perfom_pivot(self):
        if self.pivot:
            # Turn the pivot row to one
            self.one_row()
            
            # turn all other columns to zero
            self.zero_rows()
            
            # Clear the pivot
            self.pivot = None
            
            
    def solve(self):
        while True:
            self._pivot_count += 1
            if self._pivot_count > 100:
                print "Pivoting too many times. Something's wrong"
                break
            
            # Stop if there are no negative elements in the bottom row
            neg_nums = np.where(self.t[-1] < 0)[0]
            if neg_nums.size == 0:
                print "No negative numbers in the bottom row."
                print "Optimal solution is found." 
                if self._show_steps:
                    print self.t, "\n\n"
                break
            else: 
                self.get_pivot_point()                        
                # TODO: Add logic for stopping when there are no positive elements in the pivot column
                self.perfom_pivot()
            
            
    def answer(self):
        return self.t[-1]