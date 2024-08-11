# strings it

## Description
> Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/5bd86036f013ac3b9c958499adf3e2e2/strings) without running it?

## Hints
> strings

## Solution
- We can use `strings strings | grep 'picoCTF'` to quick find flag
> The strings command is a very useful tool in security analysis and investigation. It allows you to extract and analyze character strings from binary or executable files, helping you detect hidden or suspicious information in these files.

## Flag
> picoCTF{5tRIng5_1T_827aee91}