# import codecs
# print(codecs.encode('cvpbPGS{arkg_gvzr_V\'yy_gel_2_ebhaqf_bs_ebg13_Ncualgvd}', 'rot_13'))
import base64


c = base64.b64decode('536B704D525656575330784C52567055523151795530745752465A48546B4A54527A56495255315855316448576B354657565179546B706154555A5055307379536C4A4B566B4657536A564956545A554D6C424B4E51253344253344').decode("utf-8")
for i in range(0, 256):
     for j in range(1, 256):
             k = "".join([chr((ord(x) - i + j) %j) for x in c])
             if 'flag' in k:
                     print(k)
