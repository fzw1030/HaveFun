import base64
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
import requests

def sign(alertGroups, appName, msg):
    raw = ""
    for group in alertGroups:
        raw = raw + group
    raw = raw + appName
    raw = raw + msg

    hash = SHA256.new(raw.encode("utf8"))

    privKey = '''-----BEGIN PRIVATE KEY-----
MIICeAIBADANBgkqhkiG9w0BAQEFAASCAmIwggJeAgEAAoGBAOnGf8U7NFGUx0O1
EwsUKiolLN6Go4xpSYLgxEuCZxnff4yuddKqrTLh55c2BD5/ueBOn/ul4iHNU8B9
DRM8OHEy1x7QOvsg/Xe9lASl2n4sdEmEZ5Rd6jm+O97lrJJ7b6qsz3MxHyzsomMA
UShx+cVH+q+jaqO2sFrTqjQ6IIZzAgMBAAECgYEA2xQ73zDpid6ckvYZn5NJJG/s
SanxkP+GdZGAQ6c0ScnqtYM1RbTPVVThfRKRDaUTI4NraCB/9999MnG+lB0mYhyU
PfUNINRyL+9KJ6m802FkM42G0MehYpPSkgjoAM23RaIFQvWBiBTmXrslPwXnXq0W
eCbw5F724wI+0uKB/bkCQQD2TOaMF3VK1BvVy3YPKeMdCnTLXw2VIyvRGuA75sco
pSbR6l64o+FX5h2Xy6GlTgNTFvAN43y4tL1FRj9NVBiVAkEA8vtTmaU53CJyTbAY
Byz/Y3aZNK+3i+iDC1TMUCwZtDPFCVzYgNlwxsXq/j1/t5DIWlkMs/KNwIRiKI6k
nDb45wJAcrzMQcLDz0IUXXpU2yeGN4chdYQoTat+xACjKQSPDq4w8WUfDyC43zvB
2W7xNJKtFc3/slihR2JbMaRR5PIiKQJBAIUSR7K53npFEzyg2Ef1yNh8N2O3aFpj
OIGYK10tCda7E4oRIzFN5Im4Ev6yR6QM0u1IH8Ddceyhk/CKTnSPVrkCQQDfzxZU
NiyfvdTXmrW6e2l3gFiPCDGEG0WlkVg/l9xoPEOvgrfkPBnZKAAvxZtz7SERxpy+
j4qkK+qHWtiVgj3l
-----END PRIVATE KEY-----'''
    key = RSA.importKey(privKey)
    signer = PKCS1_v1_5.new(key)
    signature = signer.sign(hash)
    return base64.b64encode(signature)

def post(alertGroups, appName, msg, signature):
    alertGroupsStr = '["' + '","'.join(alertGroups) + '"]'
    msgStr = '{"alertGroup":' + alertGroupsStr + ', "appName":"' + appName + '", "msg": "' + msg + '"}'
    json_data = '{"maydayMsg":' + msgStr + ', "signature":"' + signature + '"}'
    print("SENDING POST REQUEST : " + json_data)
    head = {"Content-Type": "application/json; charset=UTF-8", 'Connection': 'close'}
    r1 = requests.post("http://10.6.1.79:11000/notapi/r/v1/mayday", data=json_data, headers=head)
    print(r1)

if __name__ == '__main__':
    alertGroups = ["webserver"]
    appName = "test mayday"
    msg = "This is a periodical drill to test bit max emergency notification connectivity, please ignore. Thank you."
    signature = sign(alertGroups, appName, msg)
    post(alertGroups, appName, msg, str(signature,"utf8"))
