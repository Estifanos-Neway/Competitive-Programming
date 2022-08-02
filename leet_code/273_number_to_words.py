# 273. Integer to English Words
# https://leetcode.com/problems/integer-to-english-words/
# Hard

class Solution(object):
    units = {
        0: "", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
        10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"
    }
    tens = {
        20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"
    }
    larges = {
        1000: "", 1000000: "Thousand", 1000000000: "Million", 1000000000000: "Billion", 1000000000000000: "Trillion", 1000000000000000000: "Quadrillion"
    }

    def parseHundred(self, hundred):
        word = ""
        tenth = hundred % 100
        if tenth < 20:
            word = self.units[tenth]
        else:
            unit = tenth % 10
            newTenth = tenth - unit
            word = self.tens[newTenth] + (" " if unit != 0 else "") + self.units[unit]
        if hundred > 99:
            hundredth = (hundred - tenth)//100
            word = self.units[hundredth] + " Hundred" + \
                (" " if word != "" else "") + word
        return word

    def parse(self, num, word, d):
        if num < 1:
            return word
        else:
            part = num % 1000
            num = (num - part) // 1000
            if part != 0:
                word = self.parseHundred(
                    part) + " " + self.larges[d] + (" " if word != "" else "") + word
            d *= 1000
            return self.parse(num, word, d)

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        return "Zero" if num == 0 else self.parse(num, "", 1000).strip()


if __name__ == "__main__":
    s = Solution()
    print(s.numberToWords(123)+"|")
