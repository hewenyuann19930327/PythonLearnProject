'''
    Python中定义和调用函数都很简单，但是如何顶一个函数参数和传递参数，
    就涉及到一些套路了。Python中的参数主要分以下几种：
        ·必选参数
        ·默认参数
        ·可变参数
        ·关键字参数
        
'''
""" 可变参数 """
'''
    在某些情况下，我们定义函数的时候，无法预估函数应该制定多少个参数，
    这时我们就可以使用可变参数了，就是说参数个数是不确定的。

    在参数前面加一个*号，表示可变的。
    函数的内部参数接收到的是一个tuple。
    这个*号，在给函数传递参数的时候也可以用，来表示任意参数。
'''
""" 关键字参数 """
'''
    可变参数是允许你将不定量的参数传递给函数，而关键字参数则允许你将
    不定长度的键值对，作为参数传递给一个函数。

    在参数前面有两个*号，这样子就可以接收不定长度的键值对，
    在函数内部，她会表示成一个dict。
    同样地，我们也可以使用这个方式来调用函数时传参。
'''
""" 参数组合 """
''' 
    实际使用中，我们经常会同时用到几种参数。但是它们在使用的时候，是
    有顺序的，依次是必选参数、默认参数、可变参数和关键字参数。
'''
# ===================
    # 函数式编程（functional programming）
# ===================
""" 它是一种编程范式（Programming paradigm），也可以说是一种编程模
式，比如常见的过程式编程和面向对象编程。 
    函数式编程的一大特性就是：可以把函数当成变量来使用，比如将函数赋
值给其他变量、把函数作为参数传递给其他函数、函数的返回值也可以是一个
函数等等。
    Python 不是纯函数式编程语言，但它对函数式编程提供了一些支持。
"""
#   其中包括了以下的几个方面
# =======================
""" 
    高阶函数
    匿名函数
    map/reduce/filter
    闭包
    装饰器
    partial 函数
"""
# =======================