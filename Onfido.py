def solution(pricing, checks):
    c, p = 0, 0
    t = len(checks) * len(pricing)
    for i in range(t):
        if c <= len(checks) - 1 and p <= len(checks)-1:
            ck,pr = [list(checks[c].values())[1]], [list(pricing[p].values())[0]]
            if ck == pr:
                if [list(checks[c].values())[2]] == ['pass'] or [list(checks[c].values())[2]] == ['fail']:
                    calculate_invoice = ([list(checks[c].values())[0], list(pricing[p].values())[1]])
                    print(calculate_invoice)
                    c += 1
                    p = 0
                else:
                    p += 1
            else:
                p += 1
        else:
            c += 1
            p = 0


pricing = [{"check_type": "document_photo", "price": 0.5, "currency": "USD"},
           {"check_type": "document_video", "price": 0.9, "currency": "USD"},
           {"check_type": "facial_similarity_photo", "price": 0.3, "currency": "USD"},
           {"check_type": "facial_similarity_video", "price": 0.8, "currency": "USD"},
           {"check_type": "right_to_work", "price": 1.25, "currency": "USD"}]

checks = [{"client": "ABC Bank", "check_type": "facial_similarity_video", "result": "pass"},
          {"client": "ABC Bank", "check_type": "facial_similarity_video", "result": "fail"},
          {"client": "XYCoin", "check_type": "document_photo", "result": "bad_input"},
          {"client": "XYCoin", "check_type": "facial_similarity_photo", "result": "pass"},
          {"client": "XYCoin", "check_type": "document_photo", "result": "pass"}]

solution(pricing, checks)

"""

output:-

['ABC Bank', 0.8]
['ABC Bank', 0.8]
['XYCoin', 0.3]
['XYCoin', 0.5]

"""
