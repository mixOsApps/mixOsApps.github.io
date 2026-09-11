# Generates the QR codes used on apps.html, and the one that goes into the PDF.
#
# Run:  python tools_gen_qr.py
#
# Why files rather than a JavaScript library on the page: these are also printed (the PDF
# carries the apps.html code), GitHub Pages should not depend on a third-party CDN staying up,
# and a committed SVG is reviewable in a diff. Re-running must produce identical files.
#
# Colours are fixed black-on-white rather than themed. A QR reader expects dark modules on a
# light ground; inverting them for dark mode makes some scanners fail, so the page puts these
# on a white tile in both themes instead.

import segno

OUT = {
    # id                       url
    'qr-salah-play':  'https://play.google.com/store/apps/details?id=com.mixzen.salah',
    'qr-salah-web':   'https://mixosapps.github.io/salah-app/',
    'qr-umrah-play':  'https://play.google.com/store/apps/details?id=com.umrahcompanion',
    # This is the one that goes in the PDF. Scanning it lands on apps.html, which is the single
    # page to update when another app ships -- the PDF itself never has to be reissued.
    'qr-apps':        'https://mixosapps.github.io/apps.html',
}

for name, url in OUT.items():
    # error='m' (~15% recovery) is the usual choice for print: enough to survive a scuffed page
    # without inflating the module count, which is what makes a code hard to scan on a phone.
    qr = segno.make(url, error='m')

    qr.save('%s.svg' % name, scale=1, border=2, dark='#000000', light='#ffffff')

    # The PDF needs a raster. 12px per module at border 2 gives a code that stays scannable
    # printed at about 3 cm square.
    if name == 'qr-apps':
        qr.save('%s.png' % name, scale=12, border=2, dark='#000000', light='#ffffff')

    print('%-16s %-3s modules  %s' % (name, qr.symbol_size(border=0)[0], url))
