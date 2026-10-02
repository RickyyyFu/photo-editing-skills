# 工作流与模板

## 目录

- [最小需求提取](#最小需求提取)
- [摄影策划模板](#摄影策划模板)
- [图像生成提示词](#图像生成提示词)
- [照片分析模板](#照片分析模板)
- [修图方向模板](#修图方向模板)
- [组照选片顺序](#组照选片顺序)

## 最小需求提取

从用户输入中提取：

- 任务：拍摄策划、生成提示词、修图、分析、选片或系列叙事
- 主体：无人物、街头人物、指定人物、物件或品牌
- 地点与进入权限：主街、侧巷、屋顶、室内隔窗、站台等；真实场所的地址、营业状态、时间与规则须当前核验，未核验时不要写成确定事实
- 天气与时间：强雨、小雨、雨后、雪、夜、蓝调时刻
- 输出：单张、组照、横竖比例、平台、商业限制
- 强度：克制、沉浸、实验

若用户未指定且风险不高，默认：原创东京电子街区、雨后仍有小雨、竖幅 4:5、35–50mm 的自然空间感、少量行人、沉浸强度。

## 摄影策划模板

按以下顺序输出：

1. **原创命题**：一句可被画面证明的情绪矛盾。
2. **视觉策略**：空间、天气、光色、人物或物件如何共同工作。
3. **场所与时间**：给出场所类型和进入方式，不虚构许可。
4. **人物与服装**：写动作、与场所的关系、服装功能、道具和禁止项。
5. **镜头与光线**：写焦段范围、机位、景深或快门意图、现有光与补光逻辑。
6. **镜头清单**：至少覆盖建立、细节、人物、反射和收束五种功能。
7. **后期与选片**：说明色彩因果、结构校正、系列节奏和淘汰标准。
8. **安全与许可**：天气、交通、路人、场地方、器材和撤离条件。

### 镜头清单表

| 序号 | 叙事功能 | 主体与动作 | 机位 / 焦段感 | 光与雨面 | 构图重点 | 备选条件 |
| --- | --- | --- | --- | --- | --- | --- |
| 01 | 建立空间 |  |  |  |  |  |
| 02 | 发现细节 |  |  |  |  |  |
| 03 | 引入人物 |  |  |  |  |  |
| 04 | 反射变化 |  |  |  |  |  |
| 05 | 收束余韵 |  |  |  |  |  |

## 图像生成提示词

### 架构

将以下片段写成一段连贯提示词，不机械罗列：

```text
[原创主体与动作] + [具体城市空间及用途] + [天气如何改变至少两种表面] +
[主景、反射和人物的空间层级] + [可解释的人工光源与方向] +
[焦段感、机位、景深或运动表现] + [局部色彩关系] +
[建筑校正、湿纹理与后期克制度] + [叙事矛盾] + [比例与媒介]
```

主提示词中不要只写摄影师姓名。若用户以姓名请求风格，可先说明“已转译为雨夜城市、清晰结构、反射与偶然人物等特征”，再给无姓名成品。

### 街头 / 城市模板

```text
An original [vertical/horizontal] nighttime urban photograph of [specific subject]
in [specific district function and street structure], [rain state] interacting with
[surface 1] and [surface 2]. [Composition hierarchy], with [human scale/action].
Illuminated by [motivated practical sources], [lens and camera-height feel],
[depth/motion treatment]. [Palette relationship] concentrated in reflections while
the architecture remains legible and undistorted. [Texture/post direction].
The mood holds [tension A] against [tension B], grounded in a real, lived-in city.
```

### 环境人物模板

```text
An original environmental portrait of [person/role] [place-related action] in
[specific urban location]. The city remains recognizable through [two anchors].
[Pose and gaze], wearing [functional wardrobe with one distinctive detail], using
[prop] as part of the action. [Motivated key light] plus [ambient practical light],
[lens feel and distance], [rain/glass/metal surface behavior]. Keep skin believable;
let [two colors] live mainly in the background and reflections. [Narrative tension],
[aspect ratio], no studio-backdrop feeling.
```

### 物件 / 商业模板

```text
An original city-object portrait of [product/object] placed naturally at
[specific urban micro-location]. [Weather] reveals [material details]; [light source]
creates a traceable reflection across [surface]. [Composition and lens feel],
[brand/text preservation requirement], [palette relationship], [human trace if any].
Precise structure, controlled glow, tactile wet texture, cinematic but not generic
cyberpunk, [aspect ratio and intended use].
```

### 通用避免项

仅在工具支持负面提示词时单独传入；否则以简短自然语言附在主提示词末尾：

```text
Avoid generic cyberpunk clichés, random neon, warped buildings, gratuitous Dutch
angles, global teal-orange grading, excessive bloom, crushed featureless blacks,
plastic skin, runway poses without context, dry spotless pavement, duplicated
umbrellas, malformed hands, and prominent unreadable AI text.
```

### 示例：原创雨夜城市

```text
Vertical 4:5 nighttime photograph in a lived-in electronics district: a repair-shop
worker lowers a metal shutter while two late commuters cross the narrow side street.
Fine rain beads on the shutter and transparent umbrellas; a shallow gutter mirrors
a red shop lamp and a cool pharmacy sign. The shutter is the main subject, its
reflection forms a second vertical layer, and the commuters provide small-scale
movement in the distance. Eye-level 40mm perspective, straight architecture,
moderate depth of field, rain frozen without looking staged. Coal-blue shadows,
localized red-orange and cyan highlights, restrained glow, crisp wet textures.
The scene feels both near-future and lovingly archival, like a business closing for
the night rather than an empty neon spectacle.
```

## 照片分析模板

先用一段话给结论，再使用下表。没有证据的栏写“无法判断”，不要补齐。

| 维度 | 画面证据 | 与研究语言的关系 | 置信度 | 改进建议 |
| --- | --- | --- | --- | --- |
| 构图 |  |  |  |  |
| 光线 |  |  |  |  |
| 色调 |  |  |  |  |
| 镜头感 |  |  |  |  |
| 人物姿态 |  |  |  |  |
| 场景 |  |  |  |  |
| 服装 / 道具 |  |  |  |  |
| 后期 |  |  |  |  |
| 叙事 |  |  |  |  |

结尾输出：

- 最强相符点：3 项以内
- 主要偏离：2 项以内
- 下一步：1 个最能改变结果的动作

## 修图方向模板

```text
1. 结构：校正无意的垂直 / 水平畸变，保留有意的超广角张力。
2. 曝光：压住环境亮度，保留光源纹理；打开关键暗部而不抬成灰。
3. 颜色：确定主光色与对比色，只在其真实影响区域增加纯度。
4. 水与雨：分别处理雨粒、路面反射、玻璃水滴和金属高光。
5. 主体：用局部明暗与色差引导，不靠全局光晕。
6. 人物：保护肤色、衣料与轮廓；去除不必要的霓虹污染。
7. 输出：按展示尺寸控制降噪、颗粒、锐化与暗部压缩。
```

## 组照选片顺序

1. 用一张地理明确的建立镜头开场。
2. 用两到三张不同尺度的街景建立天气和人流。
3. 插入物件、结构或反射特写，打破连续大景。
4. 在中段放人物最强的一张，不必是最大脸部。
5. 用安静侧巷、关灯、空伞或残留反射收束。
6. 淘汰只有霓虹颜色、没有地点与行为信息的重复画面。
