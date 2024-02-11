# Wordlists & Co

## Resources

- [Kaonashi Passwords](https://github.com/kaonashi-passwords/Kaonashi)
- [Richelieu Wordlist](https://github.com/tarraschk/richelieu)
- [RockYou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)
- [Packet Storm Wordlists](https://packetstormsecurity.com/Crackers/wordlists/page4/)
- [Gwicks Dictionaries](http://www.gwicks.net/dictionaries.htm)

## SCADA Default Passwords

- [Critifence Default Password Database](http://www.critifence.com/default-password-database/)

## Other Wordlist Resources

- [Weakpass](https://weakpass.com/)
- [Probable Wordlists](https://github.com/berzerk0/Probable-Wordlists)
- [Pwdb Public](https://github.com/FlameOfIgnis/Pwdb-Public)

## CeWL

CeWL allows you to build custom wordlists based on online resources. If you know that your target is target.com, you can parse web content to build lists, though it can be time-consuming.

- 5 levels of depth and minimum 7 characters per word:

```bash
cewl -w customwordlist.txt -d 5 -m 7 www.sans.org
```

- Visit and parse other sites:

```bash
cewl -w customwordlist.txt -d 5 -m 7 -o www.sans.org
```

- Include email addresses:

```bash
cewl -w customwordlist.txt -d 5 -m 7 -e www.sans.org
```

## PACK (Password Analysis and Cracking Kit)

You can get stats about already cracked passwords to define new masks.

- [PACK GitHub](https://github.com/iphelix/pack)

```bash
python statsgen.py rockyou.txt
```

## Combinator

Combinator is part of the hashcat-utils and can be used to prepare a combined wordlist for cracking. It allows combination with other settings like masks or rules.

- [Hashcat-Utils GitHub](https://github.com/hashcat/hashcat-utils)

### Usage Examples:

- Two files combination:

```bash
combinator.exe file1 file2
```

- Three files combination:

```bash
combinator2.exe file1 file2 file3
```

- Feed output directly to hashcat:

```bash
combinator.exe file1 file2 | hashcat -m x hashs.file -a 0 --force -O
```
