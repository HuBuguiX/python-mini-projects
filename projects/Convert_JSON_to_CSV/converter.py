import json

if __name__ == '__main__':
    try:
        # 以读文件的模式打开一个文件对象
        # 第一个参数为包括文件名的路径，第二个参数是打开模式
        # 文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的：f.close()
        # `with`语句来自动帮我们调用`close()`方法
        with open('input.json', 'r') as f:
            # `read()`方法可以一次读取文件的全部内容，Python把内容读到内存，用一个`str`对象表示
            # 把JSON反序列化为Python对象(dict). `json.loads()`把JSON的字符串反序列化
            data = json.loads(f.read())

            # *args: 可变参数。args在函数内部为一个tuple
            output = ','.join([*data[0]])
            for obj in data:
                output += f'\n{obj["Name"]},{obj["age"]},{obj["birthyear"]},'
            
            with open('output.csv', 'w') as f:
                f.write(output)

    except Exception as ex:
        print(f'Error: {str(ex)}')

