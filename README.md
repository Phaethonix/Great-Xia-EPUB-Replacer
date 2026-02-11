# Great Xia Replacer

I don't know where you're getting your EPUBs from. And I'm not asking.

But if you've been driven to the brink of madness by the phrase **"Great Xia"** appearing every other sentence in your webnovel, machine translations, well, here's a script for that.

## What it does

Finds `Great Xia` in the text files of an unpacked EPUB and replaces it with something that doesn't make you want to **** the author ********** forever. Technically speaking you could use it to replace any word or phrase, and technically speaking you could run it in a batch across multiple files, but that's not really the point here. The point is **Great Xia** MUST GO!! (also Huaxia, Dragon Country ect.)

## Files

```
Great-Xia.py        # The actual replacement script
Greater-Xia.sh      # Shell script for Linux
Greater-Xia.bat     # Batch script for Windows (AI generated, I don't use Winslop)
README.md           # You are here
```

## Usage

### Linux

```bash
chmod +x Greater-Xia.sh
./Greater-Xia.sh
```

### MacOS

I don't know same as Linux I guess (,,>___<,,) Good luck.

### Windows

Should just work by double-click `Greater-Xia.bat` or run it from cmd. Good luck ദ്ദി(˵ •̀ ᴗ - ˵ ) ✧ 

## What the scripts do

Drop your `.epub` files in the same folder as the scripts, then run. The script will:

1. Extract each `.epub` into `Novels`
2. Back up the original `.epub` files into `Original_Novels`
3. Run `Great-Xia.py` on the extracted contents
4. Repack the folder back into a `.epub` and save it into `Novels`
5. Write a `script.log` so you can see how many replacements were made

Check `script.log` if you're curious how many times "Great Xia" was haunting your book.

## Requirements

- Python 3
- `zip` (Linux) or PowerShell (Windows)

## Note on EPUBs

Standard Windows ZIP compression (`Compress-Archive`) is slightly heavier than the `zip` command used on Linux. The resulting EPUBs will work fine, but they might just be slightly larger in file size. Not really a problem unless you're on a diet.

## Why does this exist

Because "Great Xia" is in there like 47 times per chapter and I needed it gone.
