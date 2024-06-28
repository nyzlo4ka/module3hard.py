def calculate_structure_sum(data_structure):
    def sum_elements(element):
        total_sum = 0
        if isinstance(element, (list, tuple, set)):
            for item in element:
                total_sum += sum_elements(item)
        elif isinstance(element, dict):
            for key, value in element.items():
                total_sum += sum_elements(key)
                total_sum += sum_elements(value)
        elif isinstance(element, str):
            total_sum += len(element)
        elif isinstance(element, (int, float)):
            total_sum += element
        return total_sum

    return sum_elements(data_structure)


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


result = calculate_structure_sum(data_structure)
print(result)



