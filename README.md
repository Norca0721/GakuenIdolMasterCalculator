# Gakuen_Calc

基于 [HoshinoBotV2](https://github.com/Ice-Cirno/HoshinoBot) 的 [学園アイドルマスター](https://gakuen.idolmaster-official.jp/) 的分数线查询插件

旨在为学友们提供明确的在特定三围下的各评级最低分数线

### 说明事项
```
不指定难度的情况，单项属性上限默认1800
N.I.A.模式的最终选拔通过的ランク奖励算法缺失
难度选项：regular|  pro  | master |  nia
属性上限： 1200  | 1500  |  1800  | 2000
```
### 前置条件

- Python 3.9+

### 开启插件

- 在想要开启的群聊中发送：```开启 Gakuen_Calc```

### 指令

- /学mas算分 Vo Da Vi [regular|pro|master|nia]  |  计算特定三维下各评级所需スコア和ランク
- /学mas算分 Vo Da Vi [スコア|ランク] [regular|pro|master|nia]  |   计算特定三维与终测分数能够达成的评级

### 更新日志

`项目开始时并没有更新日志，从N.I.A模式实装时开始记录`

**v 1.0.0 - 2024.12.29**
1. 初模式スコア逆算器和计算器
2. N.I.A模式ランク逆算器和计算器
- 感谢 [学マス評価値計算機](https://gkms-calc.netlify.app/) 和 
[学マス計算機（公開用）](https://docs.google.com/spreadsheets/d/1eEdzfHGi7iXpohR-UHr5-W1z7PcYBqQr8OAV7gcvhR8/edit?gid=0#gid=0)
 提供的算法

### 未来的大饼

1. 使用opencv实现对图片的识别并自动算分