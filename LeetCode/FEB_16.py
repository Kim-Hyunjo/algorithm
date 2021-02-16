class Solution:
    def kWeakestRows(self, mat, k):
        strength = []
        for i in range(len(mat)):
            cnt = 0
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    cnt += 1
                    if j == len(mat[i])-1:
                        strength.append((i,cnt))
                elif mat[i][j] == 0:
                    strength.append((i,cnt))
                    break            
        strength = sorted(strength,key=lambda x:x[1])
        return [strength[i][0] for i in range(k)]         

mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
k = 3
sol = Solution()
sol.kWeakestRows(mat,k)