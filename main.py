from ans import *

def getANS(exam):
	ans = dict()
	for i in range(len(exam)):
		a = input(f"{i+1} : ")
		ans[i+1] = a

	return ans

def getPOINT(exam, ans):
	point = dict()
	cor = 0

	for i in ans:
		if ans[i] != exam[i]:
			point[i] = f"{ans[i]} > {exam[i]}"
		else:
			cor += 1
	per = cor/len(exam)

	return point, cor, per

def examList():
	for i in list_exam:
		print('-', i)
	
	while True:
		ex = input("Exam name : ")
		try:
			exam = local[ex]
			break
		except:
			print("Exam name not found")
	return exam

if __name__ == "__main__":
	exam = examList()
	ans = getANS(exam)	
	point, cor, per = getPOINT(exam, ans)
	print("\nSCORE : ", cor)
	print("PERCENT : ", per)
	for i in point:
		print(i, point[i])
