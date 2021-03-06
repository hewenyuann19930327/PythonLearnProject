# Python 运行解释
'''
Python是一种计算机编程语言。
    计算机编程语言和我们日常使用的自然语言有所不同，最大的区别就是，自
    然语言在不同的语境下有不同的理解，而计算机要根据编程语言执行任务，
    就必须保证编程语言写出的程序决不能有歧义，所以，任何一种编程语言都
    有自己的一套语法，编译器或者解释器就是负责把符合语法的程序代码转换
    成CPU能够执行的机器码，然后执行。Python也不例外。
'''

# 数据类型介绍
'''
    计算机顾名思义就是可以做数学计算的机器，因此，计算机程序理所当然地
    可以处理各种数值。但是，计算机能处理的远不止数值，还可以处理文本、
    图形、音频、视频、网页等各种各样的数据，不同的数据，需要定义不同的
    数据类型。
'''

# --------------------
    # 1、整数
# --------------------
'''
    Python可以处理任意大小的整数，当然包括负整数，在程序中的表示方法和
    数学上的写法一模一样.计算机由于使用二进制，所以，有时候用十六进制表
    示整数比较方便，十六进制用0x前缀和0-9，a-f表示。
'''
# --------------------
    # 2、浮点数
# --------------------
'''
    浮点数也就是小数，之所以称为浮点数，是因为按照科学记数法表示时，一个
    浮点数的小数点位置是可变的，比如，1.23x109和12.3x108是完全相等的。
    浮点数可以用数学写法，如1.23，3.14，-9.01，等等。但是对于很大或很小
    的浮点数，就必须用科学计数法表示，把10用e替代，1.23x109就是1.23e9，
    或者12.3e8，0.000012可以写成1.2e-5，等等。
    整数和浮点数在计算机内部存储的方式是不同的，整数运算永远是精确的（除
    法难道也是精确的？是的！），而浮点数运算则可能会有四舍五入的误差。
'''
# --------------------
    # 3、字符串
# --------------------
'''
    字符串是以单引号'或双引号"括起来的任意文本，要注意，''或""本身只是一
    种表示方式，不是字符串的一部分，因此，字符串'abc'只有a，b，c这3个字符。
    如果'本身也是一个字符，那就可以用""括起来。
    如果字符串内部既包含'又包含"怎么办？可以用转义字符\来标识，转义字符\
    可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所
    以\\表示的字符就是\。
    如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还
    允许用r''表示''内部的字符串默认不转义。
    如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许
    用'''...'''的格式表示多行内容。
    注意在输入多行内容时，提示符由“>>>”变为“...”，提示你可以接着上一行输入
    ，注意“...”是提示符，不是代码的一部分。
'''
# --------------------
    # 4、布尔值
# --------------------
'''
    布尔值和布尔代数的表示完全一致，一个布尔值只有True、False两种值，要么是
    True，要么是False，在Python中，可以直接用True、False表示布尔值（请注意
    大小写），也可以通过布尔运算计算出来。
    布尔值可以用and、or和not运算。
'''
# --------------------
    # 5、空值
# --------------------
'''
    空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义
    的，而None是一个特殊的空值。
'''
# --------------------
    # 6、变量
# --------------------
'''
    变量的概念基本上和初中代数的方程变量是一致的，只是在计算机程序中，变量不
    仅可以是数字，还可以是任意数据类型。
    变量在程序中就是用一个变量名表示了，变量名必须是大小写英文、数字和_的组合
    ，且不能用数字开头。
    在Python中，等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可
    以反复赋值，而且可以是不同类型的变量。
    这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。静态语
    言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。和静
    态语言相比，动态语言更灵活，就是这个原因。
    请不要把赋值语句的等号等同于数学的等号。理解变量在计算机内存中的表示也非
    常重要，当我们写：
        a = 'ABC'
    时，Python解释器干了两件事情：

        1、在内存中创建了一个'ABC'的字符串；
        2、在内存中创建了一个名为a的变量，并把它指向'ABC'。
    也可以把一个变量a赋值给另一个变量b，这个操作实际上是把变量b指向变量a所指
    向的数据。
'''
# --------------------
    # 7、常量
