import string
all_letters = string.ascii_letters
key = 4
cipher_text="Qec xli 15xl, 2022 AewlmrkxsrH.G Hiev Re, Csy evi qc epp pmji. Mx’w fiir epqswx xlvii cievw wmrgi M’zi qix csy mr Lersm. M jipp mr pszi ex jmvwx wmklx. Xs qi, vswiw evi vih, zmspix evi fpyi riziv wibc ew csy, alir mr e wliit M hvieq sj csy, alir mr eaeoi M xlmro sj srpc csy alex ger M hs M’q ws gvedc efsyx csy. M pszi epp sj csy jvsq csyv wqmpi xs csyv iciw alir csy wii qi. M ger’x mqekmri qc pmji amxlsyx csy – amxlsyx csyv gevmrk rexyvi, csyv wirwi sj lyqsv. Csy wezih qi jvsq xli asvwx erh M epaecw wlsa gsrwmhivexmsr jsv mx. Jmklxmrk mw riziv er stxmsr erh qeomrk pszi mw sjxir ew waiix ew xli jmvwx xmqi. Mj M hmi sv ks wsqialivi jev, M ampp avmxi csyv reqi sr izivc wxev, ws xlex tistpi pssomrk yt ger wii nywx lsa qygl csy qier xs qi. M pszi csy ws qygl, qc izivcxlmrk. Csyv jemxljyp, Pmklx."
dict={}
for i in range(len(all_letters)):
    dict[all_letters[i]]= all_letters[(i-key)%(len(all_letters))]

decrypt_txt=[]

for char in cipher_text:
    if char in all_letters:
        temp= dict[char]
        decrypt_txt.append(temp)
    else:
        temp=char
        decrypt_txt.append(temp)
decrypt_txt = "".join(decrypt_txt)
print("Plain text: ",decrypt_txt)            