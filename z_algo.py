def z_arr(s):

    Z = [0] * len(s)

    rt = 0
    lt = 0

    for k in range(1, len(s)):

        if k > rt:
            # If k is outside the current Z-box, do naive computation.
            n = 0
            while n + k < len(s) and s[n] == s[n+k]:
                n += 1
            Z[k] = n
            if n > 0:
                lt = k
                rt = k+n-1
        else:
            # If k is inside the current Z-box, consider two cases.

            p = k - lt  # k'
            right_part_len = rt - k + 1 #beta'

            if Z[p] < right_part_len:
                Z[k] = Z[p] #Z[k]'
            else:
                i = rt + 1
                while i < len(s) and s[i] == s[i - k]:
                    i += 1

                Z[k] = i - k

                lt = k
                rt = i - 1
    return Z


string = input("Enter a string: ")

print(z_arr(string))
