"""ADSS extraction from a given DC."""

import sys

def find_param(C, u):
    """Find parameters for ADSS: n, s and l."""
    print(u)
    global n,s,l
    i = u
    if i+1 > len(C):
        s = -1
        n = C[i]
        l = 1
        return

    if C[i] == C[i+1]:
        n = C[i]
        l = i
        i += 1
        while i < len(C) and C[i] == n:
            i += 1
        l = i - l
        if i == len(C):
            s = -1
            return
        s = C[i]
        return
    n = C[i]
    s = C[i+1]
    l = 1
    i += 1
    while i+1 < len(C) and C[i+1] in (n,s):
        if C[i] == C[i+1]:
            if C[i] == s:
                temp = n
                n = s
                s = temp
                l = 0
            return
        else:
            i += 1


def find_run(C, st):
    """Find next run."""
    global n, s, l
    cnt = 0
    i = st
    if i+1 > len(C):
        return -1
    else:
        i += 1
        while i<len(C) and C[i] == n:
            cnt += 1
            i += 1
        return cnt


def extract_adss(C):
    """Extract ADSS from chain code of DC."""
    global n, s, l
    A = [0]
    u = 0
    length = len(C)
    while u < length:
        find_param(C, u)
        c = l
        if (s - n) % 8 == 1:
            p = q = find_run(C, u + c)
            if p != -1:
                d = e = (p + 1) / 2
                c = c + 1 + p
                if l - p <= e:
                    while q - p <= d:
                        k = find_run(C, u + c)
                        if k != -1:
                            if l - k > e:
                                c = c + 1 + k
                                break
                            if k - p <= e:
                                c = c + 1 + k
                            else:
                                c = c + 1 + p + e
                            if k < p:
                               p = k
                               d = e = (p + 1) / 2
                            if k > q:
                                q = k
        u = u + c
        A.append(u)
        u = u + 1

    for point in A:
        print(point)

C = [3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 4, 3, 2]
extract_adss(C)
