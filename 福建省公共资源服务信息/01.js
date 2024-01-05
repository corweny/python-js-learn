const CryptoJs = require('./crypto-js')
const md5 = require('./md5.min.js');
r_a="B3978D054A72A7002063637CCDF6B2E5"
r_e="EB444973714E4A40876CE66BE45D5930"
r_i="B5A8904209931867"
function b(t) {
    var e = CryptoJs.enc.Utf8.parse(r_e)
      , n = CryptoJs.enc.Utf8.parse(r_i)
      , a = CryptoJs.AES.decrypt(t, e, {
        iv: n,
        mode: CryptoJs.mode.CBC,
        padding: CryptoJs.pad.Pkcs7
    });
    return a.toString(CryptoJs.enc.Utf8)
}
function s(t, e) {
    return t.toString().toUpperCase() > e.toString().toUpperCase() ? 1 : t.toString().toUpperCase() == e.toString().toUpperCase() ? 0 : -1
}
function l(t) {
    for (var e = Object.keys(t).sort(s), n = "", a = 0; a < e.length; a++)
        if (void 0 !== t[e[a]])
            if (t[e[a]] && t[e[a]]instanceof Object || t[e[a]]instanceof Array) {
                var i = JSON.stringify(t[e[a]]);
                n += e[a] + i
            } else
                n += e[a] + t[e[a]];
    return n
}
function u(e) {
    return md5.update(e)["hex"]()
}
function d(t) {
    for (var e in t)
        "" !== t[e] && void 0 !== t[e] || delete t[e];
    var n = r_a + l(t);
    return u(n)
}
// ccc={
//     "ts": 1704434378073,
//     "pageSize": 20,
//     "AREACODE": "",
//     "M_PROJECT_TYPE": "",
//     "KIND": "GCJS",
//     "GGTYPE": "",
//     "PROTYPE": "",
//     "timeType": "6",
//     "BeginTime": "2023-07-05 00:00:00",
//     "EndTime": "2024-01-05 23:59:59"
// }
// console.log(d(ccc))
// e="B3978D054A72A7002063637CCDF6B2E5BeginTime2023-07-05 00:00:00EndTime2024-01-05 23:59:59KINDGCJSpageSize20timeType6ts1704434142789"
// console.log(u(e))