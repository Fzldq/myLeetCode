def main():  # 线段树思维
    def pushup(rt):
        Sum[rt] = Sum[rt << 1] + Sum[rt << 1 | 1]

    def build(left, right, rt):
        if left == right:
            Sum[rt] = a[left]
            return
        mid = (left + right) >> 1
        build(left, mid, rt << 1)
        build(mid + 1, right, rt << 1 | 1)
        pushup(rt)
        return

    def pushdown(rt, ln, rn):
        if Add[rt]:
            Add[rt << 1] += Add[rt]
            Add[rt << 1 | 1] += Add[rt]
            Sum[rt << 1] += Add[rt] * ln
            Sum[rt << 1 | 1] += Add[rt] * rn
            Add[rt] = 0

    def update(Left, Right, C, left, right, rt):
        if Left <= left and right <= Right:
            Sum[rt] += C * (right - left + 1)
            Add[rt] += C
            return
        mid = (left + right) >> 1
        pushdown(rt, mid - left + 1, right - mid)
        if Left <= mid:
            update(Left, Right, C, left, mid, rt << 1)
        if Right > mid:
            update(Left, Right, C, mid + 1, right, rt << 1 | 1)
        pushup(rt)

    def query(Left, Right, left, right, rt):
        if Left <= left and right <= Right:
            return Sum[rt]
        mid = (left + right) >> 1
        pushdown(rt, mid - left + 1, right - mid)
        ans = 0
        if Left <= mid:
            ans += query(Left, Right, left, mid, rt << 1)
        if Right > mid:
            ans += query(Left, Right, mid + 1, right, rt << 1 | 1)
        return ans

    a = [0]
    a.extend(sorted(s[2:n + 2]))
    maxa = 2 * 10 ** 5
    Sum = [0] * (maxa << 2)
    Add = [0] * (maxa << 2)

    build(1, n, 1)

    for x in s[n + 2:]:
        left, right = 1, n
        ans = -1
        while left <= right:
            mid = (left + right) >> 1
            if query(mid, mid, 1, n, 1) >= x:
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        if ans == -1:
            # print(0)
            pass
        else:
            # print(n - ans + 1)
            update(ans, n, -1, 1, n, 1)


class ListNode:  # 链表思维
    def __init__(self, val):
        self.val = val
        self.next = None


def main2():
    lst = s[2:n + 2]
    maxa = 200000 + 10
    nlst = [0] * (maxa + 1)
    for i in lst:
        nlst[i] += 1
    tail = back = ListNode(nlst[maxa])
    back_sqr = []
    for i in range(maxa - 1, -1, -1):
        tmp = ListNode(nlst[i] + back.val)
        tmp.next = back
        back = tmp
        if i % 447 == 0:
            back_sqr.append(tmp)
    back_sqr.reverse()

    for i in s[n + 2:]:
        div, mod = divmod(i, 447)

        if mod:
            tmp = back_sqr[div]
            for j in range(mod - 1):
                tmp = tmp.next
            # print(tmp.next.val)
            for j in range(div + 1, 448):
                back_sqr[j] = back_sqr[j].next

        else:
            tmp = back_sqr[div - 1]
            for j in range(446):
                tmp = tmp.next
            # print(tmp.next.val)
            for j in range(div, 448):
                back_sqr[j] = back_sqr[j].next
        tmp.next = tmp.next.next
        tail.next = ListNode(0)
        tail = tail.next


if __name__ == '__main__':
    import timeit
    import numpy as np
    # s = map(int, open(0).read().split())
    s = np.r_[np.array([200000, 200000]), np.random.randint(
        1, 200001, size=400000)]  # 30%处的超大输入例
    n, q = s[:2]
    print(timeit.timeit('main()', number=1, globals=globals()))  # 131.0805197秒
    # 15.208506599999993C秒
    print(timeit.timeit('main2()', number=1, globals=globals()))
