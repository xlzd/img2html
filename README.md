# img2html: Convert a image to HTML  [![Version][version-badge]][version-link] ![WTFPL License][license-badge]


`img2html` 用于将图片转化为 HTML 页面，并没有什么实际作用，只是为了好玩。

```
                                 ___      __          __                    ___
 __                            /'___`\   /\ \        /\ \__                /\_ \
/\_\     ___ ___       __     /\_\ /\ \  \ \ \___    \ \ ,_\    ___ ___    \//\ \
\/\ \  /' __` __`\   /'_ `\   \/_/// /__  \ \  _ `\   \ \ \/  /' __` __`\    \ \ \
 \ \ \ /\ \/\ \/\ \ /\ \L\ \     // /_\ \  \ \ \ \ \   \ \ \_ /\ \/\ \/\ \    \_\ \_
  \ \_\\ \_\ \_\ \_\\ \____ \   /\______/   \ \_\ \_\   \ \__\\ \_\ \_\ \_\   /\____\
   \/_/ \/_/\/_/\/_/ \/___L\ \  \/_____/     \/_/\/_/    \/__/ \/_/\/_/\/_/   \/____/
                       /\____/
                       \_/__/
```


### 示例

原始图片             |  转换后
:-------------------------:|:-------------------------:
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200822122243148.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0NPQ081Ng==,size_16,color_FFFFFF,t_70#pic_center)|![在这里插入图片描述](https://img-blog.csdnimg.cn/20200822122129328.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0NPQ081Ng==,size_16,color_FFFFFF,t_70#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200822122255159.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0NPQ081Ng==,size_16,color_FFFFFF,t_70#pic_center)|![在这里插入图片描述](https://img-blog.csdnimg.cn/20200822122141183.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0NPQ081Ng==,size_16,color_FFFFFF,t_70#pic_center)
### 使用方式
---

#### 命令行
使用帮助：
```
usage: img2html [-h] [-b #RRGGBB] [-s 4~30] [-c CHAR] [-t TITLE] [-f FONT] -i
                IN [-o OUT]

img2html : Convert image to HTML

optional arguments:
  -b #RRGGBB, --background #RRGGBB  background color (#RRGGBB format)
  -s (4~30), --size (4~30)          font size (int)
  -c CHAR, --char CHAR              characters
  -t TITLE, --title TITLE           html title
  -f FONT, --font FONT              html font
  -i IN, --in IN                    image to convert
  -o OUT, --out OUT                 output file
```

使用实例：
直接在命令行中输入`img2html -i 图片路径 -o 网页路径`

如：`img2html -i D:\before4.png -o D:\index.html`

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200822123102209.png#pic_center)


#### 代码调用

```Python
from img2html.converter import Img2HTMLConverter

converter = Img2HTMLConverter(*some config here*)
html = converter.convert(*image_path*)

# done, so easy.
```


### 安装
---
对于Python3.x来说，由于作者没有适配Python3.x，因此应通过我写的源码安装：

```
$ git clone https://github.com/cocos56/img2html.git
$ cd img2html
$ python setup.py install
```


对于Python2.x来说

`img2html` 已经上传到了 [PYPI](https://pypi.python.org/pypi/img2html)，所以最简单的安装方式就是使用 pip：

```
$ pip install img2html
```

更新：

```
$ pip install img2html --upgrade
```

卸载：
```
pip uninstall img2html
```

### License
---

WTFPL ([here](https://github.com/xlzd/img2html/blob/master/LICENSE))


[version-badge]:   https://img.shields.io/pypi/v/img2html.svg?label=version
[version-link]:    https://pypi.python.org/pypi/img2html/
[license-badge]:   https://img.shields.io/badge/license-WTFPL-007EC7.svg
