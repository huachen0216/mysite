push的时候报错：
#hint: Updates were rejected because the tip of your current branch is behind
#hint: its remote counterpart. Merge the remote changes (e.g. 'git pull')
#hint: before pushing again.

git中的内容与本地中的内容部一直，需要先fetch，然后再merge，最后上传push。

强制push：
git push -u origin master -f

定期使用项目仓库内容更新自己仓库内容。
$ git remote add upstream github.com/yeasy/docker_practice
$ git fetch upstream
$ git checkout master
$ git rebase upstream/master
$ git push -f origin master
