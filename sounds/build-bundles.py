"""Pack the samples in raw/ into three script files the page loads with <script src>.
Script files work even when the page is opened straight from disk (file://), where Chrome blocks fetch().
Run:  python build-bundles.py   (from this folder) after adding or swapping samples."""
import base64, os, json

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, 'raw')
BUNDLES = {
    'drums':  ['kicks', 'snares', 'claps', 'hats', 'opens', 'percs', 'dark', 'fx'],
    'bass':   ['bass'],
    'melody': ['piano', 'bells', 'flute', 'organ', 'kalimba', 'harp'],
    'acoustic': ['ac-kicks', 'ac-snares', 'ac-sticks', 'ac-toms', 'ac-closed', 'ac-open', 'ac-crash', 'ac-ride'],
}
for bundle, folders in BUNDLES.items():
    parts = ['window.LP_SAMPLES = window.LP_SAMPLES || {};']
    total = 0
    for folder in folders:
        for f in sorted(os.listdir(os.path.join(RAW, folder))):
            if not f.lower().endswith(('.ogg', '.wav', '.mp3')): continue
            data = open(os.path.join(RAW, folder, f), 'rb').read(); total += len(data)
            key = folder + '/' + os.path.splitext(f)[0]
            parts.append('LP_SAMPLES[%s]=%s;' % (json.dumps(key), json.dumps(base64.b64encode(data).decode())))
    out = os.path.join(HERE, bundle + '.js')
    open(out, 'w').write('\n'.join(parts) + '\n')
    print(f'{bundle}.js  {len(parts)-1} samples  {total//1024} KB audio -> {os.path.getsize(out)//1024} KB')
