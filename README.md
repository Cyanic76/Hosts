# Cyanic's Hosts lists

All my hosts lists for you to add to your adblocker.

## Use the main hosts list

Add `https://hosts.cyanic.tk/cyanicHosts.txt` to your adblock (like Pi-Hole). All of the requests that are made to the specified domains will be redirected to 0.0.0.0 (nowhere).

## Choose what you want to block

The goal is to [block standard ad and tracker domains](https://hosts.cyanic.tk/cyanicHosts.txt) and [if you want to block corporations](https://codeberg.org/Cyanic76/Hosts/issues/1), you choose what you want/need to block.

## Get all hosts together

<details><summary>Shell</summary>
Run the `merge_all_hosts.sh` in the `merge_all` folder.
</details>

<details><summary>GitHub Actions (outdated)</summary>
<a href="https://codeberg.org/Cyanic76/Hosts/">View on Codeberg</a>

:warning: This is now outdated and the last artifact has expired.

A workflow was set up for users to download a large file containing ALL hosts from ALL files. 

1. Go to [GitHub Actions](https://github.com/Cyanic76/Hosts/actions?query=is%3Asuccess).

2. Click on the most recent successful run.
  
![Click on the run that shows first.](https://cdn.discordapp.com/attachments/854342838194929685/975399982427426887/unknown.png)

3. Scroll to *Artifcats*.
  
![Scroll down to the Artifacts section](https://cdn.discordapp.com/attachments/854342838194929685/975400093056380979/unknown.png)

4. Click on the `output` text next to the box to start the download.

5. Extract the hosts.txt file from the ZIP archive you'll get.
  
![Extract](https://cdn.discordapp.com/attachments/854342838194929685/975400450335600650/unknown.png)

[![Merge all files into one](https://github.com/Cyanic76/Hosts/actions/workflows/merge_all.yml/badge.svg)](https://github.com/Cyanic76/Hosts/actions/workflows/merge_all.yml)
</details>

## Contributing

If you notice that one or more domains and/or subdomains have not been added to any of my lists, you may [create a new issue](https://github.com/Cyanic76/Hosts/issues/new) with the list of those domains. I will review and add them.

Before filing a new issue or PR, [search in the existing ones](https://github.com/search?l=&q=is%3Aissue++repo%3ACyanic76%2FHosts&type=issues) to make sure you will not open a duplicate one.

**Feel free to add your own hosts to the lists!** Fork the repository, edit the correct files and open a pull request on this repository.

## Legal

I am not liable for any damage. Therefore, feel free to use [Issues](https://github.com/Cyanic76/Hosts/issues/new) to report problems. You are the only one responsible for using this list. This project is licensed under MIT.

---
Maintained by [Cyanic76](https://github.com/Cyanic76).
