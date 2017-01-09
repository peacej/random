if S > L and M > P:
    overlap = (S - L) * (M - P)
elif M > P and N > Q:
    overlap = (M - P) * (N - Q)
elif R > K and N > Q:
    overlap = (R - K) * (N - Q)
elif R > K and S > L:
    overlap = (R - K) * (S - L)
else:
    overlap = 0
return (N - L) * (M - K) + (S - Q) * (R - P) - overlap
