print("WELCOME TO THE COLLINS ENCRYPTION CODE")
class encryption():
  def __init__(self):
    return

  def check_encrypt_count(self, string, key):
    self.string_encrypted=string #I am only naming it self.string_encrypted because I want to loop it to an amount of times
    counter=0
    while counter<int(str(key)[0]): 
      '''
      This is a second level encryption I recently added to make it relatively harder to decrypt; 
      This part of the code enables to program run the encryptiong multiply times depending on the first number in the encryption key
      '''
      self.encrypt(self.string_encrypted, int(key))
      counter+=1
    return self.string_encrypted

  def check_decrypt_count(self, string, key):
    self.string_decrypted=string #I am only naming it self.string_encrypted because I want to loop it to an amount of times
    counter=0 
    while counter<int(str(key)[0]):
      self.decrypt(self.string_decrypted, int(key))
      counter+=1

    return self.string_decrypted


  def encrypt(self, unencrypt, key):
    self.encrypted=[]
    for i in unencrypt:
      if ord(i) in range(65, 91):
        i=chr((((ord(i)-65)+(key%26))%26)+65)
        self.encrypted.append(i)
      elif ord(i) in range(97, 123):
        i=chr((((ord(i)-97)+(key%26))%26)+97)
        self.encrypted.append(i)
      else:
        self.encrypted.append(i)
    self.string_encrypted = "".join(self.encrypted)
    return

  def decrypt(self, undecrypt, key):
    self.decrypted=[]
    for i in undecrypt:
      if ord(i) in range(65, 91):
        i=chr((((ord(i)-65)-(key%26))%26)+65)
        self.decrypted.append(i)
      elif ord(i) in range(97, 123):
        i=chr((((ord(i)-97)-(key%26))%26)+97)
        self.decrypted.append(i)
      else:
        self.decrypted.append(i)
    self.string_decrypted="".join(self.decrypted)
    return 
      

      



mad=encryption()
answer="babie doll"
while answer!="C":
  answer=input("What do you wish to do (A or B or C)\n[A] Encrypt a code\n[B] Decrypt an encrypted code\n[C] Exit\n")
  if answer=="A":
    unencrypt=input("Type in a string or sentence you wish to encrypt")
    key=input("Type in encryption key(can be any positive number)")
    print(mad.check_encrypt_count(unencrypt, key))

  elif answer=="B":
    undecrypt=input("Type in a string or sentence you wish to decrypt")
    key=input("Type in encryption key used to encrypt the data")
    print(mad.check_decrypt_count(undecrypt, key))
