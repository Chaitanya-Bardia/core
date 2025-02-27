import random
from django.core.cache import cache

def send_otp(mobile,user_obj):
    if cache.get(mobile):
        return False,cache.ttl(mobile)
    try:
        otp_to_send = random.randint(1000,9999)
        cache.set(mobile , otp_to_send , timeout=60)
        user_obj.otp = otp_to_send
        user_obj.save()
        return True,0

    except Exception as e:
        print(e)

def send_otp_mail(emailid,user_obj):
    if cache.get(emailid):
        return False,cache.ttl(emailid)
    try:
        otp_to_send = random.randint(1000,9999)
        cache.set(emailid , otp_to_send , timeout=60)
        user_obj.otp = otp_to_send
        user_obj.save()
        return True,0
    except Exception as e:
        print(e)