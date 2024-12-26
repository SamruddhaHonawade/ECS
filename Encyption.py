def xor_encrypt_decrypt(input_string, key):
    
    
    
    input_bytes = bytearray(input_string, 'utf-8')
    output_bytes = bytearray([byte ^ key for byte in input_bytes])
    return output_bytes.decode('utf-8', 'ignore')

# Example usage:
key = 123  # XOR key
original_text = input("Enter the message: ")

encrypted_text = xor_encrypt_decrypt(original_text, key)
print(f"Encrypted: {encrypted_text}")

decrypted_text = xor_encrypt_decrypt(encrypted_text, key)
print(f"Decrypted: {decrypted_text}")
