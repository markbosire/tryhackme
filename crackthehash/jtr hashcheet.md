# John Cheatsheet

## Cracking Modes

### Dictionnary attack
```bash
./john --wordlist=password.lst hashFile
```

### Dictionnary attack using default or specific rules
```bash
./john --wordlist=password.lst --rules=rulename hashFile
./john --wordlist=password.lst --rules mypasswd
```

### Incremental mode
```bash
./john --incremental hashFile
```

### Loopback attack (passwords taken from the potfile)
```bash
./john --loopback hashFile
```

### Mask bruteforce attack
```bash
./john --mask=?1?1?1?1?1?1 --1=[A-Z] hashFile --min-len=8
```

### Dictionnary attack using masks
```bash
./john --wordlist=password.lst -mask='?l?l?w?l' hashFile
```

## MISC & Tricks

### Show hidden options
```bash
./john --list=hidden-options
```

### Using session and restoring them
```bash
./john hashes --session=name
./john --restore=name
./john --session=allrules --wordlist=all.lst --rules mypasswd &
./john status
```

### Show the potfile
```bash
./john hashes --pot=potFile --show
```

### Search if a root/uid0 has been cracked
```bash
john --show --users=0 mypasswdFile
john --show --users=root mypasswdFile
```

### List OpenCL devices and get their id
```bash
./john --list=opencl-devices
```

### List format supported by OpenCL
```bash
./john --list=formats --format=opencl
```

### Using multiples GPU
```bash
./john hashes --format:openclformat --wordlist:wordlist --rules:rules --dev=0,1 --fork=2
```

### Using multiple CPU (eg. 4 cores)
```bash
./john hashes --wordlist:wordlist --rules:rules --dev=2 --fork=4
```

## Wordlists & Incremental

### Sort a wordlist for the wordlist mode
```bash
tr A-Z a-z < SOURCE | sort -u > TARGET
```

### Use a potfile to generate a new wordlist
```bash
cut -d ':' -f 2 john.pot | sort -u pot.dic
```

### Generate candidate passwords for slow hashes
```bash
./john --wordlist=password.lst --stdout --rules:Jumbo | ./unique -mem=25 wordlist.uniq
```

### Incremental character sets
- `--incremental:Lower` (26 characters)
- `--incremental:Alpha` (52 characters)
- `--incremental:Digits` (10 characters)
- `--incremental:Alnum` (62 characters)

### Create a new charset
```bash
./john --make-charset=charset.chr
```

Then set the following in the John.conf
```ini
[Incremental:charset]
File = $JOHN/charset.chr
MinLen = 0
MaxLen = 31
CharCount = 95
```

### Using a specific charset
```bash
./john --incremental:charset hashFile
```

## Rules

### Predefined rules
```bash
--rules:Single
--rules:Wordlist
--rules:Extra
--rules:Jumbo # All the above
--rules:KoreLogic
--rules:All # All the above
```

### Create a new rule in John.conf
```ini
[List.Rules:Tryout]
l
u
...
```

### Rule Descriptions

| Rule          | Description                                               |
|---------------|-----------------------------------------------------------|
| l             | Convert to lowercase                                     |
| u             | Convert to uppercase                                     |
| c             | Capitalize                                               |
| l r           | Lowercase the word and reverse it                        |
| l Az"2015"    | Lowercase the word and append "2015" at the end            |
| d             | Duplicate                                                |
| l A0"2015"    | Lowercase the word and append "2015" at the beginning      |
| A0"#"Az"#"    | Add "#" at the beginning and the end of the word           |
| C             | Lowercase the first char and uppercase the rest           |
| t             | Toggle case of all characters                            |
| TN            | Toggle the case of the character in position N            |
| r             | Reverse the word                                         |
| f             | Reflect (Fred --> Fredderf)                              |
| {             | Rotate the word left                                     |
| }             | Rotate the word right                                    |
| $x            | Append char X to the word                                |
| ^x            | Prefix the word with X char                              |
| [             | Remove the first char from the word                      |
| ]             | Remove the last char from the word                       |
| DN            | Delete the character in position N                       |
| xNM           | Extract substring from position N for M characters        |
| iNX           | Insert char X in position N and shift the rest right     |
| oNX           | Overstrike char in position N with X                     |
| S             | Shift case                                               |
| V             | Lowercase vowels and uppercase consonants                |
| R             | Shift each char right on the keyboard                    |
| L             | Shift each char left on the keyboard                     |
| <N            | Reject the word unless it is less than N characters long |
| >N            | Reject the word unless it is greater than N characters long|
| \'N           | Truncate the word at length N                            |
