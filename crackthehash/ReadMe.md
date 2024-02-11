## Crack The Hash CTF Writeup

This is how i used various tools and techniques to crack different password hashes.

**Introduction:**

I used online services for simpler hashes and Hashcat or JTR for more complex ones.

**Tasks:**

The writeup then details your approach for each task, including:

- **Task 1.1 - MD5:** Identified as MD5 using Hash-Identifier. 
- **Task 1.2 - SHA1:** Identified as SHA1 using Hash-Identifier. 
- **Task 1.3 - SHA256:** Identified as SHA256 using Hash-Identifier.
- **Task 1.4 - Blowfish Bcrypt:** Identified as Blowfish Bcrypt using online search. Cracked using JTR with rockyou.txt wordlist.
- **Task 1.5 - MD4:** Assumed to be MD4 based on previous tasks. Cracked using JTR with MD4 module.

**Section Two:**

This section focuses on harder hashes with brute-force protection:

- **Task 2.1 - SHA256:** Cracked quickly using JTR due to weak password.
- **Task 2.2 - NTLM:** Identified as NTLM using Hash-Identifier. Cracked quickly using JTR due to weak algorithm.
- **Task 2.3 - SHA512Crypt:** Identified as SHA512Crypt using online search. Cracked using JTR with salt and rounds extracted from the hash.
- **Task 2.4 - SHA1 + Salt:** Identified as SHA1 with salt by Hash-Identifier. Cracked using Hashcat with HMAC-SHA1 module and correct password:salt format.

**Final Thoughts:**

The writeup emphasizes the importance of strong passwords and highlights the effectiveness of tools like Hashcat in password cracking, even against algorithms with built-in protection.

**Improvements:**

- Consider adding specific commands used for each Hashcat crack.
- You could mention the limitations of online cracking services.
- Briefly explain the concept of salting and its purpose.

I hope this is helpful!
