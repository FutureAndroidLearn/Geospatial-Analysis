import struct

f = open("hancock.shp","rb")
f.seek(36)
a = struct.unpack("<d", f.read(8))
b = struct.unpack("<d", f.read(8))
c = struct.unpack("<d", f.read(8))
d = struct.unpack("<d", f.read(8))

f.seek(36)
e = struct.unpack("<dddd", f.read(32))

pass