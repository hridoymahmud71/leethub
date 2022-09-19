class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = numBottles # as we can drink at least the give nnumber of bottles
        while numBottles >= numExchange:

            exchangable = numBottles // numExchange
            reminder = numBottles % numExchange
            numBottles = exchangable + reminder
            result += exchangable

        return result