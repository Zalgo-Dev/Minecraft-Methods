# Exploiting the NuVotifier Vulnerability (Protocol V1)

## Description
NuVotifier is a plugin that enables Minecraft servers to receive votes from listing websites. It utilizes RSA encryption to verify the authenticity of votes. However, certain versions of NuVotifier still support the **Protocol V1**, which relies on basic RSA encryption and lacks robust countermeasures against specific attack vectors.

This vulnerability allows an attacker to send arbitrary votes using a public key obtained from the target server, thereby simulating fake votes without utilizing legitimate voting sites.

## Technical Details
### **NuVotifier Protocol V1**
The expected format for a valid vote in **Protocol V1** is:

`VOTE\n ServiceName\n Username\n Address\n Timestamp\n`

Each vote must be **fully encrypted using the server's RSA public key**.

### **Exploitation**
The attack involves:
1. **Retrieving the RSA public key** from the NuVotifier server.
2. **Generating a fake vote** adhering to the Protocol V1 structure.
3. **Encrypting the vote with the public key.**
4. **Sending the vote to the server via a TCP connection.**

If no secondary verification system (e.g., a filtering plugin) is implemented, the server will consider these votes legitimate.

## Proof of Concept (PoC)
A Python script has been developed to demonstrate this vulnerability. It allows sending arbitrary votes by specifying the target server's IP and the player's username:

`python Fake-Vote.py <ip> <username>`


## Impact
- **Vote Forgery**: An attacker can simulate votes without using legitimate sites.
- **Illicit Rewards**: If a server offers in-game rewards for each vote, this vulnerability enables unauthorized acquisition of such rewards.
- **Log Spamming**: Massive fake vote submissions can saturate the server's logs.

## Showcase
https://youtu.be/m3dLHnYTVdA

## Status
This vulnerability is **known** and has been addressed in previous updates. NuVotifier acknowledges that Protocol V1 is insecure, but it remains enabled by default to ensure compatibility with many existing voting sites that only support this protocol. [SpigotMC Reference](https://www.spigotmc.org/resources/nuvotifier.13449/updates?page=3&utm_source=chatgpt.com)

## Conclusion
NuVotifier's **Protocol V1** is outdated and susceptible to vote spoofing attacks. It remains active on numerous servers to maintain compatibility with existing voting systems.
