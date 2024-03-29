#region imports
from AlgorithmImports import *
#endregion
import config
import statistics as stats
from collections import deque



class VOL_MA():
    
    def __init__(self, algorithm, length):

        self.Length = length

        self.volume_ma = deque(maxlen=self.Length)
        self.value = None
        self.is_ready = False

        self.algorithm = algorithm

        self.Bullish = False
        self.Bearish = False


    def Update_Value(self, value):      # value = volume
        self.volume_ma.appendleft(value)

        if len(self.volume_ma) == self.Length:
            self.value = sum(self.volume_ma) / len(self.volume_ma)
            self.is_ready = True

        

    def Bull_Or_Bear(self, bar):
        # self.volume_ma.appendleft(bar.Volume)

        # if len(self.volume_ma) == self.Length:
        #     self.is_ready = True
        #     self.value = sum(self.volume_ma) / len(self.volume_ma)
        if self.is_ready:
            if bar.Close - bar.Open >= 0:
                barcolor = "GREEN"
            else:
                barcolor = "RED"

            if barcolor == "GREEN" and bar.Volume > self.value:
                self.Bullish = True
                self.Bearish = False
            elif barcolor == "RED" and bar.Volume < self.value:
                self.Bullish = False
                self.Bearish = True
            else:
                self.Bullish = False
                self.Bearish = False
