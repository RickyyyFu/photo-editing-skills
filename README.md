# 修图与影像创作技能集

个人修图、摄影处理与影像创作的 Codex 技能仓库。每个技能在 `skills/` 中使用独立子文件夹，便于继续添加其他技能。

## 已收录技能

| 技能 | 作用 | 调用名称 |
| --- | --- | --- |
| [实景拼贴](skills/scenes-gathered-zine-v1-3/) | 保留真实摄影，结合抽象插画、结构色与手撕纸边缘制作纸刊海报 | `$scenes-gathered-zine-v1-3` |
| [影像蒸馏](skills/scene-distillation-zine-v1-3/) | 将照片作为创作参考，重新绘制为不含原始摄影像素的原创纸刊插画 | `$scene-distillation-zine-v1-3` |

## 安装到本机

克隆此仓库后，将需要的技能目录复制到 `~/.codex/skills/`。Windows 上通常是 `C:\Users\<用户名>\.codex\skills\`。

保留目录内部结构，例如 `SKILL.md` 和 `agents/openai.yaml`。若安装目录已存在，请先比较内容或备份，避免直接覆盖。

## 使用

在 Codex 上传一张照片，然后发送：

```text
用 $scenes-gathered-zine-v1-3 把这张照片制作成纸刊拼贴海报。
保留主要人物和场景关系，文字使用中文，其他设计请根据照片决定。
```

或：

```text
用 $scene-distillation-zine-v1-3 重新创作这张照片。
主题是“靠近与错过”，使用大量留白，最终画面只保留原创插画。
```

影像蒸馏支持在请求中加入准确的 `单色块模式`，使用一整块高饱和色与中性黑灰绘制其余元素。

## 添加其他技能

在 `skills/` 下新增以技能名称命名的目录，并加入它的 `SKILL.md` 及所需配置、资源。第三方技能应同时保留原作者署名、来源和对应许可证。

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
```

## 作者与许可

目前这两个技能由 **Zeejay0** 创作，本仓库仅作个人收集与备份，未修改技能正文及配置。

来源：[Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill)。技能取自提交 [`899b32a322de82cce46a831b78433a6062288ddb`](https://github.com/Zeejay0/gathered-scenes-zine-skill/tree/899b32a322de82cce46a831b78433a6062288ddb)，即此前安装使用的版本。

这两个技能分别保留原始 **Gathered Scenes Zine Personal Non-Commercial License**，仅限个人非商业用途。免费分享必须保留许可证、署名和来源，并适用相同条款；商业用途需取得作者的书面授权。

本仓库不对所有技能设置统一许可证。未来新增的技能适用各自目录内的许可条款。
