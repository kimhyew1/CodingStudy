# Hash Algorithm ------------------------------------------------------------------
# key = 무언가를 찾기 위한 검색어, value = 그 검색어로 나온 결과 (ex.사전, 전화번호부)
# --> 모든 데이터 타입으로 접근이 가능하다. 
# --> 특히 String 기반으로 정보를 기록하고 관리해야할때는 무조건 hash를 사용한다고 생각!
# --> put, get, getOrDefault(파이썬에는 get에 포함) 이 3가지 특히 잘 알아놓기. 
# 파이썬에서는 dictionary라고 명칭함. 하지만 타 언어에서는 Hash Map라고 명칭
# ---------------------------------------------------------------------------------

# 1) in : 딕셔너리에 해당 키가 있는지 
students = {'kim': 17, 'lee': 15, 'park': 18}

if 'kim' in students:
	print('kim is in students')
else:
	print('kim is not in students')
## >> kim is in students
if 'son' in students:
	print('son is in students')
else:
	print('son is not in students')
## >> son is not in students


# 2) keys : 딕셔너리의 키 뽑기
# key 출력
print(students.keys())
## >> dict_keys(['kim', 'lee', 'park'])

# key 순서대로 출력
for student in students.keys():
	print(student)
## >> kim
## >> lee
## >> park



# 3) values : 딕셔너리의 값 뽑기 
# value 출력
print(students.values())
## >> dict_values([17, 15, 18])

# value 순서대로 출력
for age in students.values():
	print(age)
## >> 17
## >> 15
## >> 18



# 4) items : 딕셔너리의 키&값 합쳐서 뽑기
# 키&값 출력
print(students.items())
## >> dict_items([('kim', 17), ('lee', 15), ('park', 18)])

# 키&값 순서대로 출력
for student_info in students.items():
	print(student_info)
## >> ('kim', 17)
## >> ('lee', 15)
## >> ('park', 18)



# 5) get : 딕셔너리 키로 값을 얻는 법  
# get(key, x)로도 사용이 가능함. 딕셔너리에 key가 없는 경우, x를 리턴해달라는 말임. 만약 키가 있으면 기존값을 반환
# 딕셔너리를 카운터하는 경우에 유용하게 사용

# students 에 있는 키값
print(students.get('kim'))
## >> 17

# students 에 없는 키값
print(students.get('son'))
## >> None
print(students.get('son'), 'unknown')
## >> None unknown



# 6) del : 딕셔너리에서 키,값 한쌍을 지우는 법
print(students)
## >> {'kim': 17, 'lee': 15, 'park': 18}
del students['kim']
print(students)
## >> {'lee': 15, 'park': 18}
# del students['son']
## >> error 발생



# 7) clear : 딕셔너리의 키,값 모든 값을 지우는 법
# students.clear()
# print(students)
## >> {}



# 8) update(put) : 다른 딕셔너리 혹은 키,값 쌍의 반복 가능한 객체를 사용하여 업데이트. 값 갱신 혹은 새롭게 추가
# 역할 : 다른 딕셔너리(또는 key–value 쌍)를 한꺼번에 병합
# 이미 존재하는 키라면 덮어씌움 / 여러 개의 키를 동시에 추가 및 수정 가능 / 반환값은 none
students.update({'min':19})
print(students)
## >> {'lee': 15, 'park': 18, 'min': 19}
students['kim'] = 21
print(students)
## >> {'lee': 15, 'park': 18, 'min': 19, 'kim': 21}



# 9) setdefault : 지정된 키가 딕셔너리에 없으면 키와 함께 기본값을 추가함. 이미 존재하면 기존의 값을 반환하고 변경 안함. 
# 역할 : 이 키가 없으면 기본값으로 만들고, 있으면 그대로 두기
# 이미 존재하면 절대 덮어쓰지 않음 / 단일 키만 처리 / 해당 키의 최종 값 반환
print(students.setdefault('lee', 30))
## >> 15



# ---------------------------------------------------------------------------------
# init : 빈 딕셔너리 선언
dict1 = {}
dict2 = dict()
print(dict1)
## >> {}
print(dict2)
## >> {}


# key로만 순회
dict = {'david': 300, 'Anna': 180}
for key in dict:
    print(key)
# value를 찾고 싶으면 dict[key] 와 같이 접근을 따로 해주어야 함. 
for key in dict:
    value = dict[key]
    print(value)


# key-value 동시 순회
dict = {'david': 300, 'Anna': 180}
for key, value in dict.items():
    print(key, value)
	


# list to dictionary
# 1. Dictionary Comprehesion(딕셔너리 컴프리헨션) 이용
string_list = ['A','B','C']
dictionary = {string : 0 for string in string_list}
print(dictionary)
## >> {'A': 0, 'B': 0, 'C': 0}
dictionary = {string : i for i,string in enumerate(string_list)}
print(dictionary)
## >> {'A': 0, 'B': 1, 'C': 2}

# 2. dict.fromkeys(key, value) 이용
dictionary = dict.fromkeys(string_list,0)
print(dictionary)
## >> {'A': 0, 'B': 0, 'C': 0}
dictionary = dict.fromkeys(string_list)
print(dictionary)
## >> {'A': None, 'B': None, 'C': None}

# 3. list의 값을 value로 갖는 dict 만들기 (1번 방법에서 key와 value가 반대로)
dictionary = {i : string_list[i] for i in range(len(string_list))}
print(dictionary)
## >> {0: 'A', 1: 'B', 2: 'C'}

# 두개의 리스트로 진행을 한다면...
# 4. zip 사용하여 묶기
string_list = ['A','B','C']
int_list = [1, 2, 3]
dictionary = dict(zip(string_list, int_list))
print(dictionary)
## >> {'A': 1, 'B': 2, 'C': 3}

# tuple로 되어있는 list를 dict로 바꾸려면..
tuple_list = [('A',1), ('B',2), ('C',3)]
dictionary = dict(tuple_list)
print(dictionary)
## >> {'A': 1, 'B': 2, 'C': 3}



def funcs(A,B): #A,B는 리스트가 입력 됨
    hash_table = { hash(x) for x in A } #comprehension을 통해 A에 있는 값을 hash() 함수로 변환한 값을 hash_table에 입력 한다. 
    interAnB = list() # 공통으로 포함되어 있는 값을 저장하기 위한 변수
    print(hash_table)

    for val in B : # B에 있는 값에 대해서
        if hash(val) in hash_table : # hash(val) 이 hash_table에 있으면
            interAnB.append(val)     # interAnB 리스트에 값을 추가 함

    print(interAnB)




# 예시: 리스트 A, B의 차집합 (A - B) 구하기 (딕셔너리 활용)
list_A = [1, 2, 3, 4]
list_B = [3, 4, 5, 6]

# B의 원소를 해시맵(딕셔너리)에 저장하여 빠른 검색을 위함
hash_B = {}
for item in list_B:
    hash_B[item] = True

result = []
for item in list_A:
    # B에 없는 원소만 result에 추가
    if item not in hash_B:
        result.append(item)

print(f"딕셔너리 활용 차집합 (A - B): {result}") # 출력: [1, 2]