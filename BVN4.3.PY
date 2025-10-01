# BTVN4.3
p, q, e = 17, 23, 5
n = p * q

def char_to_num(ch):
    return ord(ch) - ord('A')

def num_to_char(num):
    return chr((num - 1) % 26 + ord('A'))

text = "HANH"

# Chuyển ký tự sang số
plain_nums = [char_to_num(ch) for ch in text]

# Mã hóa: C = M^e mod n
cipher_nums = [pow(m, e, n) for m in plain_nums]

# Đổi số về chữ
cipher_text = ''.join(num_to_char(c % 26 + 1) for c in cipher_nums)

print("n =", n, ", e =", e)
print("Plaintext:", text)
print("Plain numbers:", plain_nums)
print("Cipher numbers:", cipher_nums)
print("Cipher text:", cipher_text)

