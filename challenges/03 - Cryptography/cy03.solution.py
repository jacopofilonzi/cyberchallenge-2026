from base64 import b64decode


input_64 = "ZmxhZ3t3NDF0XzF0c19hbGxfYjE="
input_10 = 664813035583918006462745898431981286737635929725



# 1. Calcola quanti byte servono
n_bytes = (input_10.bit_length() + 7) // 8

# 2. Converti in bytes e decodifica


flag_left = b64decode(input_64).decode()

flag_right = input_10.to_bytes(n_bytes, 'big').decode()

print(f"{flag_left}{flag_right}")