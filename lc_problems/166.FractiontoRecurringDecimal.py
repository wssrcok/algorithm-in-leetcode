class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = '-' if numerator / denominator < 0 else ''
        numerator, denominator = abs(numerator), abs(denominator)
        res = ''
        res += str(numerator // denominator)
        numerator = numerator % denominator
        if not numerator:
            return sign + res
        # numerator is smaller than denominator
        d = {numerator:0}
        decimal = []
        while True:
            numerator *= 10
            q = numerator // denominator
            numerator = numerator % denominator
            decimal.append(str(q))
            if numerator == 0:
                return sign + res + '.' + ''.join(decimal)
            if numerator not in d:
                d[numerator] = len(decimal)
            else:
                decimal.insert(d[numerator], '(')
                return sign + res + '.' + ''.join(decimal) + ')'
