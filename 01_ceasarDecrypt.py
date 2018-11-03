text=input("Input Text:")
alphabet="abcdefghijklmnopqrstuvwxyz"
k=3
cipher=""
for c in text:
  if c in alphabet:
    cipher +=alphabet[(alphabet.index(c)-k)%(len(alphabet))]
print('Your Decrypted Message is '+ cipher) 