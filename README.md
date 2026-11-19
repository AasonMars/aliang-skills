# Aliang Skills

一组用于内容研究、创作与个人成长管理的可复用 Agent Skills。每个 skill 将一项工作整理成可供 AI 助手执行的流程。

## Skill 列表

| Skill | 用途 | 输入与输出 |
| --- | --- | --- |
| [Aliang Growth Workbench](skills/aliang-growth-workbench/SKILL.md) | 建立个人成长工作台，整理规则、记忆、知识、能力、待办和项目 | 输入工作台位置及希望整理的资料范围；生成属于使用者的工作台 |
| [Aliang Research](skills/aliang-research/SKILL.md) | 研究对标作者的近期作品、评论需求和视频脚本 | 输入作者主页或作品链接；输出研究结果，可按需整理为飞书多维表格 |

## 安装个人成长工作台

克隆本仓库后，在仓库根目录执行：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
if [ -e "${CODEX_HOME:-$HOME/.codex}/skills/aliang-growth-workbench" ]; then
  echo "aliang-growth-workbench 已存在，请先检查已有版本。"
else
  cp -R skills/aliang-growth-workbench "${CODEX_HOME:-$HOME/.codex}/skills/aliang-growth-workbench"
fi
```

重新启动 Codex 或开启新会话，然后说：“使用 aliang-growth-workbench，帮我建立个人成长工作台。”首次建立需要一个新目录或空目录；已有资料时由 AI 先检查并提出整理方案。技能使用本机已有 Python 3，自动生成的路由和分类视图在记录更新后刷新，不会后台持续运行。第三方代码及许可证保留在技能资源中。

## 使用前了解

- Skill 是工作指引，不自带社交平台数据接口、视频下载服务、语音识别模型或飞书连接。
- 需要研究的数据须能通过当前环境中可用、已授权的工具获取；评论、互动数据及视频的可获取范围取决于平台和服务。
- 下载视频、机器转写及写入飞书是按需执行的步骤。相应步骤需要可访问的媒体、可用的语音识别能力或可编辑的飞书多维表格权限。
- 第三方服务可能收费或对数据量、访问频率有限制。缺少能力或权限时，应说明具体缺口，不编造数据。

## 安装到 Codex

先克隆仓库，在仓库根目录执行：

```bash
git clone https://github.com/AasonMars/aliang-skills-public.git
cd aliang-skills-public
```

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
if [ -e "${CODEX_HOME:-$HOME/.codex}/skills/aliang-research" ]; then
  echo "aliang-research 已存在，请先检查已有版本。"
else
  cp -R skills/aliang-research "${CODEX_HOME:-$HOME/.codex}/skills/aliang-research"
fi
```

重新启动 Codex 或开启新会话后，可在对话中直接提及 `aliang-research` 或描述适用任务。其他支持 Agent Skills 的工具可能使用不同的安装目录和加载方式，请按该工具的说明安装。

## 使用示例

将下面的占位内容替换为你有权研究的真实链接：

```text
使用 aliang-research，研究这个作者最近 30 天可获取的作品：
<作者主页或作品链接>

整理每条作品的标题、发布时间、互动数据和原始链接；
总结选题结构与评论中的常见需求；
对可获取的视频进行转写，分析开场、句长、转折和结尾。
下载可用的视频和封面，并整理到飞书多维表格。
```

也可以只要求账号研究、评论分析或整理现有资料。实际输出应标明采集时间、数据覆盖范围、转写来源和不可获取的内容；飞书表格创建与文件上传以用户授权为前提。

## 仓库结构

```text
skills/
  aliang-growth-workbench/
    SKILL.md
    scripts/
    assets/
  aliang-research/
    SKILL.md
```

后续 skill 以 `aliang-` 开头，放在各自目录中；按实际需要增加参考资料、脚本或资源。

## 隐私与分享

仓库只保存通用方法和虚构示例。提交前检查文件与版本历史，排除真实账号、作品及评论、转写稿、表格数据和链接、凭据、日志与个人路径。研究成果由使用者自行管理，不应自动提交至公开仓库。

## 许可证

本仓库采用 [MIT License](LICENSE)，允许按许可证使用、修改和分发，包括商业使用。平台作品及第三方素材的权利不因本许可证改变；仓库中如有单独标注的内容，遵循其对应许可。

## 私有 Git 与本地工作台

建立工作台时，AI 可优先介绍私有 GitHub 仓库加本地克隆方案，也可先只在本地建立。创建远程仓库、提交或推送前按用户授权执行；已有资料先检查，不覆盖。支持对仅含 `.git`、没有提交和暂存内容的空仓库初始化。

新工作台默认忽略个人记忆、收件箱、项目和归档内容（各 README 除外）以及常见凭据文件；这些被忽略的内容不会被 Git 自动备份。知识库、能力库等仍可能包含个人信息，每次提交前应检查实际待上传文件，并确认远程仓库为私有。


获取本技能所克隆的是公开技能仓库；个人工作台应由使用者在本人选择和授权的本地目录及私有仓库中独立建立，不包含作者的个人数据。
