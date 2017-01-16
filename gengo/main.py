#!/usr/bin/python
# -*- coding: utf-8 -*-
from hashlib import sha1
import hmac
import json
import requests
import time

if __name__ == '__main__':
    PUBLIC_KEY = '{euSdkCalHR5w]K6Ot2=T5p_MPrhEj)ondFRIDf1rjN9MRf)9FwAKn[N67c$_$3D'
    PRIVATE_KEY = '=fj|kXUSb5A]IVtVW84_pgjw~U5UD0DZlZmjOdnuGgREP01Mdv0(ty}AxXvvfQ)^'

    URL = 'http://api.sandbox.gengo.com/v2/'
    RESPONSE_TYPE = 'json'
    header = {"Accept": "application/{0}".format(RESPONSE_TYPE)}

    data = {
        "api_key": PUBLIC_KEY,
        "api_sig": PRIVATE_KEY,
        "ts": str(int(time.time()))
    }
    # use your private_key to create an hmac
    data["api_sig"] = hmac.new(
        data["api_sig"],
        data["ts"],
        sha1
    ).hexdigest()

    get_language_pair = requests.get(URL, headers=header, params=data)
    res_json = json.loads(get_language_pair.text)
    if not res_json["opstat"] == "ok":
        msg = "API error occured.\nerror msg: {0}".format(
            res_json["err"]
        )
        raise AssertionError(msg)
    else:
        print(res_json)
