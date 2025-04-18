# Gakuen_Calc

基于 [HoshinoBotV2](https://github.com/Ice-Cirno/HoshinoBot) 的 [学園アイドルマスター](https://gakuen.idolmaster-official.jp/) 的分数线查询插件

旨在为学友们提供明确的在特定三围下的各评级最低分数线

### 关于N.I.A.

N.I.A.最终选拔属性加成与ランク加成均与三维各Pt有关

- 首次属性加成

| 主属性   | 第二属性 | 第三属性 | 三维 |
| ---------- | ---------- | ---------- | ---------- |
| 40000 | 30000 | 25000 | 各属性PT点(*数据存疑) |
| 172 | 142 | 116 | 各属性加成 |



- 二次属性加成</br>
首次属性加成后各三维 * 各三维倍率</br>
如：vo * vo倍率

- Pt不足的属性加成：不明
- ランク加成：不明

### 说明事项

- 不指定难度的情况，单项属性上限默认1800 -
- N.I.A.模式无法进行精确的分数线，详见[关于N.I.A.](https://github.com/Norca0721/GakuenIdolMasterCalculator?tab=readme-ov-file#%E5%85%B3%E4%BA%8Enia)内容 -

| 难度选项 | regular| pro | master | nia |
| ---------- | ---------- | ---------- | ---------- | ---------- |
| 属性上限 | 1200  | 1500 | 1800 | 2000 |

### 前置条件

- Python 3.9+

### 开启插件

- 在想要开启的群聊中发送：```开启 Gakuen_Calc```

### 指令
```
- /学mas算分 Vo Da Vi [regular|pro|master|nia]
  计算特定三维下各评级所需スコア和ランク
- /学mas算分 Vo Da Vi [スコア|ランク] [regular|pro|master|nia]
  计算特定三维与终测分数能够达成的评级
```
### 更新日志

`项目开始时并没有更新日志，从N.I.A.模式实装时开始记录`

**v 1.0.0 - 2024.12.29**
1. 初模式スコア计算器
2. N.I.A.模式ランク计算器
- 感谢 [学マス評価値計算機](https://gkms-calc.netlify.app/) 和 
[学マス計算機（公開用）](https://docs.google.com/spreadsheets/d/1eEdzfHGi7iXpohR-UHr5-W1z7PcYBqQr8OAV7gcvhR8/edit?gid=0#gid=0)
 提供的算法

### 未来的大饼

1. 使用opencv实现对图片的识别并自动算分
2. 初模式与N.I.A.模式的逆算器