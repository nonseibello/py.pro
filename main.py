import random



prototipo="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
caratteri=int(input(" da quanti caratteri vuoi che sia composta la tua password? "))
password=""
for i in range (caratteri):
    
    
    password+=random.choice(prototipo)
print  (password)
