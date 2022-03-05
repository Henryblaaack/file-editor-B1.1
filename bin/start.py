try:
    from time import *
    select = None
    print("WARNING")
    print("==========")
    print("My work can use to play or learn")
    print("But don't use my work for commercial transactions")
    print("(I think you Do not)")
    print("5sec to continue")
    print("(Below is the Chinese version)")
    print("警告")
    print("==========")
    print("我的作品可以用来玩或者学习参考")
    print("但是不能用于商业交易等不该做事情")
    print("（你应该不会这么傻）")
    print("5秒后继续")
    print("（上面是English版本）")
    sleep(5)
    while True:
        print("File editor | 文件编辑器")
        print("Menu | 菜单")
        print("Current choice | 目前的选择:",select)
        print("1 | select files | 选择文件")
        print("2 | view files | 查看选择文件")
        print("3 | write files | 写入文件")
        print("4 | about | 关于")
        print("5 | exit | 退出")
        A = input()
        if A == "1":
            print("Please give me the file address | 请输入URL文件地址")
            select = input()
            print("complete | 完成")
        if A == "2":
            with open(select,"r")as file:
                selected = file.read()
                print(selected)
        if A == "3":
            print("1 | Overwrite writes | 覆盖写入")
            print("2 | Write at the back | 在后面写入")
            C = input()
            if C == "1":
                print("Can be written | 可以开始写了")
                D = input()
                with open(select,"w")as file:
                    file.write(D)
                print("complete | 完成")
            if C == "2":
                print("Can be written | 可以开始写了")
                D = input()
                with open(select,"a")as file:
                    file.write(D)
        if A == "4":
            print("""
            file editor | 文件编辑器
            copyright Henry_black 2022 all rights reserved
            """)
        if A == "5":
            print("GOODBYE! | 再见！")
            exit(0)
except:
    print("ERROR Please go to the help.chm to check the ERROR Except for the 5 options| 错误，请查看help.chm来检查问题5选项除外")