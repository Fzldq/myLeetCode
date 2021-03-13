class Solution:
    def fullJustify(self, words, maxWidth: int):
        n = len(words)
        len_lst = [len(i) for i in words]  # 存一下每个单词的长度
        ans = []
        tmp_count, tmp_lst = 0, []
        for i in range(n):
            # 判断当前tmp_lst的长度和 + 至少需要的空格数量 + 新单词的长度小于限制，
            if tmp_count + len(tmp_lst) + len_lst[i] <= maxWidth:
                tmp_lst += [words[i]]
                tmp_count += len_lst[i]
            else:
                rest = maxWidth - tmp_count  # 剩下这么多空格
                tmp_len = len(tmp_lst) - 1
                tmp_ans = ''
                if tmp_len:  # tmp_lst不止一个单词， 生成一个空格列
                    if not rest % tmp_len:
                        space = [rest // tmp_len] * tmp_len
                    else:
                        space = [(rest // tmp_len + 1)] * (rest % tmp_len) + \
                            [(rest // tmp_len)] * (tmp_len - rest % tmp_len)
                    for j in range(tmp_len):
                        tmp_ans += tmp_lst[j] + ' ' * space[j]
                    tmp_ans += tmp_lst[-1]
                else:  # tmp_lst只有一个单词
                    tmp_ans += tmp_lst[-1] + ' ' * rest
                ans += [tmp_ans]
                tmp_count, tmp_lst = len_lst[i], [words[i]]
        if tmp_lst:
            ans += [' '.join(tmp_lst) + ' ' *
                    (maxWidth - tmp_count - len(tmp_lst) + 1)
                    ]
        return ans
