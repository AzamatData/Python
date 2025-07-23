# Task
# Learn about map and filter functions, and be prepared to explain them in class. Provide examples using these functions with lambda expressions.

# Problems
# 1. is_prime(n) funksiyasi
# is_prime(n) funksiyasini hosil qiling (n > 0). Agar n soni tub bo'lsa True, aks holda False qiymat qaytarsin.

# Misollar:
# Kiritish:
# 4
# Natija:
# False
# (Izoh: 4 soni tub emas, chunki u 2 ga bo'linadi.)

# Kiritish:
# 7
# Natija:
# True
# (Izoh: 7 soni faqat 1 va o'ziga bo'linadi, ya'ni tub son.)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n%i==0:
            return False
    return True
    i+=1
print(is_prime(0))


# 2. digit_sum(k) funksiyasi
# digit_sum(k) funksiyasini yozing, u k sonining raqamlari yig'indisini hisoblaydi.

# Misollar:
# Kiritish:
# 24
# Natija:
# 6
# (Izoh: 24 sonining raqamlari yig'indisi: 2 + 4 = 6.)

# Kiritish:
# 502
# Natija:
# 7
# (Izoh: 502 sonining raqamlari yig'indisi: 5 + 0 + 2 = 7.)


def digit_sum(k):
    soz=str(k)
    num2=0
    i=0
    sum_num=0
    while i<=len(soz)-1:
        num2=int(soz[i])
        sum_num+=num2
        i+=1
    print(sum_num)

digit_sum(502)

# 3. Ikki sonning darajalari
# Berilgan N sonidan oshmaydigan barcha 2 ning darajalarini (ya'ni, 2**k shaklidagi sonlarni) chop etuvchi funksiyani yozing.

# Misol:
# Kiritish:
# 10
# Natija:
# 2 4 8
# (Izoh: 10 dan kichik yoki teng bo'lgan 2 ning darajalari: 2, 4, 8.)
def under_sqrt(num):
    i=0
    while i<=num:
        if i>=1:
            if 2**i<num:
                print(2**i)
        i+=1
under_sqrt(25)
