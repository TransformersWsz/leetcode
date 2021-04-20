class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1 = version1.split(".")
        l2 = version2.split(".")
        if len(l1) < len(l2):
            gap = len(l2) - len(l1)
            l1 += ["0"] * gap
        else:
            gap = len(l1) - len(l2)
            l2 += ["0"] * gap

        for num1, num2 in zip(l1, l2):
            num1 = int(num1)
            num2 = int(num2)
            if num1 > num2:
                return 1
            elif num1 == num2:
                pass
            else:
                return -1
        return 0

if __name__ == '__main__':
    solution = Solution()
    version1 = "7.5.2.4"
    version2 = "7.5.3"

    res = solution.compareVersion(version1, version2)
    print(res)