class StringCalculator:

    def __init__(self):
        pass

    def add(self,numbers):
        list_of_delimiters, numbers = self.get_delimiter(numbers);
        if(len(numbers)) == 0:
            return 0;
        else:
            list_of_numbers = self.get_list_of_numbers(numbers, list_of_delimiters)
            list_of_negative_numbers = list(filter(lambda x: int(x) < 0, list_of_numbers))
            if(len(list_of_negative_numbers) > 0):
                raise Exception("negatives not allowed: " +  " ".join(str(x) for x in list_of_negative_numbers));
            return sum(int(number) for number in list_of_numbers)


    def get_delimiter(self,numbers):
        if numbers[:2] == "//":
            numbers = numbers[2:]
            delimiters = numbers.split('\n', 1)[0];
            if len(delimiters)>1:
                list_of_delimiters = delimiters[1:-1].split("][");
            else :
                list_of_delimiters = [delimiters]
            numbers = numbers.split('\n', 1)[1];
        else :
            list_of_delimiters = [","];
        return list_of_delimiters, numbers

    def get_list_of_numbers(self, numbers, list_of_delimiters):
        list_of_numbers = numbers.replace("//", ',').replace("\n",',');
        for delimiter in list_of_delimiters :
            list_of_numbers = (list_of_numbers.replace(delimiter, ','));
        list_of_numbers = list_of_numbers.split(',');
        list_of_numbers = list(filter(lambda x: int(x) < 1000, list_of_numbers))
        return list_of_numbers
