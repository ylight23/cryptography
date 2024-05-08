import jwt
#su dung thu vien JWT de decode
#cho phep decode 2 dang: 1 la can xac thuc chu ki so (an toan hon), 2 la khong xac thuc chu ki so (mat an toan thong tin)
#crypto co noi rang dev tin rang ma hoa nay se an toan nhma ko xac thuc chu ki so thi có cái nịt
#neu muon an toan thi chac chan phai su dung 1 algorithm de decode
encode_jwt= "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmbGFnIjoiY3J5cHRve2p3dF9jb250ZW50c19jYW5fYmVfZWFzaWx5X3ZpZXdlZH0iLCJ1c2VyIjoiQ3J5cHRvIE1jSGFjayIsImV4cCI6MjAwNTAzMzQ5M30.shKSmZfgGVvd2OSB2CGezzJ3N6WAULo3w9zCl_T47KQ"
decode_jwt = jwt.decode(encode_jwt, options={"verify_signature":False}) 
print(decode_jwt)