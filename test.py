def score(x, y):
    length = len(x)
    temp = []
    for i in range(length):
        temp.append(max(x[i], y[i]))
    return min(temp)

def get_min_score(books):
    length = len(books)
    res = [0, 1, 2]
    for i in range(length-1):
        for j in range(length):
            xy_score = score(books[i], books[j])
            if res[0] < xy_score:
                res = [xy_score, i+1, j+1]
    return res


if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        n = int(input())
        books = []
        for _ in range(n):
            line = list(map(int, input().strip().split()))
            books.append(line)
        res = get_min_score(books)
        print(res)
