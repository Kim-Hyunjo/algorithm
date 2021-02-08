#c의 인덱스 저장
#순서대로 거리 저장
#-> 거리가 None이 아닌경우 비교 후 작은것 넣고
#현재 c가 작으면 진행, 더 크면 멈춤
#+ 다른 c를 만나면 멈춤

class Solution(object): 
    def searchDistance(self, start, end, step, answer, s, c, check):
        distance = 0
        if check:
            distance += 1
        for i in range(start, end, step):
            if s[i] == c and i != start:
                break
            if answer[i] is None:
                answer[i] = distance
            else:
                if answer[i] < distance:
                    break
                else:
                    answer[i] = distance
            distance += 1
        return answer

    def shortestToChar(self, s, c):
        cIdxLS = []
        answer = [None for _ in range(len(s))]
        for i in range(len(s)):
            if s[i] == c:
                cIdxLS.append(i)
        for cIdx in cIdxLS:
            distance = 0
            answer = self.searchDistance(cIdx, -1, -1, answer, s, c, False)
            answer = self.searchDistance(cIdx+1, len(s), 1, answer, s, c, True)     
        return answer