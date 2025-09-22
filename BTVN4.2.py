def mh_thay_the(plaintext, K):
    S=""
    for i in plaintext:
        if i.isalpha():
            base = ord('A') if i.isupper() else ord('a')
            S = S + (chr((ord(i) - base + K) % 26 + base))
        else:
            S = S + i
    return S

plaintext = "HANH"
K=15
ciphertext = mh_thay_the(plaintext, K)
print(f"Chuỗi {plaintext} được mã hóa thành: {ciphertext}")