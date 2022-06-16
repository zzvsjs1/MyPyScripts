if __name__ == '__main__':
    # m_prev = [
    #     [0, 1, 0, 0],
    #     [0, 0, 0, 1],
    #     [0, 0, 0, 0],
    #     [1, 1, 1, 0]
    # ]

    # m_prev = [
    #     [1, 0, 0, 0],
    #     [0, 1, 1, 1],
    #     [0, 1, 1, 0],
    #     [1, 0, 1, 1]
    # ]

    # new_m = [i[:] for i in m_prev]
    #
    # v = len(m_prev)
    #
    # for k in range(v):
    #     new_m = [i[:] for i in m_prev]
    #     for i in range(v):
    #         for j in range(v):
    #             new_m[i][j] = m_prev[i][j] | (m_prev[i][k] & m_prev[k][j])
    #
    #     m_prev = [i[:] for i in new_m]
    #
    # for i in new_m:
    #     print(i)

    m_prev = [
        [0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 0]
    ]

    v_len = len(m_prev)

    new_m = None

    index = [1, 3, 4]

    for k in index:
        new_m = [i[:] for i in m_prev]
        for i in range(v_len):
            for j in range(v_len):
                new_m[i][j] = m_prev[i][j] | (m_prev[i][k] & m_prev[k][j])

        m_prev = new_m

    s = 'ABCDEF'
    print('   ', end='')
    for i in s:
        print(f'{i}  ', end='')
    print()

    for a, i in zip(s, new_m):
        print(f'{a} {i}')
