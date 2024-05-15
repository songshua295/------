---
title: Readme
date: 2024-05-15T07:39:14Z
lastmod: 2024-05-15T22:05:58Z

---

alias：[小鹤音形词库转换工具,小鹤方案,搜狗挂接]

项目地址：[songshua295/flypy-wanciwang (github.com)](https://github.com/songshua295/flypy-wanciwang)

# Change Log

* 2024-05-15  v2.15

  * 思路转变，提供词库转换工具。词库不应该具有唯一性，而是因人而异，比如说商业接触到的更多是商业词汇，而很少用到纺织行业的词汇，所以没必要加上那些奇怪的用不到的词汇。
  * 支持搜狗细胞词库scl转换成小鹤音形编码：

    * [搜狗细胞词库_词库下载_词典_输入法字典 (sogou.com)](https://pinyin.sogou.com/dict/)

* 2024-05-11  v1.5

  * 优化词库中的部分词：部分词已经极其少见，直接删除。

* 2024-05-03  v1.0

  * 优化了单字库的一些生僻字，如yurx伛：主要是[GB18030](https://www.google.com/url?sa=t&amp;rct=j&amp;q=&amp;esrc=s&amp;source=web&amp;cd=&amp;cad=rja&amp;uact=8&amp;ved=2ahUKEwiqtqGVqY6GAxUvk1YBHSD1DTEQFnoECA8QAQ&amp;url=https%3A%2F%2Fopenstd.samr.gov.cn%2Fbzgk%2Fgb%2FnewGbInfo%3Fhcno%3DA1931A578FE14957104988029B0833D3&amp;usg=AOvVaw3o7r20mVC3mcyKebr4jnoN&amp;opi=89978449)和GBK中的字集，数据来源：

    * [GBK 编码表 - 锤子在线工具 (toolhelper.cn)](https://www.toolhelper.cn/Encoding/GBK)
    * [https://github.com/zpeng1989/number_of_bihua_chi.git](https://github.com/zpeng1989/number_of_bihua_chi.git)
  * 添加基础词库，弥补词库量太少的问题：使用的五笔中的词库，更实用。

    * 词库数据来源：[rime/rime-wubi: 【五筆字型】輸入方案 (github.com)](https://github.com/rime/rime-wubi)

  ‍

# 🗒1 概述

小鹤-万磁王是基于官方⌨[小鹤音形](https://google.tigermed.net/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwil3faz5vCFAxVPi68BHQicAt8QFnoECBcQAQ&url=https%3A%2F%2Fflypy.com%2F&usg=AOvVaw3gBahnwrM4WIiTnS9C_eh9&opi=89978449)的一个进阶方案，主要体现在词和字库量的提升，以及对部分词库进行了优化。

# 🕴2 方案适用人群

在经历数次的输入方案更换后（全拼-->智能ABC双拼7年-->五笔2年-->小鹤音形2年），我最终采用了小鹤音形的输入方案。

音码对于日常来说，以读为写的方式，奠定了其<u>听打、想打</u>的优势，更适合日常使用场景；而五笔等诸多全形码方案则在更适用于看打、录入场景，同时其拆字、想字等是需要高出音码多倍的学习成本的。固而，我将使用了两年余久的五笔换成了小鹤，因为我清楚小鹤音形更适合于我。小鹤音形的适合人群：

1. 使用小鹤双拼的人群，进而可以提升，使用小鹤音形；
2. 使用双拼或全拼，可以更换至小鹤音形；
3. 短期内（这里以1个月为基准）需要提升打字速度的人，可以通过学习小鹤双拼，减少码长进而减少击键量，之后可以考虑学习形码来减少选重。
   1. 码长：每个字击打键盘的数量；
   2. 击键量：打完文章敲击键盘的次数；
   3. 选重：比如拼音中的读音“zhong”有多个汉字“中、钟、重”等，此时我们需要按数字键或者翻页键=，对字进行二次选择。

# 🫂3 此方案解决的问题

小鹤官方不论是挂接方案还是官方app，对于词或字的安排都似乎已经到了诸多不合理的场景，所以为了更加适合听打、想打人群，故而希望将词库、字库进行优化，作为挂接方案到可以自定以的输入方案中。

此方案解决的问题以及思路如下：

1. **增大字库**：官方中挂接码单字库仅仅包含了8千余字，一些常用字没有，如伛yurx，现将<u>五笔方案</u>中的简体单字全部加入。
2. **增大词库**：官方大量的常用词没有，进而加入了大量二字词作为二、三位置候选，如果该码没有单字则作为首候选；
3. 优化候选：官方词库中的四字词大量占用了二字词的位置，如万事俱备（无尽）。故将二字词加入作为二候选，将四字词全部作为末尾候选词。

# ❔4 此方案存在的问题

不论是五笔等形码还是小鹤音形这种音形码，都无可避免的一个问题就是——词库量一旦提升，就会**增加击键量**。

所以此优化方案侧重的是**日常使用场景，如听课总结、办公客服、日常写作**，更多的是为了减少选重和击键量的基础上，优化输入手感。

# [](https://github.com/songshua295/flypy-wanciwang.git)👍5 参考与致谢

排名不分先后

1. 搜狗词库转换：[github@lewangdev](https://github.com/lewangdev)
2. 小鹤音形方案：@何海峰
3. 630方案群友
4. [深蓝 - 博客园 (cnblogs.com)](https://www.cnblogs.com/studyzy)：深蓝词库转换
5. 流弊的我

# 📧6 意见反馈与优化

建议使用github的issue版块上提意见，如果因网络环境等也可以使用邮箱反馈。

github提意见点我

[邮件点我](mailto:tianzhongs@foxmail.com)

‍