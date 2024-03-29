from ans import *
import time

def getANS(exam):
	ans = dict()
	for i in range(len(exam)):
		while True:
			a = input(f"{i+1}/{len(exam)} : ")

			if a == "change":
				while True:
					questionNum = int(input("Question number : "))
					if questionNum in ans:
						break
					else:
						print("Question Number not found")
				answerNew = input(f"New answer(Q{questionNum}) : {ans[questionNum]} > ")
				ans[questionNum] = answerNew
				print(f"{questionNum} : {answerNew}")
			else:
				ans[i+1] = a
				break
	
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
	start_time = time.time()

	exam = examList()
	ans = getANS(exam)	
	point, cor, per = getPOINT(exam, ans)
	print("\nSCORE : ", cor)
	print("PERCENT : ", per)
	for i in point:
		print(i, point[i])

	print(f"\nRUNNING TIME : {int(time.time() - start_time)} sec")
	print(f"TIME PER PROBLEM : {int((time.time() - start_time)/len(exam))} sec")