# --------------------
'''
    所谓常量就是不能变的变量，比如常用的数学常数π就是一个常量。在Python中，
    通常用全部大写的变量名表示常量:
        PI = 3.14159265359
    但事实上PI仍然是一个变量，Python根本没有任何机制保证PI不会被改变，所以，
    用全部大写的变量名表示常量只是一个习惯上的用法，如果你一定要改变变量PI的
    值，也没人能拦住你。
    最后解释一下整数的除法为什么也是精确的。
    在Python中，有两种除法，一种除法是‘/’，这种除法计算结果是浮点数，即使是
    两个整数恰好整除，结果也是浮点数。
    还有一种除法是“//”，称为地板除，两个整数的除法仍然是整数，你没有看错，整
    数的地板除“//”永远是整数，即使除不尽。要做精确的除法，使用/就可以。因为
    “//”除法只取结果的整数部分，所以Python还提供一个余数运算，可以得到两个整
    数相除的余数。无论整数做“//”除法还是取余数，结果永远是整数，所以，整数运
    算结果永远是精确的。
'''
# --------------------
    # 字符串和编码
# --------------------
'''
    在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符
    串支持多语言。对于单个字符的编码，Python提供了ord()函数获取字符的整数表
    示，chr()函数把编码转换为对应的字符。如果知道字符的整数编码，还可以用十六
    进制来写字符串。 
        '\u4e2d\u6587'
        '中文'
    两种写法是等价的。
    由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字
    节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
    Python对bytes类型的数据用带b前缀的单引号或双引号表示：
        x = b'ABC'
    要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes
    的每个字符都只占用一个字节。以Unicode表示的str通过encode()方法可以编码为
    指定的bytes。
    纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8
    编码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII
    编码的范围，Python会报错。
    在bytes中，无法显示为ASCII字符的字节，用\x##显示。
    反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把
    bytes变为str，就需要用decode()方法。如果bytes中包含无法解码的字节，decode()
    方法会报错。
    如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节。
    要计算str包含多少个字符，可以用len()函数。
    len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数。
    在操作字符串时，我们经常遇到str和bytes的互相转换。为了避免乱码问题，应当始终
    坚持使用UTF-8编码对str和bytes进行转换。
    由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存
    源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，为了让
    它按UTF-8编码读取，我们通常在文件开头写上这两行：
        #!/usr/bin/env python3
        # -*- coding: utf-8 -*-
    第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会
    忽略这个注释；
    第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码
    中写的中文输出可能会有乱码。
    申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器
    正在使用UTF-8 without BOM编码。
'''
# --------------------
    # 格式化
# --------------------
'''
格式化
    最后一个常见的问题是如何输出格式化的字符串。我们经常会输出类似'亲爱的xxx你好！
    你xx月的话费是xx，余额是xx'之类的字符串，而xxx的内容都是根据变量变化的，所以，
    需要一种简便的格式化字符串的方式。
    在Python中，采用的格式化方式和C语言是一致的，用%实现。
    你可能猜到了，%运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，
    %d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只
    有一个%?，括号可以省略。
        常见的占位符有：
        占位符 	替换内容
        %d 	    整数
        %f 	    浮点数
        %s 	    字符串
        %x 	    十六进制整数
    其中，格式化整数和浮点数还可以指定是否补0和整数与小数的位数：
        print('%2d-%02d' % (3, 1))
        print('%.2f' % 3.1415926)
    如果你不太确定应该用什么，%s 永远起作用，它会把任何数据类型转换为字符串。
    有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%。

    ------------
    format()
    ------------
    另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字
    符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多：
        'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
'''