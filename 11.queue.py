from queue import Queue

if __name__ == '__main__':
    q = Queue(-1)

    for i in range(1, 6):
        q.put(i)
        print(q.queue)

    while not q.empty():
        gt = q.get()
        print(gt)
        print(q.queue)
