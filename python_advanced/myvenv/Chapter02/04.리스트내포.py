#nums = [i for i in range(10)]
nums = [i for i in range(10) if i % 2 == 0]
print(nums)

nums2 = [100, 200, 300, 400, 500]
#double_nums = [i * 2 for i in nums2]
double_nums = [i * 2 for i in nums2 if i >= 300]
print(double_nums)

# 실습문제1
word_list = ['apple', 'watch', 'apolo', 'star', 'abocado']
result = []
for word in word_list:
    if word[0] == 'a':
        result.append(word)

print(result)

result2 = [i for i in word_list if i[0] == 'a']
print(result2)

# 실습문제2
items = ['오메가3', None, '비타민C500', None, '홍삼절편']
result3 = []
for item in items:
    if item != None:
        result3.append(item)
    else:
        result3.append('')
print(result3)

result4 = [i if i != None else '' for i in items]
print(result4)


