import base64
import pickle

encoded_string = 'gASVEgAAAAAAAAB9lIwDa2V5lIwFdmFsdWWUcy4='
decoded_string = base64.b64decode(encoded_string)
#Uncomment the line below if you want to see the decoded string before deserialization occurs.
#print(decoded_string)

deserialized_object = pickle.loads(decoded_string)

print(deserialized_object)
