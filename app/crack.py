import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))
