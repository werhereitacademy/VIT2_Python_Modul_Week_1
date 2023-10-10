if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
output = list(student_marks[query_name])   #girilen query_name mark larini l'ste yapar. ana listeden cekmis olduk zannimca
ort = sum(output) / len(output)  # aritmetik ortalama hesaplattik sum topladi len kac karakter oldu[unu yazdi outputta
print("%.2f" % ort)     #ort ta cikan sonucu 2 decimal ile yazdirir


#The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
# Print the average of the marks array for the student name provided, showing 2 places after the decimal.

