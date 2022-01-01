import rsa

message = b'Secret message!!!'
(public_key, private_key) = rsa.newkeys(1024)

print('\nprivate_key: ', private_key)
print('\npublic_key: ', public_key)
print('\nmessage: ', message)

encryptedMessage = rsa.encrypt(message, public_key)
print('\nencrypted message: ', encryptedMessage)

decryptedMessage = rsa.decrypt(encryptedMessage, private_key)
print('\ndecrypted message: ', decryptedMessage)
