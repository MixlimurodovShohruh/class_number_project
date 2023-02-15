class Number:
    def __init__(self, value: int):
        self.value = value


    def get_number(self):
        """
        Returns the number.

        returns: int
        """
        return self.value

    def is_odd(self):
        """
        Returns True if the number is odd, otherwise False.

        returns: bool

        """
        if self.value%2==1:
            return True
        else:
            return False

    def is_even(self):
        """
        Returns True if the number is even, otherwise False. 

        returns: bool
        """
        if self.value%2==0:
            return True
        else:
            return False

    def is_prime(self):
        """
        Returns True if the number is prime, otherwise False.

        returns: bool
        """
        if self.value//range(self.value):

            return True
        else:
            return False 

    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        

    def get_length(self):
        """
        Returns the number of digits in the number.

        returns: int
        """
        return len(str(self.value))
    

    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """
        pass
    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        pass

    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        pass

    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        ls=[]
        for i in str(self.value):
            ls.append(int(i))
        return ls


    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        mx=self.value%10
        for i in str(self.value):
            if int(i)>mx:
                mx=int(i)
        return mx

    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        mn=self.value%10
        for i in str(self.value):
            if int(i) < mn:
                mn = int(i)
        return mn

    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        pass

    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
        pass

    def get_range(self):
        """
        Returns the range of all the digits in the number.

        returns: list
        """
        return list[range(self.value)]                                                                                                  
    def get_frequency(self):
        """
        Returns a dictionary of the frequency of each digit in the number.

        returns: dict
        """
        pass
    

# Create a new instance of Number
number = Number(3575)
print(number.get_min())