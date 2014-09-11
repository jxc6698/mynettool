mynettool
=========

this project aims to get others' bras account

try to use two language  C  and Python 

use raw socket to get bras account and password when we stay in the same route. When peopen login bras(p.nju.edu.cn), this web use account and password in the text. so I just need to extract them out 


2014年 09月 09日 星期二 17:22:01 CST
多次测试和百度，已经解决了从数据包中取出  username 和 password 的问题
但我现在面临的是，在系楼我的电脑是抓不到别人访问 p.nju.edu.cn的数据包的，不知道是不是由于这里的交换技术已经从集线器升级到了交换机（交换机是直接通过端口转发，不会把别人的数据包转发给我的)

下一步目标，实现arp欺骗，从而可以拿到别人的数据包


2014年 09月 11日 星期四 10:14:47 CST

实现了arp欺骗，并且在arp欺骗以后进行了 数据包转发，这样可以主机发送出去的数据（我觉得在交换场景下已经很好了）

在往下就是arp欺骗，和对于cookies 的识别和利用（包括Portal具体是怎么认证的）
或者是找机会 可以潜入别人的主机


