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

转换后的 HTML 页面： [https://xlzd.me/hide/img2html/](https://xlzd.me/hide/img2html/)


原始图片             |  转换后
:-------------------------:|:-------------------------:
![](https://raw.githubusercontent.com/xlzd/img2html/master/demo/before.png)  |  ![](https://raw.githubusercontent.com/xlzd/img2html/master/demo/after.png)

### 使用方式
---

#### 命令行
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


#### 代码调用

```Python
from img2html.converter import Img2HTMLConverter

converter = Img2HTMLConverter(*some config here*)
html = converter.convert(*image_path*)

# done, so easy.
```


### 安装
---

`img2html` 已经上传到了 [PYPI](https://pypi.python.org/pypi/img2html)，所以最简单的安装方式就是使用 pip：

```
$ pip install img2html
```

更新：

```
$ pip install img2html --upgrade
```


当然，你也可以通过源码安装：

```
$ git clone https://github.com/xlzd/img2html.git
$ cd img2html
$ python setup.py install
```


### License
---

WTFPL ([here](https://github.com/xlzd/img2html/blob/master/LICENSE))


[version-badge]:   https://img.shields.io/pypi/v/img2html.svg?label=version
[version-link]:    https://pypi.python.org/pypi/img2html/
[license-badge]:   https://img.shields.io/badge/license-WTFPL-007EC7.svg
