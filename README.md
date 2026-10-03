# 修图与影像创作技能集

这是一个供个人使用的 Codex 修图与影像创作技能仓库。每个技能在 `skills/` 中使用独立子文件夹，方便以后继续添加其他技能。

当前收录四个技能，覆盖纸刊海报、原创插画、自然光旅行摄影与雨夜城市摄影。它们提供创作流程与提示词规则，实际出图需要当前 Codex 环境具备图像生成能力。

**快速开始：下载下面的单技能 ZIP，把压缩包和照片一起上传给 Agent，再复制启动指令。无需 Git，也无需记住技能调用名称。**

已安装技能的 Codex 用户仍可直接上传照片并使用 `$技能名` 调用。

## 已收录技能

| 技能 | 作用 | 调用名称 |
| --- | --- | --- |
| [实景拼贴](skills/scenes-gathered-zine-v1-3/) | 保留真实摄影，结合抽象插画、结构色与手撕纸边缘制作纸刊海报 | `$scenes-gathered-zine-v1-3` |
| [影像蒸馏](skills/scene-distillation-zine-v1-3/) | 将照片作为创作参考，重新绘制为不含原始摄影像素的原创纸刊插画 | `$scene-distillation-zine-v1-3` |
| [Roberta Mazzone 摄影指导](skills/roberta-mazzone-photography/) | 自然光、建筑框景、克制暖色的摄影规划、修图指导与图像提示词 | `$roberta-mazzone-photography` |
| [Junya Watanabe 摄影指导](skills/junya-watanabe-photography/) | 雨夜城市、人工光与湿表面反射的摄影规划、修图方向和图像提示词 | `$junya-watanabe-photography` |

### 应该选哪个？

- 想保留原照片的真实人物、建筑与场景，并加入纸面、插画和手撕边缘：选 **实景拼贴**。
- 想把照片中的情绪和关系重新创作为一幅插画：选 **影像蒸馏**。
- 想做自然光、建筑框景、温暖克制的旅行生活摄影：选 **Roberta Mazzone 摄影指导**。
- 想分析或创作雨夜城市、招牌光线、路面与玻璃反射：选 **Junya Watanabe 摄影指导**。

实景拼贴默认竖版 `3:5`，带一条安静的小字；默认小字为英文，想用中文需要明确说明。影像蒸馏默认跟随原图方向：竖图使用 `3:5`，横图使用 `5:3`，文字可自由设计，也可以要求不加文字。

## 下载并上传使用（推荐，无需 Git）

| 效果 | 下载技能包 | 适合的任务 |
| --- | --- | --- |
| 实景拼贴 | [下载 ZIP](downloads/scenes-gathered-zine-v1-3.zip?raw=true) | 保留真实照片，结合插画与手撕纸边缘制作海报 |
| 影像蒸馏 | [下载 ZIP](downloads/scene-distillation-zine-v1-3.zip?raw=true) | 把照片重新创作为原创插画海报 |
| 自然光旅行摄影 | [下载 ZIP](downloads/roberta-mazzone-photography.zip?raw=true) | 自然光旅行照片的分析、修图与拍摄指导 |
| 雨夜城市摄影 | [下载 ZIP](downloads/junya-watanabe-photography.zip?raw=true) | 雨夜街景、人工光与反射的分析、修图与创作指导 |

1. 下载想用的技能 ZIP，每次任务通常选择一个。
2. 将 ZIP 和照片一起上传给支持解压和读取文件的 Agent。
3. 复制下面的启动指令，填写希望的效果、文字或修图要求：

```text
请解压我上传的技能包，读取其中的 SKILL.md 及其要求的参考文件，按技能规则处理我上传的照片。先确认能访问包内文件；无法解压或读取时请明确告知。
我的要求：制作纸刊拼贴海报，文字用中文，其他设计根据照片决定，请直接生成成品图。
```

