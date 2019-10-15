class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        List = []


        for i in range(1,n+1):
            oneDiv = False
            div3 = ""
            div5 = ""
            if i % 3 == 0: 
                div3 = "Fizz"
                oneDiv = True
            if i % 5 == 0:
                div5 = "Buzz"
                oneDiv = True
            if oneDiv:
                List.append(div3+div5)
            else:
                List.append(str(i))

        return List
        