import base64
import pickle

# Replace this with the object you want to serialize and encode
object = {"key": "value"}

# Serialize the object using the specified protocol
serialized_object = pickle.dumps(object)

# Encode the serialized object as a base64 string
encoded_string = base64.b64encode(serialized_object)

print(encoded_string.decode('utf-8'))
