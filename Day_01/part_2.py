from part_1 import read_input_file

def count_occurrence(left_column, right_column):
    occurrence = {}
    for i in range(len(left_column)):
       occurrence.update({left_column[i]: right_column.count(left_column[i])})
    return occurrence

def calc_similarity_score(occurrence):
    similarity_score = []
    for key, value in occurrence.items():
        similarity_score.append(key * value)
    return similarity_score

def main():
    input_file = "input.txt"
    left_column, right_column = read_input_file(input_file)
    occurrence = count_occurrence(left_column, right_column)
    similarity_score = calc_similarity_score(occurrence)
    print(sum(similarity_score))

if __name__ == '__main__':
    main()

