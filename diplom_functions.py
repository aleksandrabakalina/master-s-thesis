def main():
    pass


def bad_phoneme(i, dic_seg4, mark_tuple, voc, signal, allophone):
    number_seg4 = i[3]
    dic_threshold = dic_seg4[number_seg4]
    if len(dic_threshold) == 0:
        mark1 = i[0] // 2
        mark2 = i[1] // 2
        for e in range(mark1, mark2):
            mark_tuple += (signal[e],)
        voc[mark_tuple] = allophone

    elif len(dic_threshold) == 4:
        mark_1 = dic_threshold[0] // 2
        mark_2 = dic_threshold[1] // 2
        mark_3 = dic_threshold[2] // 2
        mark_4 = dic_threshold[3] // 2
        mark1 = i[0] // 2
        mark2 = i[1] // 2

        for e in range(mark1, mark_1):
            mark_tuple += (signal[e],)
        for e in range(mark_2, mark_3):
            mark_tuple += (signal[e],)
        for e in range(mark_4, mark2):
            mark_tuple += (signal[e],)
        voc[mark_tuple] = allophone

    else:
        mark_1 = dic_threshold[0] // 2
        mark_2 = dic_threshold[1] // 2
        mark1 = i[0] // 2
        mark2 = i[1] // 2

        for e in range(mark1, mark_1):
            mark_tuple += (signal[e],)
        for e in range(mark_2, mark2):
            mark_tuple += (signal[e],)
        voc[mark_tuple] = allophone


def vowels_4_2(i, dic_seg3, mark_tuple, voc, signal, allophone):
    number_seg3 = i[3]
    dic_threshold = dic_seg3[number_seg3]
    part = len(dic_threshold)
    if part <= 3:
        mark1 = i[0] // 2
        mark2 = i[1] // 2
        for e in range(mark1, mark2):
            mark_tuple += (signal[e],)
        voc[mark_tuple] = allophone
    else:
        for j in range(len(dic_threshold) - 1):
            if j == 0:
                mark1 = dic_threshold[j] // 2
                mark2 = dic_threshold[j + 2] // 2
                for e in range(mark1, mark2):
                    mark_tuple += (signal[e],)
            if j == part - 2:
                mark1 = dic_threshold[j] // 2
                mark2 = dic_threshold[j + 1] // 2
                for e in range(mark1, mark2):
                    mark_tuple += (signal[e],)
        voc[mark_tuple] = allophone


def vowels_1(i, dic_seg3, mark_tuple, voc, signal, allophone):
    number_seg3 = i[3]
    dic_threshold = dic_seg3[number_seg3]
    part = len(dic_threshold)
    if part <= 4:
        mark1 = i[0] // 2
        mark2 = i[1] // 2
        for e in range(mark1, mark2):
            mark_tuple += (signal[e],)
        voc[mark_tuple] = allophone
    else:
        for j in range(len(dic_threshold) - 1):
            if j == 0:
                mark1 = dic_threshold[j] // 2
                mark2 = dic_threshold[j + 3] // 2
                for e in range(mark1, mark2):
                    mark_tuple += (signal[e],)
            if j == part - 3:
                mark1 = dic_threshold[j] // 2
                mark2 = dic_threshold[j + 2] // 2
                for e in range(mark1, mark2):
                    mark_tuple += (signal[e],)
        voc[mark_tuple] = allophone


def vowels_0(i, dic_seg3, mark_tuple, voc, signal, allophone):
    number_seg3 = i[3]
    dic_threshold = dic_seg3[number_seg3]
    part = len(dic_threshold)
    if part <= 7:
        mark1 = i[0] // 2
        mark2 = i[1] // 2
        for e in range(mark1, mark2):
            mark_tuple += (signal[e],)
        voc[mark_tuple] = allophone

    elif 7 < part <= 15:
        for j in range(len(dic_threshold) - 1):
            if j == 0:
                mark1 = dic_threshold[j] // 2
                mark2 = dic_threshold[j + 4] // 2
                for e in range(mark1, mark2):
                    mark_tuple += (signal[e],)
            if j == part - 5:
                mark1 = dic_threshold[j] // 2
                mark2 = dic_threshold[j + 4] // 2
                for e in range(mark1, mark2):
                    mark_tuple += (signal[e],)
        voc[mark_tuple] = allophone

    else:  # part > 20
        for j in range(len(dic_threshold) - 1):
            if j == 0:
                mark1 = dic_threshold[j] // 2
                mark2 = dic_threshold[j + 5] // 2
                for e in range(mark1, mark2):
                    mark_tuple += (signal[e],)
            if j == part - 6:
                mark1 = dic_threshold[j] // 2
                mark2 = dic_threshold[j + 5] // 2
                for e in range(mark1, mark2):
                    mark_tuple += (signal[e],)
        voc[mark_tuple] = allophone


def normal_cons(i, dic_seg3, mark_tuple, voc, signal, allophone):
    number_seg3 = i[3]
    dic_threshold = dic_seg3[number_seg3]
    part = len(dic_threshold)
    if part <= 5:
        mark1 = i[0] // 2
        mark2 = i[1] // 2
        for e in range(mark1, mark2):
            mark_tuple += (signal[e],)
        voc[mark_tuple] = allophone

    elif 5 < part <= 15:
        for j in range(len(dic_threshold) - 1):
            if j == 0:
                mark1 = dic_threshold[j] // 2
                mark2 = dic_threshold[j + 3] // 2
                for e in range(mark1, mark2):
                    mark_tuple += (signal[e],)
            if j == part - 4:
                mark1 = dic_threshold[j] // 2
                mark2 = dic_threshold[j + 3] // 2
                for e in range(mark1, mark2):
                    mark_tuple += (signal[e],)
        voc[mark_tuple] = allophone

    else:
        for j in range(len(dic_threshold) - 1):
            if j == 0:
                mark1 = dic_threshold[j] // 2
                mark2 = dic_threshold[j + 4] // 2
                for e in range(mark1, mark2):
                    mark_tuple += (signal[e],)
            if j == part - 5:
                mark1 = dic_threshold[j] // 2
                mark2 = dic_threshold[j + 4] // 2
                for e in range(mark1, mark2):
                    mark_tuple += (signal[e],)
        voc[mark_tuple] = allophone

    main()