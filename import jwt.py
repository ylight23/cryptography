import jwt
import base64

header_ = '{"typ":"JWT","alg":"none"}'
encode_ = header_.encode('ascii')
print(encode_)
b64_ = base64.b64encode(encode_)
print(b64_)