push的时候报错：
#hint: Updates were rejected because the tip of your current branch is behind
#hint: its remote counterpart. Merge the remote changes (e.g. 'git pull')
#hint: before pushing again.

git中的内容与本地中的内容部一直，需要先fetch，然后再merge，最后上传push。

强制push：
git push -u origin master -f
