# Given an array of integers, determine whether there is a Pythagorean triplet in the array. A Pythagorean triplet is a set of three numbers a, b, c such that a^2 + b^2 = c^2.
class Solution:
    def pythagoreanTriplet(self, arr):
        s = set()

        for x in arr:
            s.add(x*x)

        for a in arr:
            for b in arr:
                if a != b and a*a + b*b in s:
                    return True

        return False