class Solution:
    def minimumDays(self, S, N, M):
        if M > N:
            return -1
        if M == N and S > 6:
            return -1 
        count = 1
        total_unit = S * M
        oweek = M * 7
        z = N * 6
        # print(oweek, z)
        if oweek > z and S > 6:
            return -1
        S = S - 1
        f = N - M
        while S > 0:
            if f >= M:
                f = f - M
            elif f < M:
                f = f +  N - M
                count = count + 1
            S = S - 1 
        return count
                
                
