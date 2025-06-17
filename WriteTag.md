<a id="top"></a>
# Quick Guide on Tag Cloning
This is quick guide on making a clone or your own dump or one from this library, and assumes you have a Proxmark3 and using ProxSpace. As there are plenty of guides online that can explain things better and therefore will not be within the scope of this guide.

While over at https://github.com/Bambu-Research-Group/RFID-Tag-Guide, Magic Cards Gen2(CUID) are listed as "WORKS", however this guide's author [@exiom-xyz](https://github.com/exiom-xyz) have been unable to make it work as the AMS 2 Pro, AMS HT bricks them without reading every time. So this guide will focus on Gen4 cards (FUID and UFUID), which are "write-once" cards. The main difference is that FUID cards will lock as soon as the UID has been changed, whereas UFUID will require the user to "seal" the card.

More information on the use of magic cards can be found at https://github.com/RfidResearchGroup/proxmark3/blob/master/doc/magic_cards_notes.md#mifare-classic-uscuid

# Table of Contents
* [Dumping Tags You Own](#dumping-tags-you-own)
* [FUID](#fuid)
* [UFUID](#ufuid)

⚠ *(To ease frustrations caused by typos when issuing commands, I encourage you to use the copy button on the right, especially when multiple commands are issued using the same line)* ⚠

## Dumping Tags You Own
If you want to replicate your own tags or contribute to this library, you can easily make dump and key files of your own tags by running the following commands, after placing the tag on your Proxmark 3,
```
hf mf bambukeys -r -d;hf mf dump
```
This process should only take a few seconds with an expected output similar to below, (to keep things short, dumps of key and data were omitted)
```
[=] -----------------------------------
[=]  UID 4b... XX XX XX XX
[=] -----------------------------------

[+] Saved 192 bytes to binary file `C:\Users\exiom\Desktop\ProxSpace\pm3/hf-mf-XXXXXXXX-key.bin`
[+] Loaded binary key file `C:\Users\exiom\Desktop\ProxSpace\pm3/hf-mf-XXXXXXXX-key.bin`
[=] Reading sector access bits...
[=] .................
[+] Finished reading sector access bits
[=] Dumping all blocks from card...
[-] Sector... 15 block... 3 ( ok )
[+] Succeeded in dumping all blocks

[+] time: 10 seconds

[=] -----+-----+-------------------------------------------------+-----------------
[=]  sec | blk | data                                            | ascii
[=] -----+-----+-------------------------------------------------+-----------------

[+] Saved 1024 bytes to binary file `C:\Users\exiom\Desktop\ProxSpace\pm3/hf-mf-XXXXXXXX-dump.bin`
[+] Saved to json file C:\Users\exiom\Desktop\ProxSpace\pm3/hf-mf-XXXXXXXX-dump.json
```

## FUID
FUIDs are marketed as "write once UID", it has a default UID of `AA55C396` and will allow writes to block 0 in this state. It will lock once written to.

### Identify
You can identify the tag by issuing the following commands and will show these expected results
```
hf mf info
```
For an unlocked card the following will show,
```
[usb] pm3 --> hf mf info
[=] --- ISO14443-a Information ---------------------
[+]  UID: AA 55 C3 96
[=] --- Magic Tag Information
[+] Magic capabilities... Gen 2 / CUID
[+] Magic capabilities... Gen 4 GDM / USCUID ( Gen4 Magic Wakeup )
[+] Magic capabilities... Write Once / FUID
```
For an locked card the following will show,
```
[=] --- Magic Tag Information
[=] <n/a>
```

### Write FUID
For simplity, you need to copy the desired source dump file (hf-mf-XXXXXXXX-dump.bin) and it's key file (hf-mf-XXXXXXXX-key.bin) into the `pm3` folder of `ProxSpace` wherever this maybe on your computer.

To write to the FUID tag, we will issue the following command (replace hf-mf-XXXXXXXX-dump.bin with the file name of your source dump file)
```
hf mf restore -u XXXXXXXX --force
```
Expected Output:
```
[+] Loaded binary key file `hf-mf-5AF731B5-key.bin`
[=] Using key file `hf-mf-5AF731B5-key.bin`
[+] Loaded 1024 bytes from binary file `hf-mf-5AF731B5-dump.bin`

Wall of write messages omitted ending in ( ok )

[=] Done!
```
You can verify that the tag has been successfully written by again running `hf mf info`, the UID should now be different to the first time you ran this command and matches that of the source dump file.
```
[usb] pm3 --> hf mf info
[=] --- ISO14443-a Information ---------------------
[+]  UID: XX XX XX XX
```
You can additionally verify the content of the tag by issuing the command,
```
hf mf dump --ns
```
Your FUID tag is now written, locked and ready to use.



## UFUID
UFUIDs are marketed as a "sealable UID", it will allow writes to the card until it is "sealed" by the user.

### Identify
You can identify the tag by issuing the following command:
```
hf mf info
```
For an unlocked card the following will show,
```
[=] --- Magic Tag Information
[+] Magic capabilities... Gen 1a
[+] Magic capabilities... Gen 4 GDM / USCUID ( ZUID Gen1 Magic Wakeup )
```
For an locked card the following will show,
```
[=] --- Magic Tag Information
[+] Magic capabilities... Gen 4 GDM / USCUID ( Gen4 Magic Wakeup )
```

### Write UFUID
For simplity, you need to copy the desired source dump file (hf-mf-XXXXXXXX-dump.bin) and it's key file (hf-mf-XXXXXXXX-key.bin) into the `pm3` folder of `ProxSpace` wherever this maybe on your computer.

To write to the UFUID tag, we will issue the following gen1a command (replace hf-mf-XXXXXXXX-dump.bin with the file name of your source dump file)
```
hf mf cload -f hf-mf-XXXXXXXX-dump.bin
```
Expected Output:
```
[+] Loaded 1024 bytes from binary file `hf-mf-XXXXXXXX-dump.bin`
[=] Copying to magic gen1a MIFARE Classic 1K
[=] .................................................................
[+] Card loaded 64 blocks from file
[=] Done!
```
You can verify that the tag has been successfully written by again running `hf mf info`, the UID should now be different to the first time you ran this command and matches that of the source dump file.
```
[usb] pm3 --> hf mf info
[=] --- ISO14443-a Information ---------------------
[+]  UID: XX XX XX XX
```
You can additionally verify the content of the tag by issuing the command,
```
hf mf dump --ns
```

### Seal UFUID
Before you can use this tag, you will need to seal the UFUID tag by issuing the following commands, otherwise it will respond to Magic Card Gen1 commands which the AMS will identify and ignore the tag. 

⚠ (Please use the copy button on the right, as this procedure depends on you completing the full set of commands within a short time.) ⚠
```
hf 14a raw -a -k -b 7 40;hf 14a raw -k 43;hf 14a raw -k -c e100;hf 14a raw -c 85000000000000000000000000000008
```
Expected Output:
```
[usb] pm3 --> hf 14a raw -a -k -b 7 40;hf 14a raw -k 43;hf 14a raw -k -c e100;hf 14a raw -c 85000000000000000000000000000008
[+] 0A
[+] 0A
[+] 0A
[+] 0A
```
Now, when you issue the command `hf mf info`, it should now look like this,
```
[=] --- Magic Tag Information
[=] <n/a>
```
Your UFUID tag is now written, locked and ready to use.