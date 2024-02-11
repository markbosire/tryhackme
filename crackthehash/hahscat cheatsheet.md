# Hashcat Cheatsheet

## MISC and Tricks

- [One Rule to Rule Them All](https://www.notsosecure.com/one-rule-to-rule-them-all/)

### MAX POWER

Force the CUDA GPU interface, optimize for <32 char passwords, and set the workload to insane (-w 4).
It is supposed to make the computer unusable during the cracking process. Finally, use both the GPU and CPU to handle the cracking.

```bash
--force -O -w 4 --opencl-device-types 1,2
```

### Wrapcat - Automating hashcat commands

[Wrapcat GitHub Repo](https://github.com/Haax9/Wrapcat)

```bash
$ python wrapcat.py -m 1000 -f HASH_FILE.txt -p POT_FILE.txt --full --save
```

## Attack Modes

- `-a 0`: Straight - Hash dictionary
- `-a 1`: Combination - Hash dictionary dictionary
- `-a 3`: Bruteforce - Hash mask
- `-a 6`: Hybrid wordlist + mask - Hash dictionary mask
- `-a 7`: Hybrid mask + wordlist - Hash mask dictionary

## Charsets

- `?l`: Lowercase a-z
- `?u`: Uppercase A-Z
- `?d`: Decimals
- `?h`: Hex using lowercase chars
- `?H`: Hex using uppercase chars
- `?s`: Special chars
- `?a`: All (l,u,d,s)
- `?b`: Binary

## Options

- `-m`: Hash type
- `-a`: Attack mode
- `-r`: Rules file
- `-V`: Version
- `--status`: Keep the screen updated
- `-b`: Benchmark
- `--runtime`: Abort after X seconds
- `--session [text]`: Set session name
- `--restore`: Restore/Resume session
- `-o filename`: Output to filename
- `--username`: Ignore the username field in a hash
- `--potfile-disable`: Ignore potfile and do not write
- `--potfile-path`: Set a potfile path
- `-d`: Specify an OpenCL Device
- `-D`: Specify an OpenCL Device Type
- `-l`: List OpenCL Devices & Types
- `-O`: Optimized Kernel, Passwords <32 chars
- `-i`: Increment (bruteforce)
- `--increment-min`: Start increment at X chars
- `--increment-max`: Stop increment at X chars

## Examples

### Benchmark MD4 hashes

```bash
hashcat -b -m 900
```

### Create a hashcat session to hash Kerberos 5 tickets using a wordlist

```bash
hashcat -m 13100 -a 0 --session crackin1 hashes.txt wordlist.txt -o output.pot
```

### Crack MD5 hashes using all characters in 7 character passwords

```bash
hashcat -m 0 -a 3 hashes.txt ?a?a?a?a?a?a?a -o output.pot
```

### Crack SHA1 by using a wordlist with 2 characters at the end

```bash
hashcat -m 100 -a 6 hashes.txt wordlist.txt ?a?a -o output.pot
```

### Crack WinZip hash using a mask (Summer2018!)

```bash
hashcat -m 13600 -a 3 hashes.txt ?u?l?l?l?l?l?l?d?d?d?d! -o output.pot
```

### Crack MD5 hashes using a dictionary and rules

```bash
hashcat -a 0 -m 0 example0.hash example.dict -r rules/best64.rules
```

### Crack MD5 using the combinator function with 2 dictionaries

```bash
hashcat -a 1 -m 0 example0.hash example.dict example.dict
```

### Cracking NTLM hashes

```bash
hashcat64 -m 1000 -a 0 -w 4 --force --opencl-device-types 1,2 -O d:\hashsample.hash "d:\WORDLISTS\realuniq.lst" -r OneRuleToRuleThemAll.rule
```

### Cracking hashes from kerberoasting

```bash
hashcat64 -m 13100 -a 0 -w 4 --force --opencl-device-types 1,2 -O d:\krb5tgs.hash d:\WORDLISTS\realhuman_phill.txt -r OneRuleToRuleThemAll.rule
```

### Combined attacks with wordlist + mask + rules

```bash
hashcat -a 6 -m 0 prenoms.txt ?d?d?d?d -r rules/yourule.rule
```

### Single rule used to uppercase the first letter --> Marie2018

```bash
hashcat -a 6 -m 0 prenoms.txt ?d?d?d?d -j 'c'
```

## Scenario - Cracking Large Files (e.g., NTDS.dit)

Start by making a specific potfile and cracked files (clean environment):
- `domain_ntds.dit`
- `domain_ntds_potfile.pot`

Generate a wordlist using CeWL:

```bash
cewl -d 5 -m 4 -w OUTFILE -v URL
cewl -d 5 -m 4 -w OUTFILE -o -v URL
```

Use basic dictionary cracking with known wordlists:

```bash
.\hashcat64.exe -m 1000 hashs.txt --potfile-path potfile.pot -a 0 rockyou.txt --force -O
```

Start using wordlists + masks + simple rules:

```bash
.\hashcat64.exe -m 1000 hashs.txt -a 6 .\french\* '?d?d?d?d' -j c --increment --force -O
.\hashcat64.exe -m 1000 hashs.txt -a 6 .\french\* -1 .\charsets\custom.chr '?1' -j c --force -O
.\hashcat64.exe -m 1000 hashs.txt -a 6 .\french\* -1 .\charsets\custom.chr '?d?1' -j c --force -O
.\hashcat64.exe -m 1000 hashs.txt -a 6 .\french\* -1 .\charsets\custom.chr '?d?d?1' -j c --force -O
.\hashcat64.exe -m 1000 hashs.txt -a 6 .\french\* -1 .\charsets\custom.chr '?d?d?d?1' -j c --force -O
.\hashcat64.exe -m 1000 hashs.txt -a 6 .\french\* -1 .\charsets\custom.chr '?d?d?d?d?1' -j c --force -O
.\hashcat64.exe -m 1000 hashs.txt -a 6 CEWL_WORDLIST.txt -1 .\

charsets\custom.chr '?d?d?d?d?1' -j c --force -O
.\hashcat64.exe ...
```

Use masks after the tested word (mode 7):

```bash
.\hashcat64.exe -m 1000 hashs.txt -a 7 '?d?d?d?d' .\french\* -j c --increment --force -O
```

Continue with wordlists + complex rules:

```bash
.\hashcat64.exe -m 1000 hashs.txt --potfile-path potfile.pot -a 0 french.txt -r .rules\best64.rule --force -O
.\hashcat64.exe -m 1000 hashs.txt --potfile-path potfile.pot -a 0 french.txt -r .rules\OneRuleToRuleThemAll.rule --force -O
.\hashcat64.exe -m 1000 hashs.txt --potfile-path potfile.pot -a 0 french.txt -r .rules\best64.rule --force -O
.\hashcat64.exe ...
```

Use smart brute force using masks (custom charset can be useful too):

```bash
.\hashcat64.exe -m 1000 hashs.txt --potfile-path potfile.pot -a 3 '?u?l?l?l?d?d?d?d' --force -O
.\hashcat64.exe -m 1000 hashs.txt --potfile-path potfile.pot -a 3 '?u?l?l?l?l?d?d?d' --force -O
.\hashcat64.exe -m 1000 hashs.txt --potfile-path potfile.pot -a 3 '?u?l?l?l?l?l?d?d' --force -O
.\hashcat64.exe -m 1000 hashs.txt --potfile-path potfile.pot -a 3 -1 .\charset\custom '?u?l?l?l?l?l?d?1' --force -O
.\hashcat64.exe ...
```

Increment mask size and continue:

```bash
.\hashcat64.exe -m 1000 hashs.txt --potfile-path potfile.pot -a 3 '?u?l?l?l?d?d?d?d?d' --force -O
.\hashcat64.exe -m 1000 hashs.txt --potfile-path potfile.pot -a 3 '?u?l?l?l?d?d?d?d?d' --force -O
.\hashcat64.exe -m 1000 hashs.txt --potfile-path potfile.pot -a 3 '?u?l?l?l?d?d?d?d?d' --force -O
.\hashcat64.exe ...
```

If you have few hashes and a small/medium wordlist, you can use random rules and make several loops:

```bash
.\hashcat64.exe -m 1000 hashs.txt --potfile-path potfile.pot -a 0 wl.txt -g 1000000  --force -O -w 3
```

Perform combined attacks:

```bash
# Directly using hashcat
.\hashcat64.exe -m 1000 hashs.txt --potfile-path potfile.pot -a 1 wordlist1.txt wordlist2.txt --force -O
# Or in-memory feeding, it allows you to use rules but not masks
.\combinator.exe wordlist1.txt wordlist2.txt | .\hashcat64.exe -m 1000 hashs.txt --potfile-path potfile.pot -a 0 -rules .\rules\best64.rule --force -O
# Or create the wordlist before and use it
.\combinator.exe wordlist1.txt wordlist2.txt
.\hashcat64.exe -m 1000 hashs.txt --potfile-path potfile.pot -a 6 combinedwordlist.txt '?d?d?d?d' -j c --increment --force -O
```

Use already cracked passwords to build a new wordlist:

```bash
.\hashcat64.exe -m 1000 hashs.txt --potfile-path potfile.pot --show | %{$_.split(':')[1]} > cracked.txt
.\hashcat64.exe -m 1000 hashs.txt -a 6 cracked.txt '?d?d?d?d' -j c --increment --force -O
.\hashcat64.exe -m 1000 hashs.txt -a 0 cracked.txt -r .rules\OneRuleToRuleThemAll.rule --force -O
```

Check the target in popular leaks to find some passwords, then try reusing or applying rules on them.
