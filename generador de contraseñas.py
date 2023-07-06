import ramdom

characters="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

length=int(input("introduce la longitud de la contraseña"))

password=""

for i in range(length)
    password+ramdom.choice(characters)

print("esta es la contraseña generada alearotiamente", password) 
