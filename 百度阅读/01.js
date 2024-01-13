
const Crypto = require("../crypto-js")
function c_encode(e) {
    for (var t = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/", n = new Uint8Array(256), r = 0; r < t.length; r++)
        n[t.charCodeAt(r)] = r;
    var n, r = new Uint8Array(e), i = r.length, o = "";
    for (n = 0; n < i; n += 3)
        o += t[r[n] >> 2],
            o += t[(3 & r[n]) << 4 | r[n + 1] >> 4],
            o += t[(15 & r[n + 1]) << 2 | r[n + 2] >> 6],
            o += t[63 & r[n + 2]];
    return i % 3 == 2 ? o = o.substring(0, o.length - 1) + "=" : i % 3 == 1 && (o = o.substring(0, o.length - 2) + "=="),
    o
}
function u_init(t, n) {
    t = this.words = t || [],
        this.sigBytes = 4 * t.length
}



p = {
    stringify: function (t) {
        for (var e = t.words, n = t.sigBytes, r = [], i = 0; i < n; i++) {
            var o = e[i >>> 2] >>> 24 - i % 4 * 8 & 255;
            r.push(String.fromCharCode(o))
        }
        return r.join("")
    },
    parse: function (t) {
        for (var e = t.length, n = [], r = 0; r < e; r++)
            n[r >>> 2] |= (255 & t.charCodeAt(r)) << 24 - r % 4 * 8;
        return new u_init(n, e)
    }
}
var s = {
    stringify: function (t) {
        // try {
            // bbb=escape(p.stringify(t))
        return decodeURIComponent(encodeURIComponent(p.stringify(t)))
        // } catch (t) {
        //     throw new Error("Malformed UTF-8 data")
        // }
    },
    parse: function (t) {
        return p.parse(decodeURIComponent(encodeURIComponent(t)))
    }
}
function u(t) {
    var e = s.parse("D0CD8B760CE07BC3")
        , n = s.parse("2011121211143000")
        , r = c_encode(t);
    return Crypto.AES.decrypt(r, e, {
        iv: n
    }).toString(s).replace(/</g, "&lt;").replace(/>/g, "&gt;")
}
function binaryStringToArrayBuffer(binaryString) {
    // 使用TextEncoder将二进制字符串转换为Uint8Array
    const encoder = new TextEncoder();
    const uint8Array = encoder.encode(binaryString);

    // 创建一个新的ArrayBuffer，并使用Uint8Array填充它
    const arrayBuffer = uint8Array.buffer.slice(0);

    return arrayBuffer;
}

function main(data1){
    const buffer = binaryStringToArrayBuffer(data1)
    return u(buffer)
}

// url1 = "https://novel-content-new.cdn.bcebos.com/6742163408422523020?md5hash=7a67dd0f3d7f702955f228283bb85f5d&timestamp=1705045123"
//return main(data1);

// console.log(main(data1))

