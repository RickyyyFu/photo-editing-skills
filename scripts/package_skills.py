"""Build and verify independently uploadable skill ZIPs using Python 3."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
PACKAGES = {
    'scenes-gathered-zine-v1-3': ('实景拼贴', '保留真实摄影，制作纸刊拼贴海报，小字用中文，其他设计根据照片决定，直接生成成品图。'),
    'scene-distillation-zine-v1-3': ('影像蒸馏', '把照片重新创作为原创插画海报，不保留原照片片段，文字用中文，其他设计根据照片决定，直接生成成品图。'),
    'roberta-mazzone-photography': ('自然光旅行摄影', '用 edit 模式处理这一张照片，轻微暖色、保护高光、保留真实材质及人物身份和场景结构，不新增或移动物体；请生成修图预览。'),
    'junya-watanabe-photography': ('雨夜城市摄影', '分析这张照片的现有光线与反射，给出修图方案并生成预览；保留人物身份与建筑结构，避免过度饱和和辉光，不凭空添加雨夜或霓虹元素。'),
}


def build():
    destination = ROOT / 'downloads'
    destination.mkdir(exist_ok=True)
    for name, (label, task) in PACKAGES.items():
        source = ROOT / 'skills' / name
        assert (source / 'SKILL.md').is_file(), name
        files = sorted(p for p in source.rglob('*') if p.is_file())
        instruction = f'请解压技能包，读取 {name}/SKILL.md 及其要求的参考文件，按规则处理我上传的照片。任务：{task}'
        guide = f'''# {label}：上传使用

1. 将本 ZIP 和照片一起上传给支持解压、文件读取与图像生成/编辑的 Agent。
2. 复制以下指令：

> {instruction}

若无法解压，请本地解压后上传完整文件夹（平台支持时）。无法读取文件时，请让 Agent 明确告知；没有图像工具时，可先输出提示词或修图方案。
附件不一定会安装为长期技能。安装时将整个 {name} 文件夹放到平台规定的 Skill 目录，保留相对路径。
本包保留技能源文件、来源和许可；如含 LICENSE / SOURCE.md，使用和分享时请遵守并保留。源仓库：https://github.com/RickyyyFu/photo-editing-skills
'''
        archive_path = destination / f'{name}.zip'
        with ZipFile(archive_path, 'w', ZIP_DEFLATED) as archive:
            for path in files:
                archive.write(path, f'{name}/{path.relative_to(source).as_posix()}')
            archive.writestr(f'{name}/START-HERE.md', guide)
        with ZipFile(archive_path) as archive:
            assert archive.testzip() is None
            for path in files:
                assert archive.read(f'{name}/{path.relative_to(source).as_posix()}') == path.read_bytes()
        print(f'{archive_path.name}: verified {len(files)} source files')


if __name__ == '__main__':
    build()