上面的示例适用于“实景拼贴”。使用其他包时，把“我的要求”换成对应任务：影像蒸馏可写“重新创作为原创插画海报，不保留原照片片段”；自然光旅行摄影可写“轻微暖色，保护高光，保留人物身份与场景结构，生成修图预览”；雨夜城市摄影可写“分析现有光线和反射，保留人物与建筑结构，避免过度饱和与辉光，生成修图预览”。每个包内的 `START-HERE.md` 也提供对应启动指令。

**使用条件：**直接出图需要 Agent 能调用图像生成或编辑工具；没有图像工具时，可要求输出提示词或修图方案。上传附件用于当前任务按规则执行，不一定会安装成长期可调用的技能。

若 Agent 无法解压 ZIP，在本地解压后上传完整文件夹（平台支持时），或按下面的方法安装。两个摄影技能包含必读 `references/`，请保留；其他包内的配置、许可证及来源文件也应一起保留。

全部技能也可通过 [下载完整仓库 ZIP](https://github.com/RickyyyFu/photo-editing-skills/archive/refs/heads/main.zip) 获取。解压后在 `skills/` 下选择所需技能；用于安装的是各个技能文件夹，而非整个仓库文件夹。

实景拼贴和影像蒸馏仅限个人非商业用途，分享时保留原作者署名、来源和许可，详见文末“作者与许可”。

## 安装到 Codex（长期使用）

### 1. 获取仓库

先安装 Git，然后在你希望存放仓库的目录运行：

```sh
git clone https://github.com/RickyyyFu/photo-editing-skills.git
cd photo-editing-skills
```

本仓库为公开仓库，下载或克隆无需登录 GitHub。也可以下载上面的单技能 ZIP，解压后直接复制技能文件夹，无需安装 Git。如果本机已有此仓库，进入原目录即可；更新前先保存自己的修改，再运行 `git pull --ff-only`。

### 2. 复制需要的技能

下面的安装命令均在仓库根目录执行。它们遇到同名目标目录会跳过，避免覆盖已有技能。只想装部分技能时，从名称列表中删去不需要的技能即可。

#### Windows：PowerShell

```powershell
$skillsRoot = Join-Path $env:USERPROFILE '.codex\skills'
New-Item -ItemType Directory -Path $skillsRoot -Force | Out-Null

$skillNames = @(
    'scenes-gathered-zine-v1-3',
    'scene-distillation-zine-v1-3',
    'roberta-mazzone-photography',
    'junya-watanabe-photography'
)

foreach ($name in $skillNames) {
    $source = Join-Path (Join-Path (Get-Location) 'skills') $name
    $target = Join-Path $skillsRoot $name
    if (-not (Test-Path -LiteralPath (Join-Path $source 'SKILL.md') -PathType Leaf)) {
        throw "找不到技能源文件，请确认当前位于仓库根目录：$name"
    }
    if (Test-Path -LiteralPath $target) {
        Write-Host "已存在，跳过：$target"
        continue
    }
    Copy-Item -LiteralPath $source -Destination $skillsRoot -Recurse
    Write-Host "已安装：$target"
}
```

默认安装位置通常是 `C:\Users\<用户名>\.codex\skills\`。

#### macOS / Linux：终端

```sh
mkdir -p "$HOME/.codex/skills"
for name in scenes-gathered-zine-v1-3 scene-distillation-zine-v1-3 roberta-mazzone-photography junya-watanabe-photography; do
  if [ ! -f "skills/$name/SKILL.md" ]; then
    printf '找不到源文件，请在仓库根目录执行：%s\n' "$name"
    break
  fi
  if [ -e "$HOME/.codex/skills/$name" ]; then
    printf '已存在，跳过：%s\n' "$name"
  else
    cp -R "skills/$name" "$HOME/.codex/skills/"
    printf '已安装：%s\n' "$name"
  fi
done
```

如果你自定义了 Codex 的技能安装目录，请替换上述目标路径。

### 3. 确认安装

确认每个目标目录内直接包含 `SKILL.md`，而不是多嵌套了一层同名文件夹；同时保留 `agents/openai.yaml`、许可证及来源文件。

开始新一轮对话并显式调用技能。如果没有被识别，可重启 Codex 后重试。

## 如何使用

1. 在 Codex 对话中上传照片，或提供本机照片的完整路径。
2. 用 `$技能名` 点名调用，并写清楚希望保留的主体、文字语言与情绪方向。
3. 查看成品后继续提出具体修改，例如“留白更多”“红色面积缩小”“保留人物位置”。

不确定设计细节时，可以写“其他设计根据照片决定”。希望只看方案时，明确写“只给提示词，先不要生成图片”。

### 示例一：实景拼贴

```text
用 $scenes-gathered-zine-v1-3 把我上传的照片制作成竖版 3:5 纸刊拼贴海报。
保留主要人物与远处风景的真实关系，简化背景细节，保留大量留白和手撕纤维边缘。
使用钴蓝色作为结构色，小字使用中文：“风从远处来”。
请直接生成成品图，并附简短创作说明。
```

实景拼贴的小字适合简短表达：自动创作的中文通常不超过 8 个汉字，英文不超过 5 个单词。你提供的文字会按原文使用；短句更适合这个技能的画面风格。

### 示例二：影像蒸馏

```text
用 $scene-distillation-zine-v1-3 重新创作我上传的照片。
主题是“靠近与错过”，保留人物姿态、空间距离和情绪线索。
最终画面不要出现原照片片段，只使用原创插画、纸面和文字。
使用大量留白和高饱和朱红色，中文文案与排版由你决定。
请直接生成成品图，并附创作想法和简短艺术指导。
```

### 示例三：单色块模式

仅影像蒸馏支持这个模式，必须在请求中准确写出 **`单色块模式`**：

```text
用 $scene-distillation-zine-v1-3 的单色块模式处理这张照片。
使用一整块高饱和柠檬黄作为主体结构，其余绘制元素使用中性黑灰色。
保留大量留白，不加文字，直接生成图片。
```

这个模式强调一个连续的高饱和色块。没有写出触发词时，默认使用常规重点色模式，可以有少量同色呼应。

### 示例四：同一张照片做两版对比

```text
请用同一张照片分别生成两版：
第一版使用 $scenes-gathered-zine-v1-3，保留真实摄影。
第二版使用 $scene-distillation-zine-v1-3，完全重新绘制为插画。
两版使用同样的暖红色方向，方便比较效果。
```

### 生成后怎么修改

```text
继续修改刚才的海报：留白更多，红色面积缩小，保留塔楼的位置和比例。
小字改成“远处有风”，不要增加其他文字。
```

一次提出少量具体调整，更容易判断修改效果。

### 示例五：自然光旅行照片修图

```text
$roberta-mazzone-photography
用 edit 模式处理我上传的照片，只处理这一张。
轻微暖色、保护高光、保留深色阴影和真实材质。
保留人物身份、姿势、服装及场景结构；不要新增或移动物体。
请根据现有光线给出修图方向；如果当前环境支持图像编辑，请生成预览。
```

更多模式与示例见 [Roberta Mazzone 中文指南](skills/roberta-mazzone-photography/README.md)。需要拍摄策划时，把 `edit` 改成 `shoot`；需要照片点评时，使用 `critique`。

### 示例六：雨夜城市照片分析与修图

```text
用 $junya-watanabe-photography 分析我上传的这张雨夜街景。
从构图、人工光、湿路面反射、人物和色彩层次说明优点与改进方向。
再给出修图方案：保护人物身份与建筑结构，突出红橙招牌和路面反射，
避免全局过饱和、过度辉光和皮肤偏青。
```

更多示例见 [Junya Watanabe 中文指南](skills/junya-watanabe-photography/README.md)。

### 示例七：摄影创作提示词与拍摄计划

```text
用 $junya-watanabe-photography 设计一组原创雨夜城市摄影，共 5 张。
地点以普通商业街为背景，用路面、玻璃与雨伞表现人工光的反射。
给出中文拍摄计划和每张图的完整生成提示词，先不要生成图片。
```

两个摄影指导技能支持分析、策划与提示词编写。需要实际出图时明确说明张数、比例和“请直接生成”；照片分析或修图建议请求不会自动代表你想替换照片内容。

## 常见问题

**安装了却没识别到技能？**

检查文件夹名称、安装位置与 `SKILL.md` 是否直接在技能目录内。再开始新对话或重启 Codex，并完整写出 `$技能名`。

**为什么只有文字，没有生成图片？**

先明确写“请直接生成成品图”。如果当前环境没有图像生成工具，技能本身不能提供出图服务；这时可以让 Codex 输出生成提示词，再交给支持参考图的图像工具使用。

**怎么指定比例、颜色和文字？**

直接写在请求里，例如“横版 5:3”“重点色用番茄红”“小字使用中文”。实景拼贴默认带微文字；影像蒸馏可以明确要求不加文字。需要特定文案时，用引号给出准确内容，并检查生成后的文字。

**照片会被用于图像生成吗？**

实际生成时，必要的参考照片和提示词会提交给图像生成服务。涉及敏感信息时，请先选择合适的照片或自行处理敏感区域。

**已有同名技能，怎么更新？**

上述安装命令会跳过同名目录。先比较现有目录与仓库版本，把旧版备份到技能安装目录以外，再复制需要的新版本。更新仓库本身不会自动更新本机已安装技能。

## 添加其他技能

在 `skills/` 下新增以技能名称命名的目录，并加入它的 `SKILL.md` 及所需配置、资源，然后在上面的“已收录技能”表中增加一行。第三方技能应同时保留原作者署名、来源和对应许可证。

发布前确认目录里没有私人照片、生成结果、密钥或账号信息。本仓库已经通过 `.gitignore` 排除常见照片目录、生成结果目录及 `.env` 文件；提交时仍需检查实际文件。

```text
skills/
  scenes-gathered-zine-v1-3/
    SKILL.md
    agents/openai.yaml
    LICENSE
    SOURCE.md
  scene-distillation-zine-v1-3/
    SKILL.md
    agents/openai.yaml
    LICENSE
    SOURCE.md
  roberta-mazzone-photography/
    SKILL.md
    README.md
    agents/openai.yaml
    references/
  junya-watanabe-photography/
    SKILL.md
    README.md
    agents/openai.yaml
    references/
```

## 作者与许可

实景拼贴与影像蒸馏这两个技能由 **Zeejay0** 创作，本仓库仅作个人收集与备份，未修改技能正文及配置。

来源：[Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill)。技能取自提交 [`899b32a322de82cce46a831b78433a6062288ddb`](https://github.com/Zeejay0/gathered-scenes-zine-skill/tree/899b32a322de82cce46a831b78433a6062288ddb)，即此前安装使用的版本。

这两个技能分别保留原始 **Gathered Scenes Zine Personal Non-Commercial License**，仅限个人非商业用途。免费分享必须保留许可证、署名和来源，并适用相同条款；商业用途需取得作者的书面授权。

本仓库不对所有技能设置统一许可证。未来新增的技能适用各自目录内的许可条款。

Roberta Mazzone 摄影指导由本仓库用户与 Codex 协作创建，依据公开作品和采访进行独立分析。它不是摄影师的官方技能，也未获得其授权；公开照片未打包收录，参考来源见该技能的 `references/sources.md`。

Junya Watanabe 摄影指导针对东京摄影师 `@jungraphy_`，而非同名时装设计师。它根据公开资料形成独立研究与创作指导，不代表摄影师本人，也不表示获得其授权。公开照片未打包收录，参考来源见该技能的 [来源记录](skills/junya-watanabe-photography/references/sources.md)。

## 维护下载包

技能内容更新后，从仓库根目录运行 `python scripts/package_skills.py`，重新生成 `downloads/` 下的四个 ZIP。脚本会检查压缩包完整性，并逐文件核对技能源文件；发布修改时同步提交下载包。
