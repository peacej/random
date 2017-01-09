def solution(S, P, Q):
    map = {'A': [1, 0, 0, 0], 'C': [0, 1, 0, 0], 'G': [0, 0, 1, 0], 'T': [0, 0, 0, 1]}
    presum = [[0, 0, 0, 0]] * (len(S) + 1)
    for i in range(len(S)):
        presum[i + 1] = [x + y for x, y in zip(presum[i], map[S[i]])]
    results = []
    for i in range(len(P)):
        start = P[i]
        end = Q[i]
        nucinrange = [x - y for x, y in zip(presum[end + 1], presum[start])]
        for j in range(len(nucinrange)):
            if nucinrange[j] >= 1:
                results.append(j + 1)
                break
    return(results)

print(solution('CAGCCTA', [2, 5, 0], [4, 5, 6]))