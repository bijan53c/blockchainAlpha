from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend


# RSA key pair
private_key = rsa.generate_private_key(
	public_exponent=65537,
	key_size=2048,
	backend=default_backend()
)

public_key = private_key.public_key()

print (private_key)
print (public_key)

private_key2 = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

print ("PRVK2",private_key2)

# sample data
Message = "20 units sent".encode()


# signing
signature = private_key.sign(Message,padding.PSS(mgf=padding.MGF1(hashes.SHA256()),salt_length=padding.PSS.MAX_LENGTH),hashes.SHA256())



#print (signature)






try:
    public_key.verify(
        signature,
        Message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Valid sign")
except Exception as e:
    print("Invalid sign  ", e)

