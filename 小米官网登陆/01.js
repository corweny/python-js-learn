// #_sign: 不清楚是什么
// #cc: c.callingCode,
// #policyName: b,
// #captCode: u || ""
// #EUI: h.EUI
const CryptoJS = require('./crypto-js')
function It(t) {
    var e;
    t = t || {};
    var i = function(t) {
        for (var e = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*", i = "", r = 0; r < t; r++) {
            var n = Math.floor(Math.random() * e.length);
            i += e.substring(n, n + 1)
        }
        return i
    }(16)
    return i;
    //   , r = new Mt({});
    // r.setPublicKey("MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCYEVrK/4Mahiv0pUJgTybx4J9P5dUT/Y0PuwMbk+gMU+jrZnBiXGv6/hCH1avIhoBcE535F8nJQQN3UavZdFkYidsoXuEnat3+eVTp3FslyhRwIBDF09v4vDhRtxFOT+R7uH7h/mzmyA2/+lfIMWGIrffXprYizbV76+YQKhoqFQIDAQAB");
    // var s = r.encrypt(window.btoa(i))
    //   , h = c().parse("0102030405060708")
    //   , u = c().parse(i)
    //   , f = window.btoa(n()(t).join(","))
    //   , p = {};
    // return n()(t).forEach((function(e) {
    //     var i = t[e]
    //       , r = a().encrypt(i, u, {
    //         iv: h,
    //         padding: l()
    //     });
    //     r = r.toString(),
    //     p[e] = r
    // }
    // )),
    // {
    //     EUI: o()(e = "".concat(s, ".")).call(e, f),
    //     encryptedParams: p
    // }
}

function getSignUser(d){
    return h = It({
        user: d
    })
    // m = h.encryptedParams,
    // user=m.user

}

function main(user_name,pass_word){
    console.log(pass_word)
    sign_user_name = getSignUser(user_name)
    hash = CryptoJS.MD5(pass_word).toString();
    return [sign_user_name,hash]
}


