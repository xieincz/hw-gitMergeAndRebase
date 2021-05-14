# hw-gitMergeAndRebase
homework: practice for git merge, rebase and squash-merge

### 前置知识
实践本 homework 之前：
* 请先完成 [hw-githubForkAndIssue](https://github.com/SDUOJ-Team/hw-githubForkAndIssue)。
* 请先完成 [hw-gitBranchAndCommit](https://github.com/SDUOJ-Team/hw-gitBranchAndCommit)。

### 本次 HW
本次 homework 是一些关于 `Git&Github` 的知识，在此，你将通过实践逐步学习以下知识：

1. Git Merge
2. Git Rebase
3. Git Squash-Merge

### 开始之前

1. Fork 当前 Repo 到你的账户之下，从现在开始这个 fork 出来的 Repo 将在下文中被称为 "你的 Repo"
2. 执行 `git clone https://github.com/你的用户名/hw-gitMergeAndRebase` 将你 fork 的仓库 clone 到本地
3. 在所有练习开始之前，请明确，现在这个 Repo 有以下的三对分支：
```
	  A---B---C my-feature-1
	 /
 ---D---E---F master-1
    
	  A---B---C my-feature-2
	 /
 ---D---E---F master-2

	  A---B---C my-feature-3
	 /
 ---D---E---F master-3 
```

## hw1: merge

1. 请在`master-1`分支上合并`my-feature-1`分支，并产生一个合并提交 `G`，期望结果如图所示：

    ```
          A---B---C my-feature-1
         /         \
     ---D---E---F---G master-1
    ```
2. push 这个 `master-1` 分支到你的 Repo

OK，现在你完成了 hw1，你现在需要对母仓库提交一个 issue 来检验你的 Repo 是否正确，issue 模板请选择 "Submit homework1"

## hw2: rebase

1. 请在 `my-feature-2` 分支上 rebase `master-2`分支，期望结果如图所示：

    ```
    D---E---F---A'---B'---C' my-feature-2
            |
            master-2
    ```
2. push 这个 `master-2` 分支到你的 Repo

OK，现在你完成了 hw2，你现在需要对母仓库提交一个 issue 来检验你的 Repo 是否正确，issue 模板请选择 "Submit homework2"

## hw3: squash-merge

1. 请将 `my-feature-3` 分支上的 3 个提交（A、B、C）使用 `merge --squash` 方式，使得这三个提交被合并成一个提交进入 `master-3` 分支，期望结果如图所示：

    ```
          A---B---C my-feature-3
         /
     ---D---E---F---G master-3 
                    |
                   压扁后的提交
    ```
2. push 这个 `master-3` 分支到你的 Repo

OK，现在你完成了 hw3，你现在需要对母仓库提交一个 issue 来检验你的 Repo 是否正确，issue 模板请选择 "Submit homework3"

## hw4: reset

1. 请基于 `my-feature` 分支创建 `my-reset-feature` 分支，并将上面最新的三个提交压扁成一个提交：

    压扁前：
    ```
     ---D---E---F---G my-feature
    ```
    
    压扁后：
    ```
     ---D---H my-reset-feature
            |
            压扁后的提交
    ```
2. push 这个 `my-reset-feature` 分支到你的 Repo

OK，现在你完成了 hw4，你现在需要对母仓库提交一个 issue 来检验你的 Repo 是否正确，issue 模板请选择 "Submit homework4"

## Credits
* https://github.com/hcsp/advanced-git