'''
    在程序运行过程中，总会遇到各种各样的错误。
    有的错误是程序编写有问题造成的，比如本来应该输出整数结果输出了字符串，这种错误我们通常称之为bug，
    bug是必须修复的。
    有的错误是用户输入造成的，这种错误可以通过检查用户输入来做相应的处理。
    还有一类错误是完全无法在程序运行过程中预测的，比如写入文件的时候，磁盘满了，写不进去了，或者从网
    络抓取数据，网络突然断了。这类错误也成为异常，在程序中通常必须处理的否则，程序会因为各种问题终止
    并退出。
    Python内置了一套异常处理机制，来帮助我们进行错误处理。
    此外，我们也需要跟踪程序的执行，查看变量的值是否正确，这个过程称为调试。Python的pdb可以让我们以
    单步方式执行代码。
'''
# 错误处理
'''
    在程序运行的过程中，如果发生了错误，可以事先约定返回一个错误代码，这样，就可以知道是否有错，以及
    出错的原因。在操作系统提供的调用中，返回错误码非常常见。比如打开文件的函数open()，成功时返回文件
    描述符（就是一个整数），出错时返回-1。
    用错误码来表示是否出错十分不便，因为函数本身应该返回的正常结果和错误码混在一起，造成调用者必须用
    大量的代码来判断是否出错。
    一旦出错，还要一级一级上报，直到某个函数可以处理该错误（比如，给用户输出一个错误信息）。
    所以高级语言通常都内置了一套try...except...finally...的错误处理机制，Python也不例外。
'''
# try...except...finally
# try:
#     print('try')
#     r = 10/0
#     print('result:',r)
# except ZeroDivisionError as e:
#     print('except:',e)
# finally:
#     print('finally...')
# print('END')
'''
    当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而
    是直接跳转至错误处理代码，即except语句块，执行完except后，如果有finally语句块，则执行finally语句
    块，至此，执行完毕。
    从输出可以看到，当错误发生时，后续语句print('result:', r)不会被执行，except由于捕获到ZeroDivisionError，
    因此被执行。最后，finally语句被执行。然后，程序继续按照流程往下走。
    由于没有错误发生，所以except语句块不会被执行，但是finally如果有，则一定会被执行（可以没有finally语句）。

    你还可以猜测，错误应该有很多种类，如果发生了不同类型的错误，应该由不同的except语句块处理。没错，可以
    有多个except来捕获不同类型的错误。
    Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但
    捕获该类型的错误，还把其子类也‘一网打尽’。
    当第二个except是第一个错误的子类第二个就永远都捕获不到错误，有except也被第一个捕获了。
    Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系：https://docs.python.org/3/library/exceptions.html#exception-hierarchy
    使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，比如函数main()调用foo(),foo()调用bar(),
    结果bar()出错了，这时，只要main()捕获到了，就可以处理了。
    这样子就是说，不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了，这样一来，就大大
    减少了写try...except...finally的麻烦。
'''
# 调用栈
'''
    如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息然后程序退出。
    出错不可怕，可怕的是不知道哪里出错了。解读错误信息是定位错误的关键。我们从上往下可以看到整个错误的调用函数链。

    出错的时候一定要分析错误的调用栈信息，才能定位错误的位置。
'''
# 记录错误
'''
    如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。既然我们不能捕获错误，就可以把错误
    堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。
    Python内置的logging模块可以非常容易地记录错误信息，同样的出现错误了，但是程序打印错误信息之后会继续执行，并正常退出。
    通过配置，logging还可以把错误记录到日志文件里，方便事后排查。
'''
# 抛出错误
'''
    因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是有意创建并抛出的。
    Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。

    如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例。
    只有在必要的时候才定义我们自己的错误类型。如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），
    尽量使用Python内置的错误类型。
    常见的我们捕获了错误，打印出来错误之后，又把错误通过raise语句抛出了。要知道捕获错误只是进行记录方便后续追踪。
    但是一般捕获的函数不知道怎么处理错误或问题，所以最恰当的方式，就是向上抛出，让顶层调用者处理错误。好比一个员工处理不了
    一个问题时，就把问题抛给老板，如果老板处理不了就继续往上抛，给更高层处理问题。
    raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error,还可以把一种类型的错误转化成另一种类型。
    但是还是需要复合逻辑转化。不应该转化成一个完全不相干的错误。
'''
# 小结一下：
'''
    Python内置的try...except...finally用来处理错误十分方便。出错时，会分析错误信息并定位错误发生的代码位置才是最关键的。
    程序也可以主动抛出错误，让调用者来处理相应的错误。但是应该在文档中写清楚可能会抛出那些错误，以及错误产生的原因。
'''
# ==============
# 调试 DEBUG
# ==============
'''
    程序能一次写完并正常运行的概率很小，基本不超过1%。总会有各种各样的bug需要修正。有的bug很简单，看看错误信息就知道，有的
    bug很复杂，我们需要知道出错时，哪些变量的值是正确的，哪些变量的值是错误的，因此，需要一整套调试程序的手段来修复bug。

    第一种方法简单直接粗暴有效，就是用print()把可能有问题的变量打印出来看看。用print()最大的坏处是将来还得删掉它，想想程序
    里到处都是print()，运行结果也会包含很多垃圾信息。所以，我们又有第二种方法。  
'''
# 断言
'''
    凡是使用print()来辅助查看的地方，都可以用断言（assert）来代替。
    assert的意思是，表达式n!=0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。如果断言失败，assert语句本身就会
    抛出AssertionError。
    但是程序中如果到处充斥着assert，和到处都是print()相比也好不到哪去。不过启动Python解释器时，可以用-O参数来关闭assert.
    关闭后，你可以把所有的assert语句当做pass来看。
'''
# def foo(s):
#     n = int(s)
#     assert n!=0,'n is zero!'
#     return 10/n
# def main():
#     foo('0')
# main()
# ====================
# logging
'''
    把print()替换为logging是第三种方式，和assert比，logging不会抛出错误，而且可以输出到文件。
    logging.info()就可以输出一段文本。运行，发现除了ZeroDivisionError，没有任何信息。但是为了看到更多的信息，需要在import logging
    之后添加一行配置。
    logging.basicConfig(level=logging.INFO)
    这就logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起
    作用了。同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你就可以放心地输出不同级别的信息，也不用删除，最后统一控制输出
    哪个级别的信息。
    logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。
'''
# pdb
'''
    第四种方式是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。然后以参数 -m pdb 启动，pdb定位到下一步要执行的代码。
    然后输入命令1来查看代码。任何时候都可以输入命令‘p 变量名’来查看变量。最后从输入q结束调试，退出程序。
    这种通过pdb在命令行调试的方法理论上是万能的，但是实在太麻烦了，如果有一千行代码，要运行到999行的敲多少命令啊。
    于是另一种 pdb.set_trace() 这个方法也是使用pdb，但是不需要单步执行，我们只需要 import pdb，然后，在可能出错的地方放一个pdb.set_trace()，
    就可以设置一个端点。
    运行代码，程序会自动在pdb.set_trace()的地方暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续执行。虽然这个方法比单步
    调试效率要高很多，但是也高不到哪里去。
'''
# IDE
'''
    如果要比较爽地设置端点、单步执行，就需要一个支持调试功能的IDE目前比较好的Python IDE有：
    Visual Studio Code
    PyCharm
'''
'''
写程序最痛苦的事情莫过于调试，程序往往会以你意想不到的流程来运行，你期待执行的语句其实根本没有执行，这时候，就需要调试了。
虽然IDE调试起来比较方便，但是最后你会发现，logging才是终极武器。
'''